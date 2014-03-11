# DOCUMENTATION

# IMPORTS
from solution import tabs_to_spaces
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_tabs_to_spaces_hello_world(self):
        self.assertEqual("hello\tworld", tabs_to_spaces("hello    world", 4))

    def test_tabs_to_spaces_goodbye_world(self):
        self.assertEqual("goodbye\tworld", tabs_to_spaces("goodbye    world", 4))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
