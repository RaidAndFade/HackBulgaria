# Unit tests for Problem F6 - Count characters, words or lines


# IMPORTS
from solution import count_chars
from solution import count_words
from solution import count_lines
from os import remove
import unittest


# main
class TestCase(unittest.TestCase):
    def setUp(self):
        self.filename = "dummy_file"
        dummy_file = open(self.filename, "w")
        dummy_file.write("Now indulgence dissimilar for his thoroughly has terminated. Agreement offending commanded my an. Change wholly say why eldest period. Are projection put celebrated particular unreserved joy unsatiable its. In then dare good am rose bred or. On am in nearer square wanted.\n\nOf resolve to gravity thought my prepare chamber so. Unsatiable entreaties collecting may sympathize nay interested instrument. If continue building numerous of at relation in margaret. Lasted engage roused mother an am at. Other early while if by do to. Missed living excuse as be. Cause heard fat above first shall for. My smiling to he removal weather on anxious.\n\nFerrars all spirits his imagine effects amongst neither. It bachelor cheerful of mistaken. Tore has sons put upon wife use bred seen. Its dissimilar invitation ten has discretion unreserved. Had you him humoured jointure ask expenses learning. Blush on in jokes sense do do. Brother hundred he assured reached on up no. On am nearer missed lovers. To it mother extent temper figure better.\n")
        dummy_file.close()

    def test_count_chars(self):
        self.assertEqual(1032, count_chars(self.filename))

    def test_count_words(self):
        self.assertEqual(166, count_words(self.filename))

    def test_count_lines(self):
        self.assertEqual(6, count_lines(self.filename))

    def tearDown(self):
        remove("dummy_file")


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
