# /usr/bin/env python
# coding:utf-8

'''
a = b = c = 1  一个值给多个变量
a,b,c = 1,2,"apple"   同时给多个变量赋值
'''
'''
my_str = "I love Python"
my_list = ["python","java","language","age"]
my_list2 = [24,12,2.3,9.7]
my_tuple = ("python",33,"java",8.8)
my_dict ={"name":"apple","age":88}
my_list1 = ['a','a',1,1,2,3]
my_set = {1,2,3}

a = 10
print(type(a))
a1 = str(a)    #强制转换从int到str
print(type(a1))
print(type(int(a1)))   #str转int
print(tuple(my_list))    #list与tuple元组转换
print(list(my_tuple))
print(set(my_list1))    #列表转set变量不重复
print(set(my_dict))    #字典类型转成set只有key值
print(list(my_dict.values()))   #字典转成列表，key，values可以单转
print(list(my_dict))
'''

my_tuple1 = ('one',1),('two',2),('three',3)
my_list_tuple = [('one',1),('two',2),('three',3)]

print(my_tuple1)
print(type(my_list_tuple))
print(dict(my_list_tuple))
