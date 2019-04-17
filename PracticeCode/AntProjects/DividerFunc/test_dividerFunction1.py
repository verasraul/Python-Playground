__author__ = 'verasraul'
'''
Test file for dividerFunction1.

'''

import unittest
from dividerFunction1 import divider



class TestDividerFunc(unittest.TestCase):
    def test_zero_division_error(self):
        # Make sure value errors is raised when int is divided by zero.
        self.assertRaises(ZeroDivisionError, divider, 3, 0)


    def test_float_result(self):
        # Test func with int divided by float result
        self.assertEqual(divider(3, 1.0), 3.0)


    def test_float_division(self):
        # Test func with float divided by float
        self.assertEqual(divider(3.0, 1.0), 3.0)


    def test_int_division(self):
        # Test func with int divided int
        self.assertEqual(divider(3, 1), 3.0)


    def test_same_number_division(self):
        # Test func when both numbers divided are the same
        self.assertEqual(divider(3, 3), 1)


    def test_division_by_higher_number(self):
        # Test func when both numbers divided are the same
        self.assertEqual(divider(3, 6), 0.5)


if __name__ == '__main__':
    unittest.main()
