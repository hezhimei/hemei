# /usr/bin/env python
# coding:utf-8

'''
集合：是一个无序的不重复元素的序列
两种方法申明
使用{}
set()

'''
#申明一个集合
#set_param = {"apple","banana","lemon","pear","apple"}
#print(set_param)

#判断元素是否在集合内
#print("apple" in set_param)
#print("orange" in set_param)

#两个集合间的运算
#a = set('abcdef')
#b = set('abcxyz')
#print(a)
#print(b)
#print(a & b)
#print(a | b)
#print(a ^ b)

#集合添加元素
my_set = {"apple", "banana", "pear"}
my_set.add("lemon")
print(my_set)

#移除指定元素
my_set.remove("lemon")
print(my_set)

#随机移除一个元素
pop_param = my_set.pop()
print(pop_param)
print(my_set)

#计算集合的个数
print(len(my_set))

#清空集合
my_set.clear()
print(my_set)