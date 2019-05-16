# /usr/bin/env python
# coding:utf-8
'''
random常用方法：
    random.uniform(1,20)  随机获取1到20之间的浮点数
    random.randint(1,20)  随机获取到1到20之间的一个整数
    random.choice(seq)  随机获取seq的一个元素
    random.sample(seq,k)  随机获取seq中的k个元素
    random.shuffle(list)  打乱list里面的元素顺序

'''
import random

print(random.randint(1,10))    #产生1到10的一个整数型随机数
print(random.random())          #产生0到1之间的随机浮点数
print(random.uniform(1.1,5.4))   #产生1.1到5.4之间的随机浮点数
print(random.choice('tomorrow'))  #从序列中随机选取一个元素
print(random.randrange(1,100,2))  #生成从1到100的间隔为2的随机数
list = [1,2,3,4,5]
random.shuffle(list)
print(list)
print(random.sample('tomorrow',3))