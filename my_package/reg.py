# /usr/bin/env python
# coding:utf-8
'''
正则表达式：记录文本规则的代码，是一个特殊的字符序列
由普通字符和元字符组成
主要是对元字符的学习
'''

import re

#reg_string = "hello39yrhdffjdkhellodhhldf"
#reg = "hello"

#result = re.findall(reg,reg_string)
#print(result)

'''
元字符
.匹配除换行符以外的任意字符
\w 匹配字母或数字或下划线或汉字
\s 匹配任意的空白符
\d 匹配数字
\b 匹配单词的开始或结束
^ 匹配字符串的开始
$ 匹配字符串的结束

'''

#reg_string = "hello397hefshfdlhoehellojjfjfjf"
#reg = "\d"
#s = re.findall(reg, reg_string)
#print(s)

#reg = "^hello"
#s = re.findall(reg, reg_string)
#print(s)


'''
反义代码
\W 匹配任意不是字母、数字、下划线、汉字的字符
\S 匹配任意不是空白符的字符
\D 非数字
\B 匹配不是单词开头或结束的位置
[^a] 匹配除了a以外的任意字符
[^abcd]
'''

'''
限定符
* 重复零次或多次
+ 重复一次或多次
？ 重复零次或一次
{n } 重复n次
{n,} 重复n次或更多次数
{n,m} 重复n到m次

'''

#reg_string = "hello39117hefshfdlhoehellojjfjfjf"
#reg = "\d{4}"
#result = re.findall(reg,reg_string)
#print(result)

#reg = "[0-9a-z]{4}"
#result = re.findall(reg,reg_string)
#print(result)

#匹配IP
#ip = "this is ip : 192.168.1.123:192.168.3.45"
#reg = "\d+.\d+.\d+.\d+"
#result = re.findall(reg,ip)
#print(result)

#search
#ip = "this is ip : 192.168.1.123:192.168.3.45"
#reg = "(\d{1,3}.){3}\d{1,3}"
#result = re.search(reg,ip)[0]
#print(result)

'''
search 和 findall
search 只匹配第一个
findall 匹配所有

'''

'''
组匹配

'''
#s = "this is phone:13888888888 and this is my postcode:012345"
#reg = "this is phone:(\d{11}) and this is my postcode:(\d{6})"
#result = re.search(reg, s)
#print(result)

#result = re.search(reg, s).group(0)
#print(result)
#result = re.search(reg, s).group(1)
#print(result)
#result = re.search(reg, s).group(2)
#print(result)

#reg_string = 'hellopythonhelloworldhellostring'
#reg = 'Hello'
#result = re.match(reg,reg_string,re.I).group()
#print(result)

#re.I 忽略大小写
#match 只匹配开头的

#贪婪与非贪婪
#贪婪：尽可能多的匹配，默认贪婪匹配
#非贪婪：尽可能少的匹配
#非贪婪操作符：？，用在* + ？后边的，要求正则匹配的越少越好
#* 重复零次或多次
#+ 重复一次或多次
#？ 重复零次或一次

#reg_string = "pythonnnnnnnnnnpythonhelloPytho"

#贪婪
#reg = "python*"
#result = re.findall(reg,reg_string)
#print(result)

#非贪婪
'''
reg = "python*?"
result = re.findall(reg,reg_string)
print(result)

reg = "python+?"
result = re.findall(reg,reg_string)
print(result)

reg = "python??"
result = re.findall(reg,reg_string)
print(result)

'''
#练习 手机号码验证
'''
移动：139，138，137，136，135，134，150，151，152，157，158，159，182，183，187，188
联通：130，131，132，185，186，145，147
电信：133，153，180，189

'''
def checkCellphone(cellphone):
    regex = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$"
    result = re.findall(regex,cellphone)
    if result:
        print("匹配成功")
        return True
    else:
        print("匹配失败")
        return False

cellphone = "13739393939"
print(checkCellphone(cellphone))


'''
验证邮箱的合法性：
新浪、网易、搜狐、qq
jdgoeg@sina.com
hdgoewg@sina.com.cn
jgoewg@163.com
hfiegh@126.com
heigow@qq.com
djslafj@sohu.com
'''

def checkEmail(email):
    regem = "(^[a-zA-Z0-9|_][a-zA-Z0-9|_]* + @(\w+.) + (com|cn|net)$)"
    result = re.findall(regem,email)
    if result:
        print("邮箱合法")
        return True
    else:
        print("邮箱不合法")
        return False


email = "15394230620呵_@163.com.cn"
print(checkEmail(email))