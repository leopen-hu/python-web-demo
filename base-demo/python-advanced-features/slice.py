list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(list1[:3])
print(tuple1[:3])

print(list1[1:2])
print(tuple1[1:2])

print(list1[-2:-1])
print(tuple1[-2:-1])

print(list1[-2:])
print(tuple1[-2:])

print(list1[:8:2])
print(tuple1[:8:2])


def trim(s):
    if s == '':
        return ''
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
