# Unit test for Problem 6 - Sevens in A Row

# IMPORTS
from solution import sevens_in_a_row
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))

    def test_two(self):
        self.assertFalse(sevens_in_a_row([1, 7, 1, 7, 7], 4))

    def test_three(self):
        self.assertTrue(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))

    def test_four(self):
        self.assertTrue(sevens_in_a_row([7, 2, 1, 6, 2], 1))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
