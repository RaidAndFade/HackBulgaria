# Problem 1 - String Utils

# Implement a Python module, called string_utils.py,
# with the following functions:

# lines(text) - Takes a String argument text and
# returns a list of strings, where each element
# is each line in text
# unlines(elements) - Takes a list of Strings as
# argument and returns a String, where each element
# from elements is joined with new line
# words(text) - Takes a String argument text and
# returns a list of Strings, where each element
# is a word from text
# unwords(elements) - The reverse function of words.
# Takes a list of strings and returns a single string,
# where each element is joined by a single whitespace - " "
# Create a Unit Test file, called string_utils_tests.py
# and write as many test cases as you can think of, for those 4 functions.


# FUNCTIONS
def lines(text):
    return text.split("\n")


def unlines(list):
    return "\n".join(list)


def words(text):
    return text.split(" ")


def unwords(list):
    return " ".join(list)


# main
def main():
    lines("hello\nworld")
    lines("goodbye\nworld")

    unlines(["hello", "world"])
    unlines(["goodbye", "world"])

    words("hello world")
    words("goodbye world")

    unwords(["hello", "world"])
    unwords(["goodbye", "world"])


# PROGRAM RUN
if __name__ == "__main__":
    main()
