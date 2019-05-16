# /usr/bin/env python
# coding:utf-8

import time
import datetime

print(time.asctime())
print(time.ctime())
print(time.time())
print(time.localtime())
print(time.mktime(time.localtime()))
print(time.struct_time(time.localtime()))
print(time.strftime("%Y-%m-%d",time.localtime()))
'''
strftime:把一个代表时间的元组或者struct_time(如由time.localtime()和time.gmtime()返回)转化为格式化的时间字符串．如果t未指定，
将传入time.localtime()，如果元组中任命一个元素越界，将会抛出ValueError异常
    %Y  ===>完整的年份
    %m  ===>月份(01-12)
    %d  ===>一个月中的第几天(01-31)
    %H  ===>一天中的第几个小时(24小时制，00-23)
    %M  ===>分钟数(00-59)
    %S  ===>秒(01-61)
    %z  ===>用+HHMM或者-HHMM表示距离格林威治的时区偏移(H代表十进制的小时数，M代表十进制的分钟数)
    %a  ===>本地(local)简化星期名称
    %A  ===>本地完整星期名称
    %b  ===>本地简化月份名称
    %B  ===>本地完整月份名称
    %c  ===>本地相应的日期和时间表示
    %I  ===>一天中的第几个小时(12小时制，01-12)
    %p  ===>本地am或者pm的相应符
    %j 年内的一天（001-366）
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身
'''
#获取日历
import calendar
cal =calendar.month(2016,1)
print(cal)

print(time.clock())    #用以浮点数计算的秒数返回当前的cpu时间，用来衡量不同程序的耗时
print(time.perf_counter())
print(time.process_time())  #python3.8没有time.clock()方法