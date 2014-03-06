# Unit test for Problem 14 - Turn a number into a list of digits

# IMPORTS
from solution import number_to_list
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual([1, 2, 3], number_to_list(123))

    def test_two(self):
        self.assertEqual([9, 9, 9, 9, 9], number_to_list(99999))

    def test_three(self):
        self.assertEqual([1, 2, 3, 0, 2, 3], number_to_list(123023))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
