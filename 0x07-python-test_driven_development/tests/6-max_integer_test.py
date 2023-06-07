=============================
Maximum integer function test
=============================


import unittest
from max_integer import max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 2, -3, 4, -5])
        self.assertEqual(result, 4)

    def test_duplicate_numbers(self):
        result = max_integer([5, 5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_single_element_list(self):
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_float_numbers(self):
        result = max_integer([1.5, 2.7, 3.2, 4.9])
        self.assertEqual(result, 4.9)

    def test_mixed_float_and_integer(self):
        result = max_integer([1, 2.5, 3, 4.2])
        self.assertEqual(result, 4.2)

if __name__ == '__main__':
    unittest.main()
