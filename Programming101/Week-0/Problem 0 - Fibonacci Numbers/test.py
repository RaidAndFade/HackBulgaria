# Unit test for Problem 0 - Fibonacci Numbers

# IMPORTS
from solution import nth_fibonacci
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_fibonacci_of_one(self):
        self.assertEqual(1, nth_fibonacci(1))
    def test_fibonacci_of_two(self):                
    def test_fibonacci_of_three(self):
        self.assertEqual(2, nth_fibonacci(3))
    def test_fibonacci_of_ten(self):
        self.assertEqual(55, nth_fibonacci(10))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
