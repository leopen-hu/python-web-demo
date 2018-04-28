import functools

print('to 16', int('A2', base=16))


def int16(x, base=16):
    return int(x, base)


int16_2 = functools.partial(int, base=16)


print('to 16', int('A2', base=16))
print('to 16 int16', int16('A2'))
print('to 16 int16_2', int16_2('A2'))
