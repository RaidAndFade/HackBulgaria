# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-8---number-containing-a-single-digit


# FUNCTIONS
def contains_digit(number, digit):
    number = str(number)
    digit = str(digit)

    if digit in number:
        return True

    else:
        return False


# main
def main():
    contains_digit(123, 4)
    contains_digit(42, 2)
    contains_digit(1000, 0)
    contains_digit(12346789, 5)


# PROGRAM RUN
if __name__ == '__main__':
    main()
