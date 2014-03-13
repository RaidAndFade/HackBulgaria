# Problem 4 - Count files by extension

# Implement a program, called ext.py, which takes one argument
# - a file extension and prints to the output, the number of files
# with the given extension, that are located in the current directory 
# (From where we run ext.py)

# For example:

# $ ls
# ext.py solution.py tests.py omg.txt program.cpp folder/
# $ python ext.py .py
# 3
# $ python ext.py py
# 0
# $ python ext.py .cpp
# 1
# Implement a Unit Test, testing ext.py


# IMPORTS
from glob import glob
from sys import argv


# FUNCTIONS
def number_of_files_with_extension(extension):
    files = (glob('*%s' % extension))
    return len(files)


# main
def main():
    number_of_files_with_extension(argv[1])


# PROGRAM RUN
if __name__ == "__main__":
    main()
