# /usr/bin/env python
# coding:utf-8


def open_func(in_file):
    try:
        file_in = open(in_file,'r')
        content=file_in.read()
    except IOError:
        print("IOError--文件不存在")
    else:
        print(content)
    finally:
        print("everything is ok")


if __name__ == "__main__":

    open_func('zuoye3.py')



'''

file_in = open("/Users/a123/PycharmProjects/hemei/my_test/hanshu1.py","r")
content = file_in.read()
print(content)
'''
