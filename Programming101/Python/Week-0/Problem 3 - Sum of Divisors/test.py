# Unit test for Problem 3 - Sum of Divisors

# IMPORTS
from solution import sum_of_divisors
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(15, sum_of_divisors(8))

    def test_two(self):
        self.assertEqual(8, sum_of_divisors(7))

    def test_three(self):
        self.assertEqual(1, sum_of_divisors(1))

    def test_four(self):
        self.assertEqual(2340, sum_of_divisors(1000))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
