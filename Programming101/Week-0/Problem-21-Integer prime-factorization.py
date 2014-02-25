# Problem 21 - Integer prime factorization
#
# Given an integer n, we can factor it in the following form:
#
# n = p1^a1 * p2^a2 * ... * pn^an
# Where each p is a prime number and each a is an integer and p^a means p to the power of a.
#
# This is called prime factorization.
#
# Lets see few examples
#
# 10 = 2^1 * 5^1 25 = 5^2 356 = 2^2 * 89 ^ 1
# Implement a function, called prime_factorization(n) which takes an integer and returns a list of tuples (pi, ai), which is the result of the factorization.
#
# The list should be sorted in increasing order of the prime numbers.
#
# Signature
#
# def prime_factorization(n):
#     # Implementation
# Test examples
#
# >>> prime_factorization(10)
# [(2, 1), (5, 1)] # This is 2^1 * 5^1
# >>> prime_factorization(14)
# [(2, 1), (7, 1)]
# >>> prime_factorization(356)
# [(2, 2), (89, 1)]
# >>> prime_factorization(89)
# [(89, 1)] # 89 is a prime number
# >>> prime_factorization(1000)
# [(2, 3), (5, 3)]

# FUNCTIONS
def prime_factorization(number):
    primes = [ ]

    number = int(number)

    for divisor in range(2, number + 1):
        while number % divisor == 0:
            primes.append(divisor)
            primes.append(primes.count(divisor))
            number //= divisor


    return tuple(primes)


# main
def main():
    inputNumber = int(input("Enter a number: "))
    print(prime_factorization(inputNumber))

# PROGRAM RUN
main()