# Unit tests for filehandler.py


# IMPORTS
from os import remove
from glob import glob
from filehandler import FileHandler
import unittest


class FileHandlerTests(unittest.TestCase):
    def setUp(self):
        self.fh = FileHandler()

    def test_take_order(self):
        self.assertTrue(self.fh.take_order("Person", 5))
        self.assertEqual({"Person": 5}, self.fh.orders)

    def test_take_second_order(self):
        self.assertTrue(self.fh.take_order("Person", 5))
        self.assertTrue(self.fh.take_order("Person", 10))
        self.assertEqual({"Person": 15}, self.fh.orders)

    def test_list_orders(self):
        self.assertTrue(self.fh.take_order("Person", 5))
        self.assertEqual("Person - 5", self.fh.list_orders())

    def test_fetch_files(self):
        self.assertEqual([], self.fh.fetch_files())

    def test_save_file(self):
        self.assertTrue(self.fh.take_order("Person", 5))
        self.assertTrue(self.fh.save_file())
        files = self.fh.fetch_files()
        self.assertEqual(1, len(files))

    def test_fetch_file_name(self):
        self.assertTrue(self.fh.save_file())
        self.fh.list_files()
        self.assertEqual(self.fh.files[0], self.fh.fetch_file_name(0))

    def test_fetch_history(self):
        self.assertTrue(self.fh.take_order("Person", 5))
        self.assertEqual("take", self.fh.fetch_history())

    def tearDown(self):
        for filename in glob("./orders_*"):
            remove(filename)


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
