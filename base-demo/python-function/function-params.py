# 必选参数
def my_func(x, y):
    return x / y


print(my_func(2, 1))


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s


print(power(2), power(2, 3))


# 可变参数
def calc_numbers(*args):
    sum = 0
    for n in args:
        sum = sum + n * n
    return sum


print('calc 1, 2:', calc_numbers(1, 2))
print('calc no params', calc_numbers())
list1 = [1, 2]
tuple1 = (1, 2)
print('calc [1, 2]:', calc_numbers(*list1))
print('calc (1, 2):', calc_numbers(*tuple1))


# 关键字参数
def person(name, age, **kw):
    _person = {
        'name': name,
        'age': age,
        'other': kw
    }
    return _person


print(person('Leopen', 26))
print(person('Leopen2', 26, sex='male'))
other_info = {'sex': 'male', 'city': 'Shanghai'}
print(person('Leopen2', 26, **other_info))


# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Leopen', 26, city='Shanghai', job='coder')
extra_info = {
    'city': 'Shanghai',
    'job': 'coder'
}
person('Leopen', 26, **extra_info)


def fx(a, *args, **kw):
    print('a:', a, '*args:', *args, 'kw:', kw)


fx(5, 6, 7, x=7)
