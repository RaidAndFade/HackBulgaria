# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-9---number-containing-all-digits


# FUNCTIONS
def contains_digits(number, list_digits):
    if len(list_digits) == 0:
        return False

    number = str(number)

    digits_found = 0

    for i in range(len(list_digits)):
            if str(list_digits[i]) in number:
                digits_found += 1

    if digits_found == len(list_digits):
        return True

    else:
        return False


# main
def main():
    contains_digits(402123, [0, 3, 4])
    contains_digits(666, [6, 4])
    contains_digits(123456789, [1, 2, 3, 0])
    contains_digits(456, [])


# PROGRAM RUN
if __name__ == '__main__':
    main()
