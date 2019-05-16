# /usr/bin/env python
# coding:utf-8

'''
查找/tomcat/log/ 目录下的log文件，如果文件最后修改时间是在1小时之前，
把次文件打包压缩，备份到/home/back/log 目录下
import os
import subprocess

print(os.stat("demo.txt")[9])
print(subprocess.check_output(['tar -cvf tomat.tar log'],shell=True))
'''
'''
import os

result =[]
def searchFile(path,name):

    for item in os.listdir(path):
        item_path = os.path.join(path,item)
        if os.path.isdir(item_path):
            searchFile(item_path,name)
        elif os.path.isfile(item_path):
            if name in item:
                global result
                result.append(item_path+';')
                print(item_path+';',end='')

searchFile('.','log')
'''
import os
import time

def search_file(path,match_postfix=None):
    match_file = []
    for root, dirs, file_names in os.walk(path):
        for file_name in file_names:
            if match_postfix:
                if file_name.endswith(match_postfix):
                    match_file.append(os.path.join(root,file_name))
    return match_file
print(search_file('.','.log'))
#for file_path in search_file('.','.log'):













