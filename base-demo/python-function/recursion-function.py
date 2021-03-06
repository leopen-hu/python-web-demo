def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(100))


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact2(100))


# 汉诺塔算法
# n == 1: a -> c
# n > 1: n(a -> c) = (n-1)( a->b ) + a->c + ( n-1 )( b->c )
# 先把前n-1移到中间柱（a到b），把第n个移动到目标柱(a到c)，再把中间柱的n-1个移动到目标柱(b到c)
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)


move(10, 'A', 'B', 'C')
