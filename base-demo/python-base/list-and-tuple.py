# list
test_list = ['aaa', 'bbb', 'ccc']
print('init', test_list)
test_list.append('ddd')
print('append', test_list)
test_list.insert(2, '222')
print('insert', test_list)
test_list.pop()
print('pop', test_list)
print('len', len(test_list))
print('index -1', test_list[-1])

# tuple
single_tuple = ('aaa',)
print('single tuple', single_tuple)
test_tuple = ('aaa', 'bbb', ['ccc', 'ddd'])
print('init', test_tuple)
test_tuple[2][1] = 'dxd'
print('tuple\'s list_item change', test_tuple)
test_list2 = [1, 2]
test_tuple2 = (1, 2, test_list2)
print('init tuple2', test_tuple2)
test_list2[1] = 3
print('tuple2\'s list\'s item change', test_tuple2)
test_list2 = 3  # not change tuple
print('tuple2\'s list change', test_tuple2)
