# Problem 11 - Counting substrings
#
# Implement a function, called count_substrings(haystack, needle) which returns the count of occurrences of the string needle in the string haystack.
#
# Don't count overlapped substings and take case into consideration! For overlapping substrings, check the "baba" example below.
#
# Signature
#
# def count_substrings(haystack, needle):
#     # Implementation
# Test examples
#
# >>> count_substrings("This is a test string", "is")
# 2
# >>> count_substrings("babababa", "baba")
# 2
# >>> count_substrings("Python is an awesome language to program in!", "o")
# 4
# >>> count_substrings("We have nothing in common!", "really?")
# 0
# >>> count_substrings("This is this and that is this", "this")  # "This" != "this"
# 2

# FUNCTIONS
def count_substring(string, word):
    return string.count(word)

# main
def main():
    inputString = str(input("Enter a string: "))
    inputSubString = str(input("Enter the substring you want to find: "))
    print("Times found:", count_substring(inputString, inputSubString))

# PROGRAM RUN
main()