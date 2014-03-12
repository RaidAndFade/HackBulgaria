# Problem 2 - To tab or to space?

# When you have your string_utils.py tested and running,
#  add the following function:

# tabs_to_spaces(str, one_tab_n_spaces=4) - which takes a string
# and replaces all tabs in it, with the amount
#  of one_tab_n_spaces of spaces. The default is 1 tab = 4 spaces.
# Here, a tab in a string is represented by the special '\t' symbol

# >>> a = "       string"
# >>> a
# '\tstring'
# When you have that tested, implement a Python script,
# called spacify.py, which takes a filename as the only
# argument and replaces all tabs in that file with 4 spaces.

# Use the string_utils.py module!


# IMPORTS
from re import sub
from sys import argv


# FUNCTIONS
def read_file_contents(filename):
    # read file contents
    file = open(filename, "r")
    contents = file.read()
    file.close()
    return contents


def write_file_contents(filename, contents):
    file = open(filename, "w")
    file.write(contents)
    file.close()


def tabs_to_spaces(string, one_tab_n_spaces):
    contents = read_file_contents(argv[1])
    # separator (tab)
    separator = " " * one_tab_n_spaces

    # replace spaces with tab in contents
    output = sub(" +", separator, contents)

    # write the contents to the file
    write_file_contents(string, output)

    # return the new contents
    return output


# main
def main():
    tabs_to_spaces(argv[1], 4)


# PROGRAM RUN
if __name__ == "__main__":
    main()
