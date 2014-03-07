# Unit test for Problem 4 - Is Prime

# IMPORTS
from solution import is_prime
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_two(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_eight(self):
        self.assertFalse(is_prime(8))

    def test_is_prime_eleven(self):

        self.assertTrue(is_prime(11))

    def test_is_prime_minus_ten(self):
        self.assertFalse(is_prime(-10))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
