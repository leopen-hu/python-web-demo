#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 尝试学习编写一个ORM

# 为了复用数据库连接，首先定义一个全局连接池
# 全局操作分为两类，一个是 select，一个是 execute（包括：save，update，remove)

# 定义字段类型 Field 并根据数据库类型分别定义一些细化的类型，如 int 等

# 定义 Model 类，是对所有数据模型的一个抽象，根据 Model 类创建数据类，如 User 等
# 该类定义了一些类方法，使继承该类的子类所产生的实例拥有一些操作方法对应 sql，不需要自己再拼写 sql

# 定义 元类 ModelMetalclass，在数据类创建时执行一系列操作，比如赋上一些通用的属性之类的。


import asyncio
import logging
import aiomysql


def log(sql, args=()):
    logging.info('SQL: %s' % sql)


async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )
    print('create_pool:', __pool)


async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close
        logging.info('rows returned: %s' % len(rs))
        return rs


async def execute(sql, args):
    log(sql)
    with (await __pool) as conn:
        try:
            cur = await conn.cursor()
            print('sql:', sql.replace('?', '%s'), '\nargs:', args)
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            await cur.close()
        except BaseException as e:
            raise
        return affected


def create_args_string(max):
    l = []
    for n in range(max):
        l.append('?')
    return ', '.join(l)


class Field(object):

    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (
            self.__class__.__name__, self.column_type, self.name)


class StringField(Field):

    def __init__(self, name=None, primary_key=False,
                 default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)


class IntegerField(Field):

    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


class TextField(Field):

    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        table_name = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, table_name))
        mappings = dict()
        fields = []
        primary_key = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info(' found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    if primary_key:
                        raise RuntimeError(
                            'Duplicate primary key for field: %s' % k)
                    primary_key = k
                else:
                    fields.append(k)
        if not primary_key:
            raise RuntimeError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings
        attrs['__table__'] = table_name
        attrs['__primary_key__'] = primary_key
        attrs['__fields__'] = fields
        attrs['__select__'] = (
            'select {primary_key}, {escaped_fields} from {table}'.format(
                primary_key=primary_key,
                escaped_fields=', '.join(escaped_fields),
                table=table_name))
        attrs['__insert__'] = (
            'INSERT INTO `{table}` ({escaped_fields}, `{primary_key}`) '
            'VALUES ({values_str})').format(
            table=table_name,
            primary_key=primary_key,
            escaped_fields=', '.join(escaped_fields),
            values_str=create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = (
            'update {table} set {key_values_str} where {primary_key}=?'.format(
                table=table_name,
                key_values_str=', '.join(map(lambda f: '{key}=?'.format(
                    key=repr(mappings.get(f).name or f)), fields)),
                primary_key=primary_key))
        attrs['__delete__'] = (
            'delete from {table} where {primary_key}=?'.format(
                table=table_name, primary_key=primary_key))
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(
                '"Model" object has no attribute {key}'.format(key=key))

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = (field.default() if callable(
                    field.default) else field.default)
                logging.debug(
                    'using default value for {key}: {value_str}'.format(
                        key=key, value_str=str(value)))
                setattr(self, key, value)
        return value

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        ''' find objects by where clause. '''
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        order_by = kw.get('order_by', None)
        if order_by:
            sql.append('order by')
            sql.append(order_by)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError(
                    'Invalid limit value: {limit}'.format(limit=limit))
        rs = await select(' '.join(sql), args)
        return [cls(**r) for r in rs]  # 把通过查询得回来的数据转成cls对象

    @classmethod
    async def findNumber(cls, select_field, where=None, args=None):
        ''' find number by select and where. '''
        # select count(x) num from y = select count(x) as num from y
        sql = ['select {select_field} _num_ from {table}'.format(
            select_field=select_field, table=cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    async def find(cls, pk):
        ''' find object by primary key. '''
        sql = [cls.__select__]
        sql.append('where {primary_key}=?'.format(
            primary_key=cls.__primary_key__))
        rs = await select(' '.join(sql), [pk], 1)
        if len(rs) == 0:
            return None
        return re[0]

    async def save(self):
        args = list(
            map(lambda x: self.getValueOrDefault(x), self.__fields__))
        # args = list()
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warn(
                'failed to insert recode: affected rows: {rows}'.format(
                    rows=rows))

    async def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn(
                'failed to update by primary key: '
                'affected rows: {rows}'.format(
                    rows=rows))

    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warn(
                'failed to remove by primary key: '
                'affected rows: {rows}'.format(
                    rows=rows))
