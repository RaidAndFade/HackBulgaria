# Problem F4 - Sum integers from file
#
# Implement a Python script, called sum_numbers.py,
# which takes one argument - a filename which has integers, separated by " "
#
# The script should print the sum of all integers in that file.
#
# Examples
#
# If we use the generated file from Problem 3:
#
# $ python sum_numbers.py numbers.txt
# 47372

# IMPORTS
from sys import argv, exit


# main
def main():
    if len(argv) == 1 or len(argv) > 2:
        exit("Error: Invalid number of arguments!")

    filename = argv[1]
    file = ""
    try:
        file = open(filename, "r")
    except IOError:
        exit("Error: File not found!")

    outputSum = 0
    for line in file:
        outputSum += int(line)

    print(outputSum)

# PROGRAM RUN
if __name__ == '__main__':
    main()
