import unittest
from dividerFunction1 import divider

# Test for dividerFunction1 pycode.
# Test 1; func will throw an error when dividing by zero
# Test 2; func will return a float when dividing by an Int by a float


#divider(3,1)

class TestDividerFunc(unittest.TestCase):
    def test_zero_division_error(self):
        # Make sure value errors is raised when int is divided by zero.
        self.assertRaises(ZeroDivisionError, divider, 3, 0)

    # Test func with int divided by float result
    def test_float_result(self):
        # capture result of divider func
        float_result = divider(3, 1.0)
        # expected result of func
        expected_float_result = 3.0
        self.assertEqual(float_result, expected_float_result)

    # Test func with float divided by float
    def test_float_division(self):
        # capture result of divider func
        floatDiv_result = divider(3.0, 1.0)
        # expected result of func
        expected_floatDiv_result = 3.0
        self.assertEqual(floatDiv_result, expected_floatDiv_result)

    # Test func with 2 integers being divided
    #









if __name__=="__main__":
    unittest.main()
