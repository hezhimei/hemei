# /usr/bin/env python
# coding:utf-8
'''
Os模块常用方法：
os.listdir():  返回指定目录下的所有文件和目录名，不包括子目录
os.getcwd():   返回当前Python进程正在工作的目录
os.removedirs("/home/test/"): 删除多个目录
os.system():  运行shell 命令
os.path.join(path,name):  连接目录与文件名或目录
os.mkdir(name):   创建目录
os.path.basename(path):   返回文件名
os.stat(file)： 获得文件属性，文件大小，创建时间，最后访问时间等
os.path.isfile():  判断是否是文件
os.path.exists():  判断目录或文件是否存在
os.path.split():  将路径分解为（文件夹,文件名）
os.path.dirname()  返回路径
'''

import os

print(os.walk('.'))

#os.mkdir('/Users/a123/aaa')
#os.removedirs("/Users/a123/aaa")
#os.removedirs("/Users/a123/sss")
'''
print(os.getcwd())
print(os.path.abspath('.'))    #返回path的绝对路径
print(os.listdir('.'))
os.system('ls -l')
#os.path.join(./ ,module_os.py)
print(os.path.split('./module_study/file1.py'))
print(os.path.dirname('./module_study/file1.py'))
print(os.path.basename('./module_study/file1.py'))

print(os.stat('../lianxi_jichu.py'))
print(os.path.getmtime('../lianxi_jichu.py'))
print(os.path.getatime('../lianxi_jichu.py'))
print(os.path.getctime('../lianxi_jichu.py'))
os.path.getsize('../lianxi_jichu.py')
'''

#举例：查找文件夹下最新的文件
'''
def new_file(test_dir):
    lists = os.listdir(test_dir)
    lists1=[]
    for i in range(len(lists)):
        listi = os.path.getmtime(lists[i])
        lists1.append(listi)
    #print(type(lists1))
    lists1.sort()
    print(lists1[-1])
    for j in range(len(lists)):
        if os.path.getmtime(lists[j]) == lists1[-1]:
            print(os.path.join(test_dir+'/'+lists[j]))
        else:
            continue

new_file('/Users/a123/PycharmProjects/hemei/module_study/')
'''