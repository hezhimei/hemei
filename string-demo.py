# /usr/bin/env python
# coding:utf-8
'''
s1 = "hello string"
s2 = "  python"
print (s1[0:6] + s2)
print (s1 + s2)
'''


# 包含运算
'''
s1 = "hello"
s2 = "he"
print (s2 in s1)
print(s2 not in s1)
'''

#转义字符
#print ("\'")

#换行符
#print ("\n")

#制表符tab
print("hello\tpython")

#回车符  光标到行首，打印\r之后的内容
#print("hellp\rPython")

#原始字符串
#print(r"hello\npython")
#print(R"hello\npython")

#字符串的格式化输出
#print ("我叫%s,今天是我第%d天学python" %('小明' , 10))

#字符串的内建函数
#查找字符串
#s = "hello python".find("l")
#print(s)

#转换为小写字母

print("Hello Python".lower())

#转换为大写字母
print("hello world".upper())

#返回字符串长度_len_()  这个函数返回的是自然长度
print("hello world".__len__())

#判断字符串是否只包含空格
print("a ".isspace())

#字符串替换
print ("Hello World".replace("o","ee"))

#文档Python自带的学习文档
#python3 -m pydoc -p 8888    本地localhost:8888