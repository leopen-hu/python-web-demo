from collections import Iterable
from collections import Iterator

list1 = [1, 2, 3]
dict1 = {'a': 1, 'b': 2, 'c': 3}
tuple1 = (1, 2, 3)
g = (x for x in range(10))

print('list Iterable?', isinstance(list1, Iterable))
print('dict Iterable?', isinstance(dict1, Iterable))
print('tuple Iterable?', isinstance(tuple1, Iterable))
print('generator Iterable?', isinstance(g, Iterable))
print('list Iterator?', isinstance(list1, Iterator))
print('dict Iterator?', isinstance(dict1, Iterator))
print('tuple Iterator?', isinstance(tuple1, Iterator))
print('generator Iterator?', isinstance(g, Iterator))
