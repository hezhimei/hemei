# /usr/bin/env python
# coding:utf-8

import time
'''
def open_file(in_file):
    with open(in_file,'r') as f1:
        #print(f1.read())
        for i in range(20):
            print(f1.readline())
            time.sleep(1)
        #print(f1.readlines())
'''
def open_write(in_file):
    with open(in_file,'a') as f2:
        #print(f2.write("第一行"+"\n"))
        print(f2.writelines(["第二行"+"\n","第三行"+"\n"]))

#open_file("./file_read.py")
open_write("./file_read.py")