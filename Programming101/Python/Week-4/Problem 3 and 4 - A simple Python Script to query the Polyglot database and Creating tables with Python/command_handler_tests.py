# Unit tests for command_handler.py


# IMPORTS
from create_database import create_database
from os import remove
import command_handler
import unittest


# main
class CommandHandlerTest(unittest.TestCase):
    def setUp(self):
        create_database("tests.db")
        self.test_interface = command_handler.CommandHandler("tests.db")

    def test_trigger_help(self):
        self.assertEqual("list_employees - Prints out all employees, in the following format - \"name - position\"\nmonthly_spending - Prints out the total sum for monthly spending that the company is doing for salaries\nyearly_spending - Prints out the total sum for one year of operation (Again, salaries)\nadd_employee, the program starts to promt for data, to create a new employee.\ndelete_employee <employee_id>, the program should delete the given employee from the database\nupdate_employee <employee_id>, the program should prompt the user to change each of the fields for the given", self.test_interface.trigger_help())

    def test_trigger_unknown_command(self):
        self.assertEqual("Unknown command!\nWhy don't you enter help to see the available commands?", self.test_interface.trigger_unknown_command())

    def test_parse_command(self):
        expected = ("test", "command")
        self.assertTupleEqual(expected, self.test_interface.parse_command("test command"))

    def test_is_command_true(self):
        command_tuple = ("test", "command")
        self.assertTrue(self.test_interface.is_command(command_tuple, "test"))

    def test_is_command_false(self):
        command_tuple = ("test", "command")
        self.assertFalse(self.test_interface.is_command(command_tuple, "command"))

    def test_trigger_list_employees(self):
        expected = "[1] Ivan Ivanov - Software Developer\n[2] Rado Rado - Technical Support Intern\n[3] Ivo Ivo - CEO\n[4] Petar Petrov - Marketing Manager\n[5] Maria Georgieva - COO"
        self.assertEqual(expected, self.test_interface.trigger_list_employees())

    def test_trigger_monthly_spending(self):
        self.assertEqual(26500, self.test_interface.trigger_monthly_spending())

    def test_trigger_yearly_spending(self):
        self.assertEqual(439000, self.test_interface.trigger_yearly_spending())

    def test_add_employee(self):
        self.assertTrue(self.test_interface.add_employee("Beer", 2000, 1, "Fuel"))

    def test_add_existing_employee(self):
        self.assertFalse(self.test_interface.add_employee("Ivan Ivanov", 5000, 10000, "Software Developer"))

    def test_trigger_delete_employee(self):
        self.assertEqual("Ivan Ivanov was deleted.", self.test_interface.trigger_delete_employee(1))

    def test_trigger_delete_non_existing_employee(self):
        self.assertEqual("Ivan Ivanov was deleted.", self.test_interface.trigger_delete_employee(1))
        self.assertFalse(self.test_interface.trigger_delete_employee(1))

    def tearDown(self):
        remove("tests.db")


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
