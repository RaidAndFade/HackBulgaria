# Problem 12 - Vowels in a string
#
# Implement a function, called count_vowels(str) which returns the count of all vowels in the given string str. Count uppercase vowels as well!
#
# The vowels are aeiouy.
#
# Signature
#
# def count_vowels(str):
#     # Implementation
# Test examples
#
# >>> count_vowels("Python")
# 2
# >>> count_vowels("Theistareykjarbunga") #It's a volcano name!
# 8
# >>> count_vowels("grrrrgh!")
# 0
# >>> count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
# 22
# >>> count_vowels("A nice day to code!")
# 8

# FUNCTIONS
def count_vowels(string):
    vowels = [ "a", "e", "i", "o", "u", "y" ]

    numVowels = 0

    for i in range(len(string)):
        if string[i] in vowels:
            numVowels += 1

    return numVowels

# main
def main():
    print(count_vowels("Python"))
    print(count_vowels("Theistareykjarbunga"))
    print(count_vowels("grrrrgh!"))
    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_vowels("A nice day to code!"))

# PROGRAM RUN
main()