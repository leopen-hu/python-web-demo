f = open('E:\\personal\\github\\python-web-demo\\base-demo\\io\\my-file.txt',
         'r', encoding='gbk', errors='ignore')

all_text = f.read()
print(all_text)

f.close()

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

with open('E:\\personal\\github\\python-web-demo\\base-demo\\io\\my-file.txt',
          'r', encoding='utf-8') as my_file_text:
    print('with', my_file_text.read())

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

with open('E:\\personal\\github\\python-web-demo\\base-demo\\io\\my-file.txt',
          'a', encoding='utf-8') as my_file_text2:
    my_file_text2.write('Hello,Python3!')

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

with open('E:\\personal\\github\\python-web-demo\\base-demo\\io\\my-file3.txt',
          'x', encoding='utf-8') as my_file_text3:
    my_file_text3.write('Hello,Python3!')

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
