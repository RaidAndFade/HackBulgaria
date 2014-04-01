# Unit tests for solution.py (TopCoder - Problem Statement for MagicalStringDiv2)


# IMPORTS
from solution import minimal_moves
import unittest


# main
class MagicalStringDiv2Tests(unittest.TestCase):
    def test_null(self):
        self.assertEqual(2, minimal_moves(">><<><"))

    def test_one(self):
        self.assertEqual(0, minimal_moves(">>>><<<<"))

    def test_two(self):
        self.assertEqual(4, minimal_moves("<<>>"))

    def test_three(self):
        self.assertEqual(20, minimal_moves("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
