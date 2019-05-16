# /usr/bin/env python
# coding:utf-8


#常用的内置函数
'''
random:随机，测试多用于生成测试数据与测试报告文件的全名等
time：时间，测试多用于处理时间等待，测试报告带时间的格式输出
Os : 对操作系统进行操作
Sys :系统相关信息
Re : 正则
subprocess:进程，执行操作系统的命令
Logging:日志

'''
'''
import  time
import os

#生成的测试报告的名字是根据当前时间和文件名全名命名的
report_time = time.strftime('%Y%m%d%H%M%S',time.localtime())
print(report_time+"_"+os.path.basename(__file__))

import random
import string

#将序列中的某个随机数据取出来作为测试数据，序列可以是列表，字符串等
courses = ['python','java','selenium','appium']
random_course = random.choice(courses)
print(random_course)

#大写小写字母和数字随机拼接为测试数据
rad_str = ''.join(random.choice(string.ascii_uppercase\
                                +string.ascii_lowercase+string.digits)\
                  for _ in range(8))
print(rad_str+"@163.com")

for i in range(8):
    print(i)               #循环8次 _相当于一个占位符

import  logging

#创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

#创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')

#再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

#定义handler的输出格式
formatter = logging.Formatter('[%(asctime)s][%(filename)s][line:%(lineno)d][%(created)f][%(message)s]')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

#记录一条日志
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this,too')
logger.error('error return')
logger.critical('bug,bug')

'''
from  study import zuoye3

if __name__ == "__main__":
    zuoye3.sum_func([2,3,4,'a'])














