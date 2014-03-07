# Problem F1 - Implement the cat command - Print file contents
#
# In linux, there is a very useful command, called cat:
#
# $ cat file.txt
# This is some file
# And cat is printing it's contents
# Implement a Python script, called cat.py that takes one argument - a filename
# and prints the contents of that file to the console.
#
# Boilerplate
#
# # cat.py
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
# If we have file.txt in the same directory with cat.py,
# and file.txt is with the following text:
#
# Python is an awesome language!
# You should try it.
# This is the result:
#
# $ python cat.py file.txt
# Python is an awesome language!
# You should try it.

# IMPORTS
from sys import argv, exit


# main
def main():
    filename = ""
    try:
        filename = argv[1]
    except IndexError:
        exit("Error: Give a file name to open!")

    file = ""
    content = ""
    try:
        file = open(filename, "r")
        content = file.read()
        print(content)
        file.close()

    except IOError:
        exit("Error: File not found!")

# PROGRAM RUN
if __name__ == '__main__':
    main()
