# Unit test for Problem 26 - Spam and Eggs

# IMPORTS
from solution import prepare_meal
import unittest


# main
class TestPrepareMeal(unittest.TestCase):
    def test_5(self):
        self.assertEqual("eggs", prepare_meal(5))

    def test_3(self):
        self.assertEqual("spam", prepare_meal(3))

    def test_27(self):
        self.assertEqual("spam spam spam", prepare_meal(27))

    def test_15(self):
        self.assertEqual("spam and eggs", prepare_meal(15))

    def test_45(self):
        self.assertEqual("spam spam and eggs", prepare_meal(45))

    def test_7(self):
        self.assertEqual("", prepare_meal(7))

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
