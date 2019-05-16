# /usr/bin/env python
# coding:utf-8
'''
json常用方法：
    json.dumps  将Python对象转化json字符串
    json.loads   将json字符串转化为Python对象

'''


import json

python_dic = {'name':'fengcheng','sex' : 'Male','c':3,'d':4,'e':5}
print(type(json.dumps(python_dic)))
print(json.dumps(python_dic))

json_str = '{"name":"fengcheng","sex":"Male","c":3,"d":4,"e":5}'
print(type(json.loads(json_str)))
print(json.loads(json_str))