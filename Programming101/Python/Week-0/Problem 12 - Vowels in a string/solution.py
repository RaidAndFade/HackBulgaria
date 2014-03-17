# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-12---vowels-in-a-string


# FUNCTIONS
def count_vowels(string):
    vowels = "aeiouy"
    numVowels = 0

    for char in string.lower():
        if char in vowels:
            numVowels += 1
    return numVowels


# main
def main():
    count_vowels("Python")
    count_vowels("Theistareykjarbunga")
    count_vowels("grrrrgh!")
    count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
    count_vowels("A nice day to code!")


# PROGRAM RUN
if __name__ == '__main__':
    main()
