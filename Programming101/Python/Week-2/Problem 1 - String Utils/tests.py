# Unit test for Problem 1 - String Utils

# IMPORTS
from solution import lines, unlines, words, unwords
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_lines_hello_world(self):
        self.assertEqual(["hello", "world"], lines("hello\nworld"))

    def test_lines_goodbye_world(self):
        self.assertEqual(["goodbye", "world"], lines("goodbye\nworld"))

    def test_unlines_hello_world(self):
        self.assertEqual("hello\nworld", unlines(["hello", "world"]))

    def test_unlines_goodbye_world(self):
        self.assertEqual("goodbye\nworld", unlines(["goodbye", "world"]))

    def test_words_hello_world(self):
        self.assertEqual(["hello", "world"], words("hello world"))

    def test_words_goodbye_world(self):
        self.assertEqual(["goodbye", "world"], words("goodbye world"))

    def test_unwords_hello_world(self):
        self.assertEqual("hello world",  unwords(["hello", "world"]))

    def test_unwords_goodbye_world(self):
        self.assertEqual("goodbye world", unwords(["goodbye", "world"]))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
