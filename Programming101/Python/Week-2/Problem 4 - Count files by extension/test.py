# Unit test for Problem 4 - Count files by extension

# IMPORTS
from ext import number_of_files_with_extension
import unittest


# main
class TestNumberOfFilesWithExtension(unittest.TestCase):
    def test_number_of_files_with_py_extension(self):
        self.assertEqual(2, number_of_files_with_extension(".py"))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
