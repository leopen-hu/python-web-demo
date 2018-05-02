# namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

# deque
from collections import deque  # nopep8

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
from collections import defaultdict  # nopep8
dd = defaultdict(lambda: 'notexist')
dd['x'] = 'abc'
print('dd[\'x\']', dd['x'], 'dd[\'x\']', dd['y'])

# orderedDict
from collections import OrderedDict  # nopep8
d2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d2, list(d2.keys()))

# Counter
from collections import Counter  # nopep8
c = Counter()
for ch in 'sdfjsjfjffjewl':
    c[ch] = c[ch] + 1

print(c)
