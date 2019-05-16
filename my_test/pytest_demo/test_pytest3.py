# /usr/bin/env python
# coding:utf-8

'''
pytest参数化
测试场景：
1，测试登录成功，登录失败（账号错误，密码错误）
2，创建多种账号：中文账号，英文账号

copy多份代码 or 读入参数
一次性执行多个输入参数
pytest.mark.parametrize


'''

import pytest

@pytest.mark.parametrize("x,y",[(3+5,8),(2+4,6),(6*9,42)])

def test_add(x,y):
    assert x == y


