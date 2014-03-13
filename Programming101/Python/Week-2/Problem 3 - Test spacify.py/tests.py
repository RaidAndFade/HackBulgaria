# Unit test for spacify.py

# IMPORTS
from spacify import tabs_to_spaces
from os import remove
import unittest


# main
class Spacify_test_Case(unittest.TestCase):
    def setUp(self):
        file = open("test_bunny.txt", "w")
        file.write("        hello          world       !      ")
        file.close()

        file = open("test_bunny.txt", "r")
        self.contents = file.read()
        file.close()


    def test_4_spaces_tab(self):
        self.assertEqual("    hello    world    !    ", tabs_to_spaces(self.contents, 4))

    def test_3_spaces_tab(self):
        self.assertEqual("   hello   world   !   ", tabs_to_spaces(self.contents, 3))

    def test_2_spaces_tab(self):
        self.assertEqual("  hello  world  !  ", tabs_to_spaces(self.contents, 2))

    def test_1_spaces_tab(self):
        self.assertEqual(" hello world ! ", tabs_to_spaces(self.contents, 1))

    def tearDown(self):
        remove("test_bunny.txt")


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
