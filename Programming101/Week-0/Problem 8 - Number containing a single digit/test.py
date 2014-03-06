# Unit test for Problem 8 - Number containing a single digit

# IMPORTS
from solution import contains_digit
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertFalse(contains_digit(123, 4))

    def test_two(self):
        self.assertTrue(contains_digit(42, 2))

    def test_three(self):
        self.assertTrue(contains_digit(1000, 0))

    def test_four(self):
        self.assertFalse(contains_digit(12346789, 5))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
