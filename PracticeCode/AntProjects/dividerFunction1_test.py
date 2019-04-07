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

    def test_float_result(self):
        # capture result of divider func
        result = divider(3, 1.0)
        # expected result of func
        expected_result = 3.0
        self.assertEqual(result, expected_result)








if __name__=="__main__":
    unittest.main()
