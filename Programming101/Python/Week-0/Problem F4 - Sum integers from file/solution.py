# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems3.md#problem-f4---sum-integers-from-file


# IMPORTS
from sys import argv, exit


# FUNCTIONS
def sum_integers_from_file(filename):
    try:
        opened_file = open(filename, "r")
    except IOError:
        exit("Error: File not found!")

    output_sum = 0
    for line in opened_file:
        numbers = line.split()
        for number in numbers:
            output_sum += int(number)
    opened_file.close()
    return output_sum


# main
def main():
    if len(argv) == 1 or len(argv) > 2:
        exit("Error: Invalid number of arguments!")

    filename = argv[1]
    print(sum_integers_from_file(filename))


# PROGRAM RUN
if __name__ == '__main__':
    main()
