print('list range:', list(range(1, 11)))

print('list comprehension', [x * x for x in range(1, 11)])
print('list comprehension with if', [
      x * x for x in range(1, 11) if x % 2 == 0])
print('list comprehension double', [x + y for x in 'ABC' for y in 'xyz'])

l = ['Hello', 'World', 18, 'Apple', None]


def getLowerStrList(l):
    return [x.lower() for x in l if isinstance(x, str)]


print(getLowerStrList(l))
