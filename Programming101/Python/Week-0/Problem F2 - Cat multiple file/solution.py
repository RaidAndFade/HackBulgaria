# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems3.md#problem-f2---cat-multiple-file


# IMPORTS
from sys import argv, exit


# FUNCTIONS
def cat(filename):
    try:
        opened_file = open(filename, "r")
        contents = opened_file.read()
        opened_file.close()
    except IOError:
        return False

    return contents.rstrip()


# main
def main():
    if len(argv) <= 1:
        exit("Error: Not enough arguments given!")

    filename = ""
    try:
        for i in range(1, len(argv)):
            filename = argv[i]
            print(cat(filename))

    except (IOError, IndexError):
        exit("Error: Make sure you have given valid file name arguments!")


# PROGRAM RUN
if __name__ == '__main__':
    main()
