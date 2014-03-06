# Unit test for Problem 13 - Consonants in a string

# IMPORTS
from solution import count_consonants
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(4, count_consonants("Python"))

    def test_two(self):
        self.assertEqual(11, count_consonants("Theistareykjarbunga"))

    def test_three(self):
        self.assertEqual(7, count_consonants("grrrrgh!"))

    def test_four(self):
        self.assertEqual(44, count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test_five(self):
        self.assertEqual(6, count_consonants("A nice day to code!"))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
