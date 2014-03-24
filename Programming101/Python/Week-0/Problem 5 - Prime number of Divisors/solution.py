# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-5---check-if-a-number-has-a-prime-number-of-divisors


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
    prime_number_of_divisors(7)
    prime_number_of_divisors(8)
    prime_number_of_divisors(9)


# PROGRAM RUN
if __name__ == '__main__':
    main()
