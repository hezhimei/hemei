# /usr/bin/env python
# coding:utf-8

#Map函数
#map(fun,seq)  返回一个序列，fun是一个函数，seq是个元组或列表
#注意，python3中map的用法与Python2不同：
#   python3中直接用map（sqr,a) => <map object at 0x10475cc18>
#   如果要输出list或者tuple，需要在map前加上list或者tuple

def sqr(x):
    return x**2
def sqr1(h,j):
    return h**2,j**2

a = (4,5,6)
e = (5,8,12)
b = tuple(map(sqr1,a,e))
print(b)
c = list(map(sqr,a))
print(c)

