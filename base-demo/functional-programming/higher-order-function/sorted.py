my_list = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return str(t[0])


sorted_list1 = sorted(my_list, key=by_name)
print('by_name', sorted_list1)


def by_score(t):
    return t[1]


sorted_list2 = sorted(my_list, key=by_score, reverse=True)
print('by_score', sorted_list2)
