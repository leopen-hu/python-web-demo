# for
test_list = ['aaa', 'bbb', 'ccc']
for item in test_list:
    print(item)

sum = 0
sum_list = list(range(101))
for sum_item in sum_list:
    if sum_item < 5:
        print('skip', sum_item)
        continue
    elif sum_item > 50:
        print('break', sum_item)
        break
    sum = sum + sum_item
print('sum', sum)

# while
sum2 = 0
sum_max = 100
while sum_max > 0:
    if sum_max > 95:
        print('skip', sum_max)
        sum_max = sum_max - 1
        continue
    elif sum_max < 50:
        print('break', sum_max)
        sum_max = sum_max - 1
        break
    sum2 = sum2 + sum_max
    sum_max = sum_max - 1
print('sum2', sum2)
