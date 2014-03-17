# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-28---word-from-anbn


# FUNCTIONS
def is_an_bn(string):
    middle = len(string) // 2
    first_half = string[:middle]
    second_half = string[middle:]

    if len(string) == 1 or string == "":
        return True

    if first_half[0] == "a" and not "b" in first_half:
        if second_half[0] == "b" and not "a" in second_half:
            if first_half.count("a") == second_half.count("b"):
                return True

    return False


# main
def main():
    is_an_bn("")
    is_an_bn("rado")
    is_an_bn("aaabb")
    is_an_bn("aaabbb")
    is_an_bn("aabbaabb")
    is_an_bn("bbbaaa")
    is_an_bn("aaaaabbbbb")


# PROGRAM RUN
if __name__ == '__main__':
    main()
