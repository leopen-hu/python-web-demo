#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# encode and decode
str1 = '中文-English'
print(str1)
b = str1.encode('utf-8')
print(b)
print(b.decode('utf-8'))

# string print with variable
print('%d + %d = %d' % (1, 2, 3))
print('{0} + {1} = {2}'.format(1, 2, 3))
