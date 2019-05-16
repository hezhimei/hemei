# /usr/bin/env python
# coding:utf-8

'''
pytest优势：
简单灵活，像写Python代码一样写测试用例
为测试方法输入不同参数化
自动重试失败的测试用例
支持allure2测试报告
具有很多第三方插件
并且可以自定义扩展（http://plugincompat.herokuapp.com/)

编写规范：
测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有__init__方法
测试函数以test_开头

'''

import pytest

@pytest.fixture()
def loginandlogout():
    print('do login action\n')
    yield
    print('do logout action\n')

class TestSample:

    @pytest.mark.usefixtures('loginandlogout')
    def test_answer(self):
        print("I am test answer\n")
        assert  1+9 == 10

    @pytest.mark.usefixtures('loginandlogout')
    def test_answers(self):
        print("I am test answer2\n")
        assert  2+9 == 11

















