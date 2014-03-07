# Problem 24 - Unique words
#
# Implement a function, called unique_words_count(arr)
# which returns the unique words count in arr.
#
# arr is a list of strings.
#
# Signature
#
# def unique_words_count(arr):
#     # Implementation
# Test examples
#
# >>> unique_words_count(["apple", "banana", "apple", "pie"])
# 3
# >>> unique_words_count(["python", "python", "python", "ruby"])
# 2
# >>> unique_words_count(["HELLO!"] * 10)
# 1

# FUNCTIONS
def unique_words_count(list):
    uniqueList = []

    for i in range(len(list)):
        if list[i] not in uniqueList:
            uniqueList.append(list[i])

    return len(uniqueList)

# main
def main():
    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(unique_words_count(["python", "python", "python", "ruby"]))
    print(unique_words_count(["HELLO!"] * 10))

# PROGRAM RUN
if __name__ == '__main__':
    main()