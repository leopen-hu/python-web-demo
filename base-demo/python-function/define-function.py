import math


def my_test_func():
    return 'my first defined function'


result = my_test_func()
print(result)


def pass_func(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError(r'"a" is a bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError(r'"b" is a bad operand type')
    print(a, b)


pass_func(1, 3)
# pass_func(1, '3')


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y-step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
