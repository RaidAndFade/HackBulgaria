# Problem 28 - Word from a^nb^n
#
# Implement a function, called is_an_bn(word) that checks if the given word is
# from the a^nb^n for n>=0 language.
# Here, a^n means a to the power of n - repeat the character "a" n times.
#
# Lets see few words from this language:
#
# for n = 0, this is the empty word ""
# for n = 1, this is the word "ab"
# for n = 2, this is the word "aabb"
# for n = 3, this is the word "aaabbb"
# and so on - first, you repeat the character "a" n times,
# and after this - repeat "b" n times
#
# The function should return True
# if the given word is from ```a^nb^n for n>=0" for some n.
#
# Signature
#
# def is_an_bn(word):
#     # Implementation
# Test examples
#
# >>> is_an_bn("")
# True
# >>> is_an_bn("rado")
# False
# >>> is_an_bn("aaabb")
# False
# >>> is_an_bn("aaabbb")
# True
# >>> is_an_bn("aabbaabb")
# False
# >>> is_an_bn("bbbaaa")
# False
# >>> is_an_bn("aaaaabbbbb")
# True

# FUNCTIONS
def is_an_bn(string):
    middle = len(string) // 2
    firstHalf = string[:middle]
    secondHalf = string[middle:]

    if len(string) == 1 or string == "":
        return True

    if firstHalf[0] == "a" and not "b" in firstHalf:
        if secondHalf[0] == "b" and not "a" in secondHalf:
            if firstHalf.count("a") == secondHalf.count("b"):
                return True

    return False

# main
def main():
    print(is_an_bn(""))
    print(is_an_bn("rado"))
    print(is_an_bn("aaabb"))
    print(is_an_bn("aaabbb"))
    print(is_an_bn("aabbaabb"))
    print(is_an_bn("bbbaaa"))
    print(is_an_bn("aaaaabbbbb"))

# PROGRAM RUN
if __name__ == '__main__':
    main()