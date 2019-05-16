# /usr/bin/env python
# coding:utf-8

'''
commands/subprocess模块
commands模块常用方法：Commands一般用在linux
    commands.getoutput(command): 获取命令执行后的输出结果
    commands.getstatus(command):  获取命令执行后的返回的状态码
    commands.getstatusoutput(command)  返回一个元组，第一个元素是状态码，第二个元素是输出结果
subprocess模块常用方法：可用在Windows和Linux
    Subprocess.call(command,shell=True): 执行Windows下命令，返回执行状态和结果
    Subprocess.check_call(command,shell=True): 执行Windows下命令，返回执行状态和结果
    Subprocess.check_output(command,shell=True):  返回执行命令后的输出

python3没有commands模块
'''
import subprocess
import os

print(subprocess.call('ls -l',shell=True))
print(os.getcwd())
print(subprocess.check_output('ls -l',shell=True))
print(subprocess.call('ifconfig -a',shell=True))

print("*"*10)

print(subprocess.check_output(["ls"," -al"],shell=True))
print("*"*10)
print(subprocess.call(["ls"," -al"],shell=True))
subprocess.Popen('ls -l',shell=True)