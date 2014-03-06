# Unit test for Problem 9 - Number containing all digits

# IMPORTS
from solution import contains_digits
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(contains_digits(402123, [0, 3, 4]))

    def test_two(self):
        self.assertFalse(contains_digits(666, [6, 4]))

    def test_three(self):
        self.assertFalse(contains_digits(123456789, [1, 2, 3, 0]))

    def test_four(self):
        self.assertFalse(contains_digits(456, []))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
