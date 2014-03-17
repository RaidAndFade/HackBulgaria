# Unit test for Problem 17 - Slope style score


# IMPORTS
from solution import slope_style_score
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertAlmostEqual(94.66, slope_style_score([94, 95, 95, 95, 90]), places=1)

    def test_two(self):
        self.assertEqual(80.0, slope_style_score([60, 70, 80, 90, 100]))

    def test_three(self):
        self.assertEqual(93.5, slope_style_score([96, 95.5, 93, 89, 92]))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
