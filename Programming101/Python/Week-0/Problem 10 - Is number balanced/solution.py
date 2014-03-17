# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-10---is-number-balanced


# FUNCTIONS
def is_number_balanced(number):
    str_number = str(number)
    numDigits = 1
    while number > 10:
        numDigits += 1
        number //= 10

    first_half = ""
    second_half = ""

    if numDigits % 2 == 0:
        middle = numDigits // 2
        first_half = str_number[:middle]
        second_half = str_number[middle:]
    else:
        middle = numDigits // 2 + 1
        first_half = str_number[:middle]
        second_half = str_number[middle-1:]

    first_halfSum = 0
    second_halfSum = 0

    for digit in first_half:
        first_halfSum += int(digit)
    for digit in second_half:
        second_halfSum += int(digit)

    if first_halfSum == second_halfSum:
        return True

    else:
        return False


# main
def main():
    is_number_balanced(9)
    is_number_balanced(11)
    is_number_balanced(13)
    is_number_balanced(121)
    is_number_balanced(4518)
    is_number_balanced(28471)
    is_number_balanced(1238033)


# PROGRAM RUN
if __name__ == '__main__':
    main()
