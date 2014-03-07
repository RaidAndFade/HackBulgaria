# Problem 9 - Number containing all digits?
#
# Implement a function, called contains_digits(number, digits),
# where digits is a list of integers and a number is an integer.
#
# The function should return True if all digits are contained by number
#
# Signature
#
# def contains_digits(number, digits):
# Implementation
# Test examples
#
# >>> contains_digits(402123, [0, 3, 4])
# True
# >>> contains_digits(666, [6,4])
# False
# >>> contains_digits(123456789, [1,2,3,0])
# False
# >>> contains_digits(456, [])
# False


# FUNCTIONS
def contains_digits(number, listDigits):
    if len(listDigits) == 0:
        return False

    number = str(number)

    digitsFound = 0

    for i in range(len(listDigits)):
            if str(listDigits[i]) in number:
                digitsFound += 1

    if digitsFound == len(listDigits):
        return True

    else:
        return False


# main
def main():
    print(contains_digits(402123, [0, 3, 4]))
    print(contains_digits(666, [6, 4]))
    print(contains_digits(123456789, [1, 2, 3, 0]))
    print(contains_digits(456, []))

# PROGRAM RUN
if __name__ == '__main__':
    main()
