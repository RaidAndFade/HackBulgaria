# Unit test for Problem 27 - Reduce file path


# IMPORTS
from solution import reduce_file_path
import unittest


# main
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual("/", reduce_file_path("/"))

    def test_two(self):
        self.assertEqual("/", reduce_file_path("/srv/../"))

    def test_three(self):
        self.assertEqual("/srv/www/htdocs/wtf", reduce_file_path("/srv/www/htdocs/wtf/"))

    def test_four(self):
        self.assertEqual("/srv/www/htdocs/wtf", reduce_file_path("/srv/www/htdocs/wtf"))

    def test_five(self):
        self.assertEqual("/srv", reduce_file_path("/srv/./././././"))

    def test_six(self):
        self.assertEqual("/etc/wtf", reduce_file_path("/etc//wtf/"))

    def test_seven(self):
        self.assertEqual("/", reduce_file_path("/etc/../etc/../etc/../"))

    def test_eight(self):
        self.assertEqual("/", reduce_file_path("//////////////"))

    def test_nine(self):
        self.assertEqual("/", reduce_file_path("/../"))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
