# /usr/bin/env python
# coding:utf-8

import unittest

class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("init class\n")
        simple_test.foo = list(range(10))
        print(str(simple_test.foo)+'\n')

    def test_1st(self):
        print(simple_test.foo)
        self.assertEqual(simple_test.foo.pop(),9)

    def test_2nd(self):
        print(simple_test.foo)
        self.assertEqual(simple_test.foo.pop(),8)

    @classmethod
    def tearDownClass(cls):
        print("end class\n")

if __name__=="__main__":
    unittest.main()