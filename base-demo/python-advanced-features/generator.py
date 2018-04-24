g = (x for x in range(1, 11))
print('generator:', g)
print('generator item 0:', next(g))

for x in g:
    print('generator iteration:', x)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print('fib', b)
        a, b = b, a+b
        n = n+1
    return 'done'


fib(6)


def g_fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done'


print('g_fib', g_fib(6))


def triangles():
    line_list = [1]
    yield line_list
    line_list = [1, 1]
    yield line_list
    i = 3
    while i > 2:
        new_list = [line_list[i-1] + line_list[i]
                    for i in range(1, i - 1)]
        new_list.insert(0, 1)
        new_list.append(1)
        line_list = new_list
        i = i + 1
        yield new_list


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
