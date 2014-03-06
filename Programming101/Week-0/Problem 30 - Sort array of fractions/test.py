# Unit test for Problem 30 - Sort array of fractions

# IMPORTS
from solution import sort_fractions
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual([(1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2)]))

    def test_two(self):
        self.assertEqual([(1, 3), (1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2), (1, 3)]))

    def test_three(self):
        self.assertEqual([(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)], sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
