# Problem 23 - Count words
#
# Given a list of strings, implement a function, called count_words(arr) which returns a dictionary of the following kind:
#
# { "word" : count }
# Where count is the count of occurrences of the word in the list arr.
#
# The result should be sorted by keys alphabetically.
#
# Signature
#
# def count_words(arr):
#     # Implementation
# Test examples
#
# >>> count_words(["apple", "banana", "apple", "pie"])
# {'apple': 2, 'pie': 1, 'banana': 1}
# >>> count_words(["python", "python", "python", "ruby"])
# {'ruby': 1, 'python': 3}

# FUNCTIONS
def count_words(list):
    outputDict = { }

    for i in range(len(list)):
         outputDict[list[i]] = list.count(list[i])

    return outputDict

# main
def main():
    print(count_words(["apple", "banana", "apple", "pie"]))
    print(count_words(["python", "python", "python", "ruby"]))
    
# PROGRAM RUN
main()