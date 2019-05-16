# /usr/bin/env python
# coding:utf-8

'''
time模块常用方法：
    time.time()   获取1970.1.1.0：0：0到当前的时间
    time.localtime()   获取本地时间
    time.gmtime()   获取格里尼治时间
    time.strftime()   格式化时间格式
    time.strptime()   字符串时间格式转化为时间
    time.mktime()   将时间元组转换为1970/1/1 0:0:0到目前的时间值
    datetime.timedelta  计算两个datetime对象的时间差
通常有三种方式来表示时间：时间戳，元组（结构化时间，struct_time）,格式化的时间字符串。
'''

import time
from datetime import datetime

def time_format():
    print(time.time())
    print(time.localtime())
    print(time.gmtime())
    print(time.strftime("%y/%m/%d %H:%M"))
    print(time.strftime("%y-%m-%d %H:%M:%S %Z"))
    print(time.strftime("%c"))
    time_tuple = time.strptime("1 Jan 2018 1:30pm","%d %b %Y %I:%M%p")
    print(type(time_tuple),time_tuple)
    print("分割线","**"*20,"分割线")

def datetime_format():
    print(datetime.now())
    print(datetime.utcnow())
    print(datetime.now().strftime("%y/%m/%d %H:%M"))
    date_format=datetime.now().strptime("1 Jan 2018 1:30pm","%d %b %Y %I:%M%p")
    print(type(date_format),date_format)

def time_delta():
    from datetime import datetime
    from datetime import timedelta
    d1=datetime.strptime('2017-12-05 17:41:20','%Y-%m-%d %H:%M:%S')
    d2=datetime.strptime('2017-12-03 19:40:28','%Y-%m-%d %H:%M:%S')
    delta = d2 -d1
    print(delta)

#后三天
    now = datetime.now()
    days_delta = timedelta(days=3)
    print(now+days_delta)

    hours_delta = timedelta(hours=0.5)
    print(now+hours_delta)

    mins_delta = timedelta(minutes=10)
    print(now+hours_delta)

if __name__=="__main__":
    time_format()
    datetime_format()
    time_delta()