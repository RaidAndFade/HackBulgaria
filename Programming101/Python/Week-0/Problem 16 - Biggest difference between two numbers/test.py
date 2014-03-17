# Unit test for Problem 16 - Biggest difference between two numbers

# IMPORTS
from solution import biggest_difference
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(-1, biggest_difference([1,2]))

    def test_two(self):
        self.assertEqual(-4, biggest_difference([1,2,3,4,5]))

    def test_three(self):
        self.assertEqual(-9, biggest_difference([-10, -9, -1]))

    def test_four(self):
        self.assertEqual(-99, biggest_difference(range(100)))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
