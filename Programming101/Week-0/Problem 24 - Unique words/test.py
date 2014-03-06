# Unit test for Problem 24 - Unique words

# IMPORTS
from solution import unique_words_count
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(3, unique_words_count(["apple", "banana", "apple", "pie"]))

    def test_two(self):
        self.assertEqual(2, unique_words_count(["python", "python", "python", "ruby"]))

    def test_three(self):
        self.assertEqual(1, unique_words_count(["HELLO!"] * 10))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
