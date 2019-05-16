# /usr/bin/env python
# coding:utf-8
'''
递归
在函数中，自己调用自己
重点：要明确递归结束的条件
优点：写法简洁
缺点：效率低
要求：每次递归的时候，规模都要有所缩小
现象：每两次相邻的调用，前一次要为后一次做准备，第一次运算的结果，是下一次运算的条件
'''
'''
def my_func(x):
    print(x)
    my_func(x+1)

my_func(1)

'''
'''
阶乘计算：5的阶乘 5*4*3*2*1
'''
'''
def f(x):
    if x == 1:
        return 1
    return x * f(x-1)
'''
'''
作业：递归查找
有一个不规则的 list = [4,6,7,9,11,2,90,44]
定义一个函数
功能要求：
接受一个list和一个数字
返回数字在列表中排序后的位置，如果出错或者没有就返回-1
'''
#list = [4,6,7,9,11,2,90,44]
#list.sort()
#def func_search(x):

def func1(list1 = eval(input()),x=int(input())):
    list1.sort()
    if len(list1)//2 == 1:
        if x < list1[(len(list1)+1)/2]:
            del list1[list1[(len(list1)+1)/2]:list1[len(list1)]]
            func1(list1,x)













