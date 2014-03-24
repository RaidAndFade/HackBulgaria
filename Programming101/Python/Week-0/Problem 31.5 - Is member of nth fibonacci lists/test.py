# Unit test for Problem 31.5 - Is member of nth fibonacci lists


# IMPORTS
from solution import member_of_nth_fib_lists
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertFalse(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))

    def test_two(self):
        self.assertTrue(member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))

    def test_three(self):
        self.assertTrue(member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))

    def test_four(self):
        self.assertFalse(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
