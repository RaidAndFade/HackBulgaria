# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems3.md#problem-f1---implement-the-cat-command---print-file-contents


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
    filename = ""
    try:
        filename = argv[1]
    except IndexError:
        return False

    print(cat(filename))


# PROGRAM RUN
if __name__ == '__main__':
    main()
