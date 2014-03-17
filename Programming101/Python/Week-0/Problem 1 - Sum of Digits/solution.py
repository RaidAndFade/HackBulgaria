# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-0---n-th-fibonacci


# FUNCTIONS
def sum_of_digits(number):
    if number < 1:
        number *= -1
    num_digits = len(str(number))

    output_sum = 0
    for i in range(num_digits):
        digit = number % 10
        output_sum += digit
        number = number // 10
    return output_sum


# main
def main():
    sum_of_digits(1325132435356)
    sum_of_digits(123)
    sum_of_digits(6)
    sum_of_digits(-10)

# PROGRAM RUN
if __name__ == '__main__':
    main()
