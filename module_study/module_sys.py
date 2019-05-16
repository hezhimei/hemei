# /usr/bin/env python
# coding:utf-8

'''
sys模块常用方法：
   sys.path   返回当前Pythonpath的列表
   sys.argv   获取命令行参数
   sys.exit   退出当前Python进程
   sys.platform    获取当前系统平台
   sys.stdin    标准输入流
   sys.stdout   标准输出流
   sys.stderr   标准错误流

'''
import sys

print(sys.path)
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())

sys.argv
print(sys.argv[0])   #打印代码本身文件路径
print(sys.argv[2:])  #从外部往程序穿参数，打印下标2之后的参数

print(sys.modules)
print(sys.modules.keys())
print(sys.modules.values())
print(sys.modules["os"])

