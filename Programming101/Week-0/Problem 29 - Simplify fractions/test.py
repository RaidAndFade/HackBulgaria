# Unit test for Problem 29 - Simplify fractions

# IMPORTS
from solution import simplify_fraction
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual((1,3), simplify_fraction((3,9)))

    def test_two(self):
        self.assertEqual((1,7), simplify_fraction((1,7)))

    def test_three(self):
        self.assertEqual((2,5), simplify_fraction((4,10)))

    def test_four(self):
        self.assertEqual((3,22), simplify_fraction((63,462)))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
