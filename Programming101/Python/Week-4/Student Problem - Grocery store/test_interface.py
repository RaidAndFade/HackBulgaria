# Unit test for interface.py


# IMPORTS
from os import remove
from create_database import create_database
from interface import CLI
import unittest


# main
class CLI_Tests(unittest.TestCase):
    def setUp(self):
        create_database("tests.db")
        self.test_interface = CLI("tests.db")

    def test_parse_command(self):
        expected = ("test", "command")
        self.assertTupleEqual(expected, self.test_interface.parse_command("test command"))

    def test_is_command(self):
        command = self.test_interface.parse_command("test command")
        self.assertTrue(self.test_interface.is_command(command, "test"))

    def test_is_not_command(self):
        command = self.test_interface.parse_command("test command")
        self.assertFalse(self.test_interface.is_command(command, "command"))

    def test_trigger_unknown_command(self):
        self.assertEqual("Error: Unknown Command!\nWhy don't you enter help to see available commands?", self.test_interface.trigger_unknown_command())

    def tearDown(self):
        remove("tests.db")


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
