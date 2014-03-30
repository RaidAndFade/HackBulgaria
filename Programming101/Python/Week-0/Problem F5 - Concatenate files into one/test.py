# Unit tests for Problem F5 - Concatenate files into one


# IMPORTS
from os import remove
from solution import concatenate
from solution import write_to_megatron
import unittest


# main
class MEGATRON_Tests(unittest.TestCase):
    def setUp(self):
        file_a = open("test_file_a", "w")
        file_a.write("Python is an awesome language!\nYou should try it.")
        file_a.close()
        file_b = open("test_file_b", "w")
        file_b.write("Also, you can use Python at a lot of different places!")
        file_b.close()
        self.expected = "Python is an awesome language!\nYou should try it.\nAlso, you can use Python at a lot of different places!"

    def test_concatenate(self):
        self.assertEqual(self.expected, concatenate(("test_file_a", "test_file_b")))

    def test_concatenate_non_existing_files(self):
        self.assertEqual("Error: File not found!", concatenate(("non_existing_a", "non_existing_b")))

    def test_write_to_megatron(self):
        write_to_megatron(concatenate(("test_file_a", "test_file_b")))
        megatron = open("MEGATRON", "r")
        self.assertEqual(self.expected, megatron.read())
        megatron.close()
        remove("MEGATRON")

    def tearDown(self):
        remove("test_file_a")
        remove("test_file_b")


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
