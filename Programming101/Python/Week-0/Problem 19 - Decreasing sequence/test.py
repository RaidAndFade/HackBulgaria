# Unit test for Problem 19 - Decreasing sequence


# IMPORTS
from solution import is_decreasing
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_decreasing([5, 4, 3, 2, 1]))

    def test_two(self):
        self.assertFalse(is_decreasing([1, 2, 3]))

    def test_three(self):
        self.assertTrue(is_decreasing([100, 50, 20]))

    def test_four(self):
        self.assertFalse(is_decreasing([1, 1, 1, 1]))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
