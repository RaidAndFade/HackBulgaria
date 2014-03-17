# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-11---counting-substrings


# FUNCTIONS
def count_substrings(string, word):
    return string.count(word)


# main
def main():
    count_substrings("This is a test string", "is")
    count_substrings("babababa", "baba")
    count_substrings("Python is an awesome language to program in!", "o")
    count_substrings("We have nothing in common!", "really?")
    count_substrings("This is this and that is this", "this")


# PROGRAM RUN
if __name__ == '__main__':
    main()
