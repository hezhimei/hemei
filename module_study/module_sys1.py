# /usr/bin/env python
# coding:utf-8
import sys

print("请输入你的名字：")
name = sys.stdin.readline()     #默认输入的格式是字符串
print('hello',name)

#例子：stdin 与input类似
#     stdout 与print类似
'''
try:
    while True:
        print("please input a number:")
        n = int(sys.stdin.readline().strip('\n'))
        #strip('\n')表示以\n 分隔
        print('please input some numbers:')
        sn = sys.stdin.readline().strip('\n')
        if sn == '':
            break
        sn = list(map(int,sn.split()))
        print(n)
        print(sn,'\n')
except:
    pass
'''
#例子

sys.stdout.write('hello'+'\n')
print('hello')
...
#从控制台重定向到文件
#f_handler =open('./test.log','a')
#sys.stdout = f_handler
#print("hello")
...

#同时重定向到控制台和文件

...
class __redirection__:

    def __init__(self):
        self.buff = ''
        self.__console__ = sys.stdout

    def write(self, output_stream):
        self.buff += output_stream

    def to_console(self):
        sys.stdout = self.__console__
        print(self.buff)

    def to_file(self, file_path):
        f = open(file_path, 'w')
        sys.stdout = f
        print(self.buff)
        f.close()


    def flush(self):
        self.buff = ''


    def reset(self):
        sys.stdout = self.__console__

if __name__=="__main__":
    c_handler =__redirection__()
    sys.stdout=c_handler
    c_handler.to_console()
    c_handler.flush()
    c_handler.reset()

...
import time

for i in range(5):
    print(i)
    sys.stdout.flush()
    time.sleep(1)







