input = input('Please input your age:\n')
age = int(input)
if age > 18:
    print('adult\'s age is %s' % age)
elif age > 12:
    print('teenager\'s age is %s' % age)
else:
    print('child\'s age is %s' % age)
