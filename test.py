# test_math_operations.py
import unittest
from math_operations import add_numbers, divide_numbers

class TestMathOperations(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-1, -1), -2)
    
    def test_add_decimal_numbers(self):
        self.assertAlmostEqual(add_numbers(2.5, 3.1), 5.6)
    
    def test_divide_valid_numbers(self):
        self.assertAlmostEqual(divide_numbers(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide_numbers(5, 0)

if __name__ == '__main__':
    unittest.main()
