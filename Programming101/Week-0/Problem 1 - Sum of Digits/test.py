# Unit test for Problem 1 - Sum of Digits

# IMPORTS
from solution import sum_of_digits
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_sum_digits_of_1325132435356(self):
        self.assertEqual(43, sum_of_digits(1325132435356))
    def test_sum_digits_of_123(self):
        self.assertEqual(6, sum_of_digits(123))
    def test_sum_digits_of_6(self):
        self.assertEqual(6, sum_of_digits(6))
    def test_sum_digits_of_minus_10(self):
        self.assertEqual(1, sum_of_digits(-10))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
