# /usr/bin/env python
# coding:utf-8

import pytest

def setup_module():
    print("整个模块开始")

def teardown_module():
    print("整个模块结束")

def setup_function():
    print("不在类中的函数前执行")

def teardown_function():
    print("不在类中的函数后执行")

def test_w_one():
    print("不在类中的方法1")

def test_w_two():
    print("不在类中的方法2")

class TestClass:
    def setup_class(self):
        print("类前执行")

    def teardown_class(self):
        print("类后执行")

    def setup_method(self):
        print("方法前执行")

    def teardown_method(self):
        print("方法后执行")

    def test_one(self):
        x = "this"
        assert "h5" in x

    def test_two(self):
        x = "hello"
        assert "hello1" == x

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b

if __name__ == '__main__':
    pytest.main(['-s', 'test_class1.py'])














