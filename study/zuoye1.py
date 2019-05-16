# /usr/bin/env python
# coding:utf-8
'''
var_float = 2.918
var = int(var_float)
print(var)

num = bin(int('18',10))
print(num)

str = "Python is popular"
print (str.replace("Python","java"))
str1 = str.replace("Python","java")
str2 = str1.capitalize()
print(str1,str2)
'''
list = [1,2,3,4,5,6,7,8]
print (list[::2])
#list2 = list.remove(list1)
list2=[]
for i in list:
    if i % 2 == 0:
        list2.append(i)
    else:
        continue
print(list2)

dict = {"name":"", "sex":"","province":""}
print (type(dict))
dict["province"] = "江苏"
print(dict)

'''
test_str = "Python was  created in 1989,Python is  using in AI,big data,IOT."
print(test_str.lower())
print(test_str.split())
test_str_list = test_str.split()
print(test_str_list[2:6])


list1 = ["python",5,6,8]
list2 = ["python","5",6,8,10]
list3 = list1 + list2
print(list3)
set1 = set(list3)
print(set1)
print(list(set1))

from zuoye3 import sum_func

if __name__ == "__main__":
    sum_func([2,3,4,'a'])
'''