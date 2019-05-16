# /usr/bin/env python
# coding:utf-8
'''
pytest--多个assert（pytest.assume)
测试场景：
    一个测试用例中有多个数据需要比较
1，一个个比较 or 放到一个数据结构里面全量比较？
    全量比较，无法知道那个值不对
    一个个比较数值，第一个失败就退出

pytest-rerunfails
测试场景：
    在web，app自动化测试中，经常出现超时导致测试失败

加成等待时间 or 重新执行？
方法：pytest重新跑失败的测试用例
pytest --reruns 3 src/testcases/api/test_pyexample_rerun.py

pytest-ordering
测试场景：
1，在web测试中，上下测试用例页面切换有依赖关系
2，在修改信息的页面中，依赖于前面用例已经创建好的信息，比如修改账号信息，依赖于已经创建好的数据
'''
'''
import time
#import pytest

def add(x,y):
    return x+y

def test_add():
    assert add(1,2)==3

def test_add2():
    print("I am 2")
    time.sleep(3)
    assert add(1.2,3.1) == 5.3
    assert add(1,2) == 3
'''
'''
import  random
def add(x,y):
    return x+y

def test_add2():
    random_value = random.randint(2,7)
    print("random_value:"+str(random_value))
    assert add(1,3) == random_value

'''

import pytest
import time

value =0
@pytest.mark.run(order=2)
def test_add2():
    print("I am 2")
    time.sleep(2)
    assert value == 10

@pytest.mark.run(order=1)
def test_add():
    print("I am test add")
    global value
    value =10
    assert value == 10

