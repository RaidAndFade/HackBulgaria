# Problem 4
#
# Given an integer, write a function,
# called is_prime(n) which returns True if n is a prime number.
# You should handle the case with negative numbers too.
#
# A primer number is a number, that is divisible only by 1 and itself.
#
# 1 is not considered to be a prime number. If you are curious why,
# find out here.
#
# Signature
#
#     def is_prime(n):
#         # implementation
#
# Test examples
#
#     >>> is_prime(1)
#     False
#     >>> is_prime(2)
#     True
#     >>> is_prime(8)
#     False
#     >>> is_prime(11)
#     True
#     >>> is_prime(-10)
#     False

# FUNCTIONS
def is_prime(number):
    if number <= 1:
        return False


    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            return False

        else:
            divisor += 1

    return True

# main
def main():
    inputN = int(input("Enter a number: "))

    print("Prime?", is_prime(inputN))

# PROGRAM RUN
main()