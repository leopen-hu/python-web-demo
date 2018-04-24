from collections import Iterable

print('string iterable?', isinstance('abc', Iterable))
print('list iterable?', isinstance([1, 2, 3], Iterable))
print('int iterable?', isinstance(123, Iterable))

for i, value in enumerate(['1', 'b', '-']):
    print('enumerate', i, value)


def findMinAndMax(source_list):
    if len(source_list) == 0:
        return (None, None)
    max = source_list[0]
    min = source_list[0]
    for x in source_list:
        if x > max:
            max = x
        if x < min:
            min = x
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
