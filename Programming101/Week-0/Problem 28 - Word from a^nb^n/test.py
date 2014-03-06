# Unit test for Problem 28 - Word from a^nb^n

# IMPORTS
from solution import is_an_bn
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_an_bn(""))

    def test_two(self):
        self.assertFalse(is_an_bn("rado"))

    def test_three(self):
        self.assertFalse(is_an_bn("aaabb"))

    def test_four(self):
        self.assertTrue(is_an_bn("aaabbb"))

    def test_five(self):
        self.assertFalse(is_an_bn("aabbaabb"))

    def test_six(self):
        self.assertFalse(is_an_bn("bbbaaa"))

    def test_seven(self):
        self.assertTrue(is_an_bn("aaaaabbbbb"))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
