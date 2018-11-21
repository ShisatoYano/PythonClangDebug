# -*- coding: utf-8 -*-
"""
Unit Test code for C language code.

Test of function add

Last update: 2018/11/18
"""

import UnitTestSample
import unittest

class UnitTestAdd(unittest.TestCase):
    def test_a(self):
        input_a = UnitTestSample.py_make_pair(10, 5)
        ans_a   = UnitTestSample.py_add(input_a['a'], input_a['b'])
        self.assertEqual(ans_a, 15, 'Test A')
    
    def test_b(self):
        input_b = UnitTestSample.py_make_pair(23, 40)
        ans_b   = UnitTestSample.py_add(input_b['a'], input_b['b'])
        self.assertEqual(ans_b, 63, 'Test B')
    
    def test_c(self):
        input_c = UnitTestSample.py_make_pair(-120, 500)
        ans_c   = UnitTestSample.py_add(input_c['a'], input_c['b'])
        self.assertEqual(ans_c, 380, 'Test C')

if __name__ == '__main__':
    unittest.main()
