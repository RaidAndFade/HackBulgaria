# Unit test for Problem 31 - Fibonacci lists


# IMPORTS
from solution import nth_fib_lists
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual([1], nth_fib_lists([1], [2], 1))

    def test_two(self):
        self.assertEqual([2], nth_fib_lists([1], [2], 2))

    def test_three(self):
        self.assertEqual([1, 2, 1, 3], nth_fib_lists([1, 2], [1, 3], 3))

    def test_four(self):
        self.assertEqual([1, 2, 3, 1, 2, 3], nth_fib_lists([], [1, 2, 3], 4))

    def test_five(self):
        self.assertEqual([], nth_fib_lists([], [], 100))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
