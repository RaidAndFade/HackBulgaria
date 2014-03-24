# Unit test for Problem 7 - Integer Palindromes


# IMPORTS
from solution import is_int_palindrome
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_int_palindrome(1))

    def test_two(self):
        self.assertFalse(is_int_palindrome(42))

    def test_three(self):
        self.assertTrue(is_int_palindrome(100001))

    def test_four(self):
        self.assertTrue(is_int_palindrome(999))

    def test_five(self):
        self.assertFalse(is_int_palindrome(123))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
