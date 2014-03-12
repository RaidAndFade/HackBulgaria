# Problem 0 - Get the things going!

# So, to do something very simple, go to calculator.py
# and add two more functions:

# integer_division(a, b)
# modulo(a, b)
# Add two more tests for the new functions and make
# sure everything is running!


# FUNCTIONS
def integer_divison(a, b):
    return a // b


def modulo(a, b):
    return a % b


# main
def main():
    integer_divison(5, 6)
    integer_divison(10, 2)
    integer_divison(2, 5)
    modulo(5, 6)
    modulo(10, 2)
    modulo(2, 5)


# PROGRAM RUN
if __name__ == "__main__":
    main()
