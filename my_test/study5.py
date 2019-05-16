# /usr/bin/env python
# coding:utf-8

#对字典的访问和操作
#查：通过key来访问对应的value    dict.get('key')
#增：插入key
#改：更新已有key的value
#删：del
ages = {'apple':5,'coco':3,'lemon':26}
print(ages.get('apple',88))      #apple存在，则输出Apple对应值，否则，输出默认值88
ages['melody'] = 33          #新增
ages['lemon'] = 15            #更改lemon的值

del ages['melody']

#key in dict
D = {'username':'apple','age':5,'salary':1000000}
print("循环出来key，再通过key可能输入值")
for key in D:
    print(key,'=>',D[key])
print("只循环出值")
for value in D.values():
    print(value)

print("同时循环出key与value，断言返回key的值与...通常用在接口测试中json的响应断言")
for key,value in D.items():
    print(key,':',value)
    assert D[key] == value


#set
set1 = {1,2,3}
set2 = set1
set3 = set('hello')
print(set3)
set3.add(1)
print(set3)
print(set3, set1)
#set.clear()
de = set3.pop()
print(de)
set3.remove("l")
a = set3 & set1
print(a)
b = set1 | set3
print(b)