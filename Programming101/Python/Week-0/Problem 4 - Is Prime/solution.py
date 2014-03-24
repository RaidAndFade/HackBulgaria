# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-4---check-if-integer-is-prime


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
    is_prime(1)
    is_prime(2)
    is_prime(8)
    is_prime(11)
    is_prime(-10)


# PROGRAM RUN
if __name__ == '__main__':
    main()
