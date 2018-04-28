import functools
import time
# import datetime


def func1():
    return 'func1-----'


my_func = func1
print(func1.__name__)
print(my_func.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def func2():
    return 'func2------'


print(func2(), func2.__name__)


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log2('execute')
def func3():
    return 'func3-----------'


print(func3(), func3.__name__)


def log4(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log4
def func4():
    return 'func4----'


print(func4(), func4.__name__)


def log5(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log5('run')
def func5():
    return 'func5----'


print(func5(), func5.__name__)


def time_spend(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        result = fn(*args, **kw)
        end_time = time.time()
        print('%s executed in %s ms' %
              (fn.__name__, int((end_time - start_time) * 1000)))
        return result
    return wrapper


@time_spend
def func6():
    time.sleep(0.012)
    return 'func6-----'


print(func6(), func6.__name__)
