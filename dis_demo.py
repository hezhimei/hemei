# /usr/bin/env python
# coding:utf-8
#字典   是一种可变容器类型，也是可以存储任意类型的对象
d = {'apple': 11, 'pear': 32,'lemon': 23}
print(d)

#字典的操作，访问
keys = d.keys()
print(keys)
print(d['pear'])

#增加
d['peach'] = 15
print(d)

#更新
d['pear'] = 27
print(d)

#删除
del d['peach']
print(d)

#字典的函数操作
#清空字典
#d.clear()

#print(d)

#判断键是否在字典中
i = 'apple' in d
print(i)

print(d.values())