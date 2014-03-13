# Unit test for Problem 5 - Count files by extension, extended

# IMPORTS
from ext import number_of_files_with_extension
import unittest


# main
class NumberOfFielsWithExtension(unittest.TestCase):
    def test_extension_py(self):
        self.assertEqual(2, number_of_files_with_extension(
                         "/HackBulgaria/Programming101/Python/Week - 2 / Problem\ 5\ -\ Count\ files\ by\ extension\, \ extended /", ".py"))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
