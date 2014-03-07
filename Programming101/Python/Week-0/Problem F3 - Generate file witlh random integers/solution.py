# Problem F3 - Generate file with random integers
#
# Implement a Python script, called generate_numbers.py
# that takes two arguments - a filename and an integer n.
#
# The script should create a file with the filename
# and print n random integers, separated by " "
#
# For random integers, you can use:
#
# from random import randint
# print(randint(1, 1000))
#
# Boilerplate
#
# # generate_numbers.py
# import sys
# from random import randint
#
#
# def main():
#     pass
#
# if __name__ == '__main__':
#     main()
# Examples
#
# $ python generate_numbers.py numbers.txt 100
# $ cat numbers.txt
# 612 453 555 922 120 840 173 98 994 461 392 739 982 598 610 205 13 604 304 591 830 313 534 47


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
