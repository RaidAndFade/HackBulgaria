# Unit test for Problem F4 - Sum integers from file


# IMPORTS
from solution import sum_integers_from_file
from os import remove
import unittest


# main
class SumIntegerFromFileTestCase(unittest.TestCase):
    def test_sum_one_number_on_line(self):
        filename = "dummy_file_test_sum_number_on_line.txt"
        opened_file = open(filename, "w")
        opened_file.write("1\n2")
        opened_file.close()
        self.assertEqual(1+2, sum_integers_from_file(filename))
        remove(filename)

    def test_sum_two_numbers_on_line(self):
        filename = "dummy_file_test_sum_two_numbers_on_line.txt"
        opened_file = open(filename, "w")
        opened_file.write("1 2 \n3 4")
        opened_file.close()
        self.assertEqual(1+2+3+4, sum_integers_from_file(filename))
        remove(filename)


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
