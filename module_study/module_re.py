# /usr/bin/env python
# coding:utf-8
'''
re模块：
灵活性，逻辑性，功能性非常强大
以极简的方式控制复制的字符串
可读性差，对初学者晦涩难懂
re模块常用方法：
    re.compile(pattern[,flags])  把正则表达式语法转化成正则表达式对象
    re.search(pattern,string[,flags])  在整个字符串中查找匹配正则表达式模块的位置，返回matchobject
        的实例，如果没有找到匹配的位置，则返回none
    re.match(pattern,string[,flags])  在字符串的开始位置测试匹配正则表达式
    re.findall()  显示出字符串中模式的所有匹配项

'''
import re

p = re.compile(r'\d+')
print(p.findall('one1two2three3four4'))
