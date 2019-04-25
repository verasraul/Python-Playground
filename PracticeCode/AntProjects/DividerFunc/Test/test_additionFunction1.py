__author__ = 'verasraul'

'''
Test file for dividerFunction1.

'''

import unittest
from additionFunction1 import addition



class TestAdditionFunc(unittest.TestCase):

    def test_float_result(self):
        # Test func with int divided by float result
        self.assertEqual(addition(3, 1.0), 4.0)


    def test_int_result(self):
        # Test func with int divided int
        self.assertEqual(addition(3, 1), 4)


    def test_same_number_addition(self):
        # Test func when both numbers divided are the same
        self.assertEqual(addition(3, 3), 6)



if __name__ == '__main__':
    unittest.main()
