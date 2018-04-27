from functools import reduce


def double_x(x):
    return 2 * x


source_list = [1, 2, 3, 4, 5]
target_iterator = map(double_x, source_list)
target_list = list(target_iterator)
print(target_list)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, }


def str2num(s):
    def fn(x, y):
        return 10 * x + y

    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


def str2num2(s):
    def char2num(s):
        return DIGITS[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


my_str = '123456'
print('str2num', type(my_str), my_str, type(str2num(my_str)), str2num(my_str))
print('str2num2', type(my_str), my_str, type(
    str2num2(my_str)), str2num2(my_str))


def normalizeName(name):
    if name is None or name == '':
        return ''
    return name[0].upper() + name[1:].lower()


def normalizeNames(names):
    return map(normalizeName, names)


print(list(normalizeNames(['dfhAdd', 'aaaa', 'AAAA', 'Adfdf', ''])))


def prod(numbers):
    return reduce(lambda x, y: x * y, numbers)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    return reduce(
        lambda x, y: x + y * pow(10, -len(str(y))),
        map(int, s.split('.'))
    )


print(str2float('12.21'))
