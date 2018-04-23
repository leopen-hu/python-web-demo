# dict
dict1 = {'aaa': 'aaa', 'bbb': 'bbb', 'ccc': 'ccc'}
print('init dict', dict1)
print('dict1 aaa:', dict1['aaa'])
dict1['ddd'] = 'ddd'
print('dict1 set ddd', dict1)
dict1['ddd'] = 'dxd'
print('dict1 set ddd', dict1)


if 'ddd' in dict1:
    print(r'key "ddd" in dict1')
ddd_value = dict1.get('ddd')


if ddd_value is not None:
    print('dict1 get ddd:', ddd_value)

dict1.pop('ddd')
print(r'key "ddd" poped:', dict1)

# set
set1 = set(['aaa', 'bbb', 'ccc'])
print('init set', set1)
set1.add('xxx')
print('set1 add:', set1)
set1.remove('xxx')
print('set1 remove:', set1)
