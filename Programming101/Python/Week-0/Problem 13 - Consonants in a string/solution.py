# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-13---consonants-in-a-string


# FUNCTIONS
def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxz"
    numConsonants = 0

    for char in string.lower():
        if char in consonants:
            numConsonants += 1

    return numConsonants


# main
def main():
    count_consonants("Python")
    count_consonants("Theistareykjarbunga")
    count_consonants("grrrrgh!")
    count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
    count_consonants("A nice day to code!")


# PROGRAM RUN
if __name__ == '__main__':
    main()
