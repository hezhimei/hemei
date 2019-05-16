# /usr/bin/env python
# coding:utf-8

str = 'python 蟒蛇'
print(dir(str))        #打印str有哪些方法

print(str.count("l"))
print(str.find("o"))    #打印o字母索引位置
print(str.capitalize())   #首字母大写
print(str.encode("gb2312"))
print(str.find("n"))
print(str*2)     #输出字符串两次
print(str + "test")    #连接字符串
print(len(str))
print(str.startswith("python"))    #判断是否是Python开头
b = "20"
print(b.isdecimal())      #判断是不是数字
print(str.upper())
print(str.lower())

print(str.replace('python','java'.upper()))
print(str*4)


s1 = '_'
s2 = ''
seq = ('a','p','p','l','e')
print(type(seq))
print(s1.join(seq))
print(s2.join(seq))

str4 = "编号 标题 测试数据 测试结果"
(no,title,test_data,test_result) = str4.split(" ")
str5 = str4.split(" ")
print(type(str5))
print(test_data)

#格式输出
print('hi,%s,you have $%d.' %('apple',1000000))

print(('hello,{0},成绩提升了 {1:.1f}%'.format('apple',17.125)))
print("{} {}".format("hello","world"))      #不设置指定位置，按默认位置

from functools import reduce
def plus(x,y):
    return x * y

if __name__=='__main__':
    print(reduce(plus, [1, 3, 5, 7, 9]))

def normalize(name):
    return name.lower().capitalize()
print(list(map(normalize,['adam','LISA','barT'])))



