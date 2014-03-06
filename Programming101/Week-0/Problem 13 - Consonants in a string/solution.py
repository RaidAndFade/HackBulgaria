# Problem 13 - Consonants in a string
#
# Implement a function, called count_consonants(str) which returns the count of all consonants in the given string str. Count uppercase consonants as well!
#
# The consonants are bcdfghjklmnpqrstvwxz.
#
# Signature
#
# def count_consonants(str):
#     # Implementation
#
# Test examples
#
# >>> count_consonants("Python")
# 4
# >>> count_consonants("Theistareykjarbunga") #It's a volcano name!
# 11
# >>> count_consonants("grrrrgh!")
# 7
# >>> count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
# 44
# >>> count_consonants("A nice day to code!")
# 6

# FUNCTIONS
def count_consonants(string):
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z" ]
    numConsonants = 0

    for char in string.lower():
        if char in consonants:
            numConsonants += 1

    return numConsonants

# main
def main():
    print(count_consonants("Python"))
    print(count_consonants("Theistareykjarbunga"))
    print(count_consonants("grrrrgh!"))
    print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_consonants("A nice day to code!"))

# PROGRAM RUN
main()