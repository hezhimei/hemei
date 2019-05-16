# /usr/bin/env python
# coding:utf-8
from collections import Counter

#将对象x转换为表达式字符串
'''
b = {"name":"apple","age":18}
str_b = repr(b)
print(str_b[0:3])

#用来计算在字符串中的有效Python表达式，并返回一个对象
a = "[1,2,3]"
list_a = eval(a)
print(list_a[0])

'''

#for year in range(1,100):
 #   print("我活了"+str(year)+"年")

str1 = 'abcdefgh'
for i in str1:
     print('_'+i,end='')      #end=''表示不换行

lists = ['apple','zip','banana','peach']
for item in lists:
    print("我今天吃了"+item)

print(list(reversed(lists)))
print(list(sorted(lists)))
#lists.sort()
#lists.reverse()
#print(lists)
'''
li = [x for x in range(10) if x % 2 == 0]
print(li)
'''
lists2 = lists*2
print(lists2)


#couter这个再学习一下
my_couter = Counter(lists2)
print(lists2.count("apple"))
print(my_couter)
print(my_couter.most_common())
