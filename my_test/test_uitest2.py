# /usr/bin/env python
# coding:utf-8

'''
unittest是Python内嵌的测试框架，原名为pyunit
unittest提供了test cases,test suites,test fixtures,test runner相关的组件
编写规范：
测试模块首先import unittest
测试类必须继承 unittest.testcase
测试方法必须以"test_"开头
模块名字，类名没有要求

基于测试方法级别的setUp,tearDown
    执行每个测试方法的时候都会执行一次setUp和tearDown
基于类级别的setUpClass,tearDownClass
    执行这个类里面的所有测试方法，只有一次执行setup，tearDown
基于模块级别的setUpModule,tearDownModule
    执行此模块里的所有类里的测试方法，只执行一次setup和teardown

'''

import unittest


class SimpleTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("setup method")
        self.foo = list(range(10))
        print(str(self.foo))

    def test_1st(self):
        print("test_1st")
        self.assertEqual(self.foo.pop(),9)

    def test_2nd(self):
        print("test_2nd")
        self.assertEqual(self.foo.pop(),9)

    @classmethod
    def tearDown(self):
        print("end method")


if __name__ == '__main__':
    unittest.main()
