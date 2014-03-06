# Unit test for Problem 21 - Integer prime factorization

# IMPORTS
from solution import prime_factorization
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_10(self):
        self.assertEqual([(2, 1), (5, 1)], prime_factorization(10))

    def test_14(self):
        self.assertEqual([(2, 1), (7, 1)], prime_factorization(14))

    def test_356(self):
        self.assertEqual([(2, 2), (89, 1)], prime_factorization(356))

    def test_89(self):
        self.assertEqual([(89, 1)], prime_factorization(89))

    def test_1000(self):
        self.assertEqual([(2, 3), (5, 3)], prime_factorization(1000))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
