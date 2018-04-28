def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


print('calc_sum', calc_sum(1, 2, 3, 4, 5))
print('lazy_sum', lazy_sum(1, 2, 3, 4, 5))
print('lazy_sum_calculated', lazy_sum(1, 2, 3, 4, 5)())

# point：返回函数不要引用任何循环变量或者后续会发生变化的变量


def createCounter():
    L = [0]    # 列表L的内存地址在初次调用时已经给定，且L[0]即第一个元素指向整数0

    def counter():
        L[0] += 1    # 改变列表L中第一个元素的值，但并没有改变列表L的内存地址
        return L[0]
    return counter


counterX = createCounter()
counterY = createCounter()
print(counterX(), counterX(), counterX())
print(counterY(), counterY(), counterY())
