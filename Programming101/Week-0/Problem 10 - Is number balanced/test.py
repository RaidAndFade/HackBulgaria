# Unit test for Problem 10 - Is number balanced

# IMPORTS
from solution import is_number_balanced
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_9(self):
        self.assertTrue(is_number_balanced(9))

    def test_11(self):
        self.assertTrue(is_number_balanced(11))

    def test_13(self):
        self.assertFalse(is_number_balanced(13))

    def test_121(self):
        self.assertTrue(is_number_balanced(121))

    def test_4518(self):
        self.assertTrue(is_number_balanced(4518))

    def test_28471(self):
        self.assertFalse(is_number_balanced(28471))

    def test_1238033(self):
        self.assertTrue(is_number_balanced(1238033))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
