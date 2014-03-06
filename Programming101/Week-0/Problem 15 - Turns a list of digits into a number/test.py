# Unit test for Problem 15 - Turn a list of digits into a number

# IMPORTS
from solution import list_to_number
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(123, list_to_number([1,2,3]))

    def test_two(self):
        self.assertEqual(99999, list_to_number([9,9,9,9,9]))

    def test_three(self):
        self.assertEqual(123023, list_to_number([1,2,3,0,2,3]))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
