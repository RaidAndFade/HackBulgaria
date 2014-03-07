# Unit test for Problem 20 - What is the sign

# IMPORTS
from solution import what_is_my_sign
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_sign_Leo(self):
        self.assertEqual("Leo", what_is_my_sign(5, 8))

    def test_sign_Aquarius_january(self):
        self.assertEqual("Aquarius", what_is_my_sign(29, 1))

    def test_sign_Cancer(self):
        self.assertEqual("Cancer", what_is_my_sign(30, 6))

    def test_sign_Gemini(self):
        self.assertEqual("Gemini", what_is_my_sign(31, 5))

    def test_sign_Aquarius_february(self):
        self.assertEqual("Aquarius", what_is_my_sign(2, 2))

    def test_sign_Taurus(self):
        self.assertEqual("Taurus", what_is_my_sign(8, 5))

    def test_sign_Capricorn(self):
        self.assertEqual("Capricorn", what_is_my_sign(9, 1))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()