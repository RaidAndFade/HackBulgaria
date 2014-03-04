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
# If we have file.txt in the same directory with cat.py, and file.txt is with the following text:
#
# Python is an awesome language!
# You should try it.
# This is the result:
#
# $ python cat.py file.txt
# Python is an awesome language!
# You should try it.

# IMPORTS
import sys

# main
def main():
    filename = sys.argv[1]
    file = open(filename, "r")
    content = file.read()
    print("-------FILE CONTENTS---------")
    print(content)
    file.close()

# PROGRAM RUN
main()