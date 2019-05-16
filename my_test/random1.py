# /usr/bin/env python
# coding:utf-8

#关于random

import random

print(random.randint(1,10))    #产生1到10的一个整数型随机数
print(random.random())          #产生0到1之间的随机浮点数
print(random.uniform(1.1,5.4))   #产生1.1到5.4之间的随机浮点数
print(random.choice('tomorrow'))  #从序列中随机选取一个元素
print(random.randrange(1,100,2))  #生成从1到100的间隔为2的随机数