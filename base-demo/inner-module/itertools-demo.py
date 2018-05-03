import itertools

print('count--------------------------------')
natuals = itertools.count(1)
for n in natuals:
    if n > 15:
        break
    print(n)

print('cycle--------------------------------')
cycles = itertools.cycle('ACB')
counter = 0
for n in cycles:
    counter = counter + 1
    if counter > 15:
        break
    print(n)

print('chain---------------------------------')
for x in itertools.chain('ACB', '894441'):
    print(x)

print('groupby-------------------------------')
# groupby 相邻的重复元素才会组成 group
for key, group in itertools.groupby('AaaBBbcCAAa', lambda x: x.upper()):
    print(key, list(group))

print('PI------------------------------------')


def pi(N):
    count = itertools.count(1, 2)
    list_n = list(itertools.takewhile(lambda x: x < 2 * N, count))

    def calc(x, i):
        return 4 / x * (1 if i % 2 == 0 else -1)

    list_x = [calc(list_n[i], i) for i in range(N)]
    return sum(list_x)


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
print(pi(100000))
