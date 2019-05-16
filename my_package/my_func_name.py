# /usr/bin/env python
# coding:utf-8

'''
__name__
在本模块启动时，__name__变量等于__main__
1、可以作为这个模块的入口，在其他语言中，叫做main函数
2、也可以作为调试使用，原因：在其他模块调用本模块时，__name__==__main__
'''
def my_print():
    print(__name__)
if __name__ == "__main__":
    my_print()
    print(1)
    print(__name__)