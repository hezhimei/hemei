# /usr/bin/env python
# coding:utf-8
'''
a = 255
print(hex(int(255)))
print(oct(255))
print(bin(255))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

if __name__=='__main__':
    print(my_abs('b'))
'''

a=[3,6,12,32,9,5]
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)

def find(L):

    for i in range(len(L)-1):
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
    a=L[0]
    b=L[-1]
    return L,a,b

if __name__=='__main__':
    c = find([3,6,12,32,9,5])
    print(c)


#列表生成器：写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

c=[x * x for x in range(1, 11)]
print(c)

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

d=[x * x for x in range(1, 11) if x % 2 == 0]
print(d)

#还可以使用两层循环，可以生成全排列：

e=[m + n for m in 'ABC' for n in 'XYZ']
print(e)

import os
f = [x for x in os.listdir('../my_test/')]
print(f)


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#generator生成器
g = (x*x for x in range(10))
print(g)
#调用generator
print(next(g))
#不断调用next函数，太变态，正确方法，用for循环：
for n in g:
    print(n)




