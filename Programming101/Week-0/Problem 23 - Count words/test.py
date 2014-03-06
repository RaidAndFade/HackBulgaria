# Unit test for Problem 23 - Count words

# IMPORTS
from solution import count_words
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1}, count_words(["apple", "banana", "apple", "pie"]))

    def test_two(self):
        self.assertEqual({'ruby': 1, 'python': 3}, count_words(["python", "python", "python", "ruby"]))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
