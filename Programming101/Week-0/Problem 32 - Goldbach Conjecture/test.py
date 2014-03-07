# Unit test for Problem 32 - Goldbach Conjecture

# IMPORTS
from solution import goldbach
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_4(self):
        self.assertEqual([(2,2)], goldbach(4))

    def test_6(self):
        self.assertEqual([(3,3)], goldbach(6))

    def test_8(self):
        self.assertEqual([(3,5)], goldbach(8))

    def test_10(self):
        self.assertEqual([(3,7), (5,5)], goldbach(10))

    def test_100(self):
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], goldbach(100))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
