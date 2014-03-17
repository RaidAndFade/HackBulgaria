# Unit test for Problem 18 - Increasing sequence?


# IMPORTS
from solution import is_increasing
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_increasing([1, 2, 3, 4, 5]))

    def test_two(self):
        self.assertTrue(is_increasing([1]))

    def test_three(self):
        self.assertFalse(is_increasing([5, 6, -10]))

    def test_four(self):
        self.assertFalse(is_increasing([1, 1, 1, 1]))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
