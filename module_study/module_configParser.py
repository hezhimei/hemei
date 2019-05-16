# /usr/bin/env python
# coding:utf-8

#用来解析类似。ini文件
'''
config实例常用方法：
    config.get('Section','options') 获取指定section下对应的option的值
    config.section()   获取配置文件中所有的sections
    config.has_section('section')  判断配置文件中是否有对应session
    config.has_option('section','option')  判断对应section是否有对应的option

'''
import configparser

def get_cfg(in_file):
    config = configparser.ConfigParser()
    config.read(in_file)
    return config
cfg = get_cfg("test.cfg")
print(cfg.get("mail_server","smtp_host"))
