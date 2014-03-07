# Problem F2 - Cat multiple file
#
# Implement a Python script, called cat2.py that
# takes multiple arguments - file names and prints the contents of all files
# to the console, in the order of the arguments.
#
# The number of the files that are given as arguments is unknown.
#
# There should be a newline between every two files that are printed.
#
# Boilerplate
#
# # cat2.py
# import sys
#
#
# def main():
#     pass
#
# if __name__ == '__main__':
#     main()
# Examples
#
# If we have two files - file1.txt and file2.txt
# in the same directory with cat2.py and:
#
# file1.txt:
#
# Python is an awesome language!
# You should try it.
# file2.txt:
#
# Also, you can use Python at a lot of different places!
# This is the result:
#
# $ python cat2.py file1.txt file2.txt
# Python is an awesome language!
# You should try it.
#
# Also, you can use Python at a lot of different places!

# IMPORTS
from sys import argv, exit


# main
def main():
    if len(argv) <= 1:
        exit("Error: Not enough arugments given!")

    filename = ""
    try:
        for i in range(1, len(argv)):
            filename = argv[i]
            file = open(filename, "r")
            content = file.read()
            print(content)

    except (IOError, IndexError):
        exit("Error: Make sure you have given valid file name arguments!")

# PROGRAM RUN
if __name__ == '__main__':
    main()
