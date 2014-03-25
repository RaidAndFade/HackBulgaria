# Problem 5 - Count files by extension, extended

# Alter the program ext.py so it takes two arguments:

# the first - destination folder
# the second - file extension
# The program prints the number of files with the given file extension,
# located in the destination folder.

# Alter the tests, so they handle the new case.

# Examples:

# $ ls
# ext.py solution.py tests.py omg.txt program.cpp folder/
# $ ls folder/
# 1.py 2.py 3.py 4.py program2.cpp holy_moly.cpp
# $ python ext.py folder/ .py
# 4
# $ ls /home/user/code
# default.py solution.py tests.py requirements.txt package.json
# $ python ext.py /home/user/code .json
# 1


# IMPORTS
from glob import glob
from sys import argv


# FUNCTIONS
def number_of_files_with_extension(folder, extension):
    files = (glob('*%s/*%s' % (folder, extension)))
    return len(files)


# main
def main():
    print(number_of_files_with_extension(
        "HackBulgaria / Programming101 / Python / Week - 2 / Problem\ 5\ -\ Count\ files\ by\ extension\, \ extended /", ".py"))


# PROGRAM RUN
if __name__ == "__main__":
    main()
