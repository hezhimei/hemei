# /usr/bin/env python
# coding:utf-8
'''
条件控制
1、比较运算符 == > < >= <= !=

'''
i = "a"
j = "B"
if i < j:
    print("a小")
else:
    print("a大")

#ASCII码表
print(ord(i))
print(ord(j))

#成员运算符  in  not in
my_string = "abcdefg"
if 'a' in my_string:
    if 'b' in my_string:
        print("a和b都在my_string中")


#逻辑运算符
#and or not
house_person = ['apple','pear','lemon','peach']
if 'apple' in house_person and 'pear' in house_person\
    and 'lemon' in house_person and 'peach' in house_person:
    print("他们在打麻将")
else:
    print("他们在玩游戏")
if 'apple' not in house_person:
    print("apple没有打麻将")
else:
    print("apple在打麻将")

#关于True和False的讨论
print(True and False)
print(True or False)
print(not True)
print(2 and 0)
print(2 or 0)
print(not 2)

'''
1代表了True  0代表了False
and 需要判断到最后一个，只有全部为真的时候，才会返回真
or的判断逻辑，只要碰到真值，就直接返回真，后边的就不再判断
'''
#例如：
print(3 and 4 and 5)
print(3 or 4 or 5)


#身份运算符
#is
#is not
i = 1
j = 1
print(i == j)
print(i is j)
print(id(i))
print(id(j))

j = j + 1
print(id(j))
list_1 = [1,2,3]
list_2 = [1,2,3]
print(list_1 is list_2)
print(list_1 == list_2)
print(id(list_1))
print(id(list_2))

'''
运算符的优先级
扩展
'''
