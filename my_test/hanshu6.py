# /usr/bin/env python
# coding:utf-8
#装饰器
import time,random

def time_count(func):
    def wrap(*args,**kwargs):
        time_flag=time.time()
        temp_result=func(*args,**kwargs)
        print("time cost:",time.time()-time_flag)
        return temp_result
    return wrap

'''
@time_count            #time_count(loop_time)

def loop_time(x,y):
    temp_result=0
    for i in range(x,y):
        time.sleep(random.choice((0.1,0.2,0.3)))
        temp_result=x + y
    return temp_result

loop_time(1,10)
loop_time(1,10)
loop_time(1,10)
'''
@time_count

def set_time(x,y):
    temp_result =0
    for i in range(x,y):
        time.sleep(random.choice((0.1,0.2,0.3)))
        temp_result=x + y
    return temp_result

set_time(1,3)
set_time(1,3)
set_time(1,3)