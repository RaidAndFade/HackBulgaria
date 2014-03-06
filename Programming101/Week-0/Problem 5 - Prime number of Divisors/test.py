# Unit test for Problem 5 - Prime number of Divisors

# IMPORTS
from solution import prime_number_of_divisors, is_prime
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(prime_number_of_divisors(7))

    def test_two(self):
        self.assertFalse(prime_number_of_divisors(8))

    def test_three(self):
        self.assertTrue(prime_number_of_divisors(9))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
