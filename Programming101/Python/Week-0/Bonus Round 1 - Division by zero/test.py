# Unit tests for solution.py (TopCoder - Problem Statement for DivideByZero)


# IMPORTS
from solution import count_numbers
import unittest


# main
class DivisionByZeroTests(unittest.TestCase):
    def test_null(self):
        self.assertEqual(3, count_numbers([9, 2]))

    def test_one(self):
        self.assertEqual(3, count_numbers([8, 2]))

    def test_two(self):
        self.assertEqual(1, count_numbers([50]))

    def test_three(self):
        self.assertEqual(11, count_numbers([1, 5, 8, 30, 15, 4]))

    def test_four(self):
        self.assertEqual(7, count_numbers([1, 2, 4, 8, 16, 32, 64]))

    def test_five(self):
        self.assertEqual(7, count_numbers([6, 2, 18]))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
