# Problem 1
#
# Given an integer, write a function,
# called sum_of_digits(n) that calculates
# the sum of the digits of n.
#
# If a negative number is given, the function
# should work as if it was positive.
#
# For example, if n is 1325132435356, the digit's sum is 43.
#  If n is -10, the sum is 1 + 0 = 1
#
# Keep in mind that in Python, there is a special operator
# for integer division:
#
#     >>> 5 / 2
#     2.5
#     >>> 5 // 2
#     2
#
# Signature
#
#     def sum_of_digits(n):
#         # implementation
#
# Test examples
#
#     >>> sum_of_digits(1325132435356)
#     43
#     >>> sum_of_digits(123)
#     6
#     >>> sum_of_digits(6)
#     6
#     >>> sum_of_digits(-10)
#     1

# FUNCTIONS
def sum_of_digits(number):
    outputSum = 0

    if number < 1:
        number *= -1

    numDigits = len(str(number))

    for i in range(numDigits):
        digit = number % 10
        outputSum += digit
        number = number // 10

    return outputSum

# main
def main():
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(123))
    print(sum_of_digits(6))
    print(sum_of_digits(-10))

# PROGRAM RUN
main()