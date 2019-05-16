# /usr/bin/env python
# coding:utf-8

from my_test import htmltestrunner
import unittest
from my_test import test_unitest3
from my_test import test_uitest2

report_title = '执行报告'
desc = '测试用例执行报告'
report_file = './testcases/report/UnittestReport.html'
testsuite = unittest.TestSuite()
testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_unitest3.simple_test))
testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_uitest2.SimpleTest))

with open(report_file, 'wb') as report:
    runner = htmltestrunner.HTMLTestRunner(stream=report, title=report_title, description=desc)
    runner.run(testsuite)