#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test max_integer with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        """Test max_integer with a list containing a single element"""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        """Test max_integer with a list of positive numbers"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers"""
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list of mixed positive and negative no."""
        result = max_integer([-4, 2, -8, 10, -5])
        self.assertEqual(result, 10)

    def test_duplicate_numbers(self):
        """Test max_integer with a list containing duplicate numbers"""
        result = max_integer([2, 5, 2, 8, 2])
        self.assertEqual(result, 8)

    def test_float_numbers(self):
        """Test max_integer with a list of float numbers"""
        result = max_integer([1.5, 2.3, 0.9, 4.7])
        self.assertEqual(result, 4.7)


if __name__ == '__main__':
    unittest.main()
