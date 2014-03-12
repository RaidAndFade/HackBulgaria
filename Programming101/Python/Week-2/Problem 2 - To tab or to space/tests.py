# Unit test for Problem 2 - To tab or to space

# IMPORTS
from solution import tabs_to_spaces
import unittest


# main
class Test_tabs_to_spaces(unittest.TestCase):
    def test_tabs_to_spaces_hello_world_tab_4(self):
        self.assertEqual(
            "    hello    world    ", tabs_to_spaces("         hello         world             ", 4))

    def test_tabs_to_spaces_goodbye_world_tab_3(self):
        self.assertEqual(
            "   goodbye   world   ", tabs_to_spaces("           goodbye       world     ", 3))

    def test_tabs_to_spaces_hello_world_tab_2(self):
        self.assertEqual(
            "  hello  world  ", tabs_to_spaces("     hello         world       ", 2))

    def test_tabs_to_spaces_goodbye_world_tab_1(self):
        self.assertEqual(
            " goodbye world ", tabs_to_spaces("        goodbye         world           ", 1))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
