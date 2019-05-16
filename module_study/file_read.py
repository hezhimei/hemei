# /usr/bin/env python
# coding:utf-8

'''
一般用open方法
1.file_instance.read():  一次性读取文件全部内容
2.file_instance.readline():  执行一次这个函数读取一行
3.ile_instance.readlines():  一次性读取文件全部内容，并放到一个列表里面，每行是一个列表元素
4.file_instance.write():   写入内容到文件，不换行
5.file_instance.writelines():   把一个列表里面所有元素写入到文件，不换行
6.file_instance.flush():  即时把缓存中的数据输出到文件（不等句柄关闭）
7.对于读大文件的某一行或者你只需要读一行，用linecache模块
r=>读   w => 写  a => 追加（一般尽量用a，用w会把原有文件数据清空）
'''



import codecs
import time

def open_example(in_file):
    file_instance = open(in_file,'r')
    content = file_instance.read()

    #line1 = file_instance.readline()
    #lines1 = file_instance.readlines()
    print(content)
    file_instance.close()


def open_utf8(in_file):
    file_instance = codecs.open(in_file,encoding="utf-8")
    content = file_instance.read()
    file_instance.close()
    print(content)

def write_utf8(in_file):
    file_instance = codecs.open(in_file,encoding="utf-8",mode="a")
    file_instance.write("新的一行"+"\n")
    file_instance.writelines(["新的二行"+"\n","新的三行"+"\n"])

    file_instance.flush()
    print("I am sleeping")

    time.sleep(20)
    file_instance.close()


#open_example('../my_test/hanshu2.py')
open_example('/Users/a123/hello.py')
#open_utf8('../my_test/hanshu1.py')
#write_utf8('../my_test/hanshu1.py')

