# Problem 3
#
# Given an integer, write a function,
# called sum_of_divisors(n) that calculates
#  the sum of all divisors of n.
#
# For example, the divisors of 8 are 1,2,4 and 8
# and 1 + 2 + 4 + 8 = 15 The divisors of 7 are 1 and 7,
#  which makes the sum = 8
#
# Signature
#
#     def sum_of_divisors(n):
#         # implementation
#
# Test examples
#
#     >>> sum_of_divisors(8)
#     15
#     >>> sum_of_divisors(7)
#     8
#     >>> sum_of_divisors(1)
#     1
#     >>> sum_of_divisors(1000)
#     2340

# FUNCTIONS
def sum_of_divisors(number):
    outputSum = 0

    for divisor in range(1, number+1):
        if number % divisor == 0:
            outputSum += divisor

    return outputSum


# main
def main():
    inputN = int(input("Enter a number: "))

    print("Sum of divisors:", sum_of_divisors(inputN))

# PROGRAM RUN
main()