# Unit test for Problem 26 - Spam and Eggs

# IMPORTS
from solution import prepare_meal
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_5(self):
        self.assertEqual("eggs", spam_and_eggs(5))

    def test_3(self):
        self.assertEqual("spam", spam_and_eggs(3))

    def test_27(self):
        self.assertEqual("spam spam spam", spam_and_eggs(27))

    def test_15(self):
        self.assertEqual("spam and eggs", spam_and_eggs(15))

    def test_45(self):
        self.assertEqual("spam spam and eggs", spam_and_eggs(45))

    def test_7(self):
        self.assertEqual("", spam_and_eggs(7))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
