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


# FUNCTIONS
def tabs_to_spaces(string, one_tab_n_spaces):
    # separator (tab)
    separator = " " * one_tab_n_spaces

    # replace spaces with tab in contents
    output = sub(" +", separator, string)

    # return the new contents
    return output


# main
def main():
    tabs_to_spaces("    hello       world       !", 4)


# PROGRAM RUN
if __name__ == "__main__":
    main()
