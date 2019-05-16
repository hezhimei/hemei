# /usr/bin/env python
# coding:utf-8

'''
函数的返回值


def func_with_return():
    print("函数被调用")

p = func_with_return()
print(p)
print(type(p))

def func_with_return(p):
    return p
p = func_with_return(5)
print(p)
print(type(p))


#重载
#python 中没有重载的概念

#多个返回值
def func_with_return(name,age):
    return name,age
n,a = func_with_return("apple",5)
print(n,a)

s = func_with_return("apple",5)
print(s)
print(type(s))
'''
#返回一个函数
def func_with_return2(x):
    if x == 2:
        def inner_func(y):
            return y*y
    if x == 3:
        def inner_func(y):
            return y*y*y
    return inner_func
cal = func_with_return2(3)
print(cal(4))













