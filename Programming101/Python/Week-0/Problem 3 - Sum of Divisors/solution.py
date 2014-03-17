# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-3---sum-all-divisors-of-an-integer


# FUNCTIONS
def sum_of_divisors(number):
    output_sum = 0

    for divisor in range(1, number+1):
        if number % divisor == 0:
            output_sum += divisor
    return output_sum


# main
def main():
    sum_of_divisors(8)
    sum_of_divisors(7)
    sum_of_divisors(1)
    sum_of_divisors(1000)


# PROGRAM RUN
if __name__ == '__main__':
    main()
