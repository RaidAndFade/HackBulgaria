# Problem F3 - Generate file with random integers
# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems3.md#problem-f3---generate-file-with-random-integers


# IMPORTS
from random import randint
from sys import argv, exit


# main
def main():
    if len(argv) < 3:
        exit("Error: Not enough arguments given!")

    filename = argv[1]
    generate_N_numbers = 0
    try:
        generate_N_numbers = int(argv[2])
    except ValueError:
        exit("Error: Make sure you provide numbers as 3rd argument!")

    file = open(filename, "w")
    for i in range(generate_N_numbers):
        rand_number = randint(0, 1001)
        file.write(str(rand_number))
        file.write("\n")
    file.close()


# PROGRAM RUN
if __name__ == '__main__':
    main()
