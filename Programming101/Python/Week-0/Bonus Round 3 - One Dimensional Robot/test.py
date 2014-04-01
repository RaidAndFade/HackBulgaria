# Unit tests for solution.py (TopCoder - Problem Statement for OneDimensionalRobotEasy)


# IMPORTS
from solution import final_position
import unittest


# main
class OneDimensionalRobotTests(unittest.TestCase):
    def test_null(self):
        self.assertEqual(2, final_position("RRLRRLLR", 10, 10))

    def test_one(self):
        self.assertEqual(4, final_position("RRRRR", 3, 4))

    def test_two(self):
        self.assertEqual(-1, final_position("LLLLLLLLLLR", 2, 6))

    def test_three(self):
         self.assertEqual(20, final_position("RRRRRRRLRRLRRRRRRRRRRRRLRLRRRRRRRRLRRRRRLRRRRRRRRR", 5, 20))

    def test_four(self):
        self.assertEqual(-30, final_position("RLRLLLLLLLRLLLRLLLLLLLLRLLLLLRLLLRRLLLLLRLLLLLRLLL", 34, 15))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
