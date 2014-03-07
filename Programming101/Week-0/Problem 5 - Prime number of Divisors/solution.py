# Problem 5
#
# Given an integer, write a function, called prime_number_of_divisors(n) which returns True if the number of divisors of n is a prime number. False otherwise.
#
# For example, the divisors of 8 are 1,2,4 and 8, a total of 4. 4 is not a prime. The divisors of 9 are 1,3 and 9, a total of 3, which is a prime number.
#
# Signature
#
#     def prime_number_of_divisors(n):
#         # Implementation
#
# Test examples
#
#     >>> prime_number_of_divisors(7)
#     True
#     >>> prime_number_of_divisors(8)
#     False
#     >>> prime_number_of_divisors(9)
#     True


# FUNCTIONS
# reuse from problem-4
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


def prime_number_of_divisors(number):
    numDivisors = 0

    for divisor in range(1, number+1):
        if number % divisor == 0:
            numDivisors += 1

    return is_prime(numDivisors)


# main
def main():
    print(prime_number_of_divisors(7))
    print(prime_number_of_divisors(8))
    print(prime_number_of_divisors(9))

# PROGRAM RUN
if __name__ == '__main__':
    main()
