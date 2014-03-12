# Unit test for spacify.py

# IMPORTS
from spacify import tabs_to_spaces
import unittest


# main
class Spacify_test_Case(unittest.TestCase):
    def test_one(self):
        self.assertEqual("some    lines", tabs_to_spaces(argv[1], 4))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
