# 多行输出
print('''123
123
234''')

# r'' 不转义
print('''转义：\\123
234''')
print(r'''不转义：\\123
234''')

# exercise
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print('''%s
%s
%s
%s
%s
%s''' % (n, f, s1, s2, s3, s4))
