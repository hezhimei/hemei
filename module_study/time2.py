# /usr/bin/env python
# coding:utf-8
'''
datetime用法：
datetime.now()   返回当前日期时间的datetime对象
datetime.utcnow()  返回当前日期时间的UTC datetime对象
datetime.combine()  将一个date对象和一个time对象合并生成一个datetime对象
datetime.utctimetuple()  返回UTC时间元组
datetime.strptime()  根据string，format2个参数，返回一个对应的datetime对象
'''
from datetime import datetime
from datetime import timedelta
print(datetime.now())
a = datetime.now()
print(a.date())     #返回日期部分
print(a.time())     #返回时间部分
print(a.utctimetuple())
b = datetime.combine(a.date(),a.time())
print(b)

'''
timedelta类用来计算2个datetime对象的差值
包含属性：
    1，days 天数
    2，microseconds 微秒数
    3，seconds  秒数
'''

