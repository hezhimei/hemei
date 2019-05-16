# /usr/bin/env python
# coding:utf-8
'''
shutil模块
    shutil.copv(src,dst) 复制文件，dst可以是目录，也可以是被复制后带文件名的全路径，比如：
        dst可以是/home/testerhome/,也可以是home/testerhome/newfile.txt
    shutil.copytree(src,dst)  复制目录包括子目录到目标目录
    shutil.rmtree(path)  删除目录包括子目录
    shutil.move(src,dst)  移动源目录包括子目录的文件到目标目录
    shutil.make_archive(base_name,format)  打包压缩文件

'''
from shutil import make_archive
import os

def targz_dir():
    archive_name = 'mvimage'
    root_dir = '../image'
    make_archive(archive_name,'gztar',root_dir)

if __name__ == '__main__':
    targz_dir()