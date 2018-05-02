from io import StringIO, BytesIO

str_io = StringIO()
str_io.write('1: Hello, Python3!\n')
str_io.write('2: Hello, Python3!\n')
str_io.write('3: Hello, Python3!')
str_io_value = str_io.getvalue()
print('str_io_value', str_io_value)

str_io_2 = StringIO('1: xxx\n2: 3333\n3: ddff')
while True:
    str_io_2_line = str_io_2.readline()
    if str_io_2_line == '':
        break
    print(str_io_2_line.strip())

byte_io = BytesIO('chinese中文'.encode('utf-8'))
print(byte_io.read())
