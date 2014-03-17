# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-21---integer-prime-factorization


# FUNCTIONS
def prime_factorization(number):
    primes = []

    for divisor in range(2, number + 1):
        divisorCount = 0
        while number % divisor == 0:
            divisorCount += 1
            number //= divisor
            if not number % divisor == 0:
                tuple = (divisor, divisorCount)
                primes.append(tuple)
    return primes


# main
def main():
    prime_factorization(10)
    prime_factorization(14)
    prime_factorization(356)
    prime_factorization(89)
    prime_factorization(1000)


# PROGRAM RUN
if __name__ == '__main__':
    main()
