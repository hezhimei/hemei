# /usr/bin/env python
# coding:utf-8

#静态方法，类方法
'''
静态方法：@staticmethod
类方法：@classmethod
静态方法，类方法可以被类或者类的实例对象调用
实例方法只能被实例对象调用
静态方法：参数没有要求
类方法：第一个参数必须要默认传类，一般用cls
实例方法：第一个参数必须要默认传实例对象，一般习惯用self

'''

#变量名如果以_开头，就变成了一个私有变量（private)
#这样的变量可以被外部所访问，但是不要随意访问
#变量名类似__xxx__的，系统自定义名字，不建议占用
