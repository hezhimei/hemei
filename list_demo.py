# /usr/bin/env python
# coding:utf-8

#列表：一组数据
#List是有序的序列
#序列中的每个元素分配一个数字，就是索引，也是位置角标，坐标
'''
list1 = ["hello", 18,"百度","京东" ]
print(list1)
print(type(list1))

#访问列表
print(list1[0])
print(list1[2:])  #访问从下标2以后的
print(list1[1:3])  #1-3,左闭右开

#更新
list1[1] = 14
print(list1)

#添加操作
list1.append('apple')
list1.append(16)
print(list1)
list1 = list1 +['coco', 3]
print(list1)

#删除操作delete
del list1[3]
print(list1)

'''

#嵌套列表
#list1 =[['apple','banana','orange'],[2,4,5]]
#print(list1)
#print(list1[0][0])

#返回列表元素的个数
#count = len(list1)
#print(count)

#移除列表中的元素,并且返回这个值a = float(input("数字1："))


#l = list1.pop(1)
# print (l)
#print(list1)

#对列表中的元素进行排序
list1 = [12,11,13]
list1.sort()
print(list1)

#查找列表中第一个匹配的元素的索引值
#list1 = [12,11,13]
#i = list1.index(11)
#print(i)
'''
station = input("请输入车站名称：")
bus_list = ['建国','爱国']
if station == '天安门东':
    bus_list.append('国庆')
    bus_list.remove('建国')
elif station == '国贸':
    bus_list.append('卫国')
    bus_list.remove('爱国')
elif station == '四惠':
    bus_list.append("建军")
print(bus_list)
'''

list = [3,4,5,6,7,2,9]
del list[2:6]
print(list)

















