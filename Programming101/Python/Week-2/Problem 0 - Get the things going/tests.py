# Unit test for Problem 0 - Get the things going!


# IMPORTS
from solution import integer_divison, modulo
import unittest


# main
class Integer_Divison_Test(unittest.TestCase):
    def test_integer_division_one(self):
        self.assertEqual(0, integer_divison(5, 6))

    def test_integer_division_two(self):
        self.assertEqual(5, integer_divison(10, 2))

    def test_integer_division_three(self):
        self.assertEqual(0, integer_divison(2, 5))

    def test_modulo_one(self):
        self.assertEqual(5, modulo(5, 6))

    def test_modulo_two(self):
        self.assertEqual(0, modulo(10, 2))

    def test_modulo_three(self):
        self.assertEqual(2, modulo(2, 5))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
