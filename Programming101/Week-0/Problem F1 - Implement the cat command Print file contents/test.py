# Unit test for Problem F1 - Implement the cat command - Print file contents

# IMPORTS
from solution import main
import unittest

# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual("Python is an awesome language!\n You should try it.")

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
