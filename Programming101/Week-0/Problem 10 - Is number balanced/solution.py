# Problem 10 - Is number balanced?
#
# A number is called balanced, if we take the middle of it and the sum of the left and right parts are equal.
#
# For example, the number 1238033 is balanced, bacause it has a left part, equal to 123, and right part, equal ot 033.
#
# We have : 1 + 2 + 3 = 0 + 3 + 3 = 6
#
# A number with only one digit is always balanced.
#
# Implement a function, called is_number_balanced(n) which checks if the given number is balanced.
#
# Signature
#
# def is_number_balanced(n):
#     # Implementation
# Test examples
#
# >>> is_number_balanced(9)
# True
# >>> is_number_balanced(11)
# True
# >>> is_number_balanced(13)
# False
# >>> is_number_balanced(121)
# True
# >>> is_number_balanced(4518)
# True
# >>> is_number_balanced(28471)
# False
# >>> is_number_balanced(1238033)
# True

# FUNCTIONS
def is_number_balanced(number):
    str_number = str(number)
    numDigits = 1
    while number > 10:
        numDigits += 1
        number //= 10

    firstHalf = ""
    secondHalf = ""

    if numDigits % 2 == 0:
        middle = numDigits // 2
        firstHalf = str_number[:middle]
        secondHalf = str_number[middle:]
    else:
        middle = numDigits // 2 + 1
        firstHalf = str_number[:middle]
        secondHalf = str_number[middle-1:]

    firstHalfSum = 0
    secondHalfSum = 0

    for digit in firstHalf:
        firstHalfSum += int(digit)
    for digit in secondHalf:
        secondHalfSum += int(digit)

    if firstHalfSum == secondHalfSum:
        return True

    else:
        return False

# main
def main():
    print(is_number_balanced(9))
    print(is_number_balanced(11))
    print(is_number_balanced(13))
    print(is_number_balanced(121))
    print(is_number_balanced(4518))
    print(is_number_balanced(28471))
    print(is_number_balanced(1238033))

# PROGRAM RUN
main()