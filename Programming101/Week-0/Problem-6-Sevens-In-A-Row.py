# Problem 6
#
# Write a function, called sevens_in_a_row(arr, n),
# which takes an array of integers arr and a number n > 0
#
# The function returns True, if there are n consecutive sevens in arr
#
# For example, if arr is [10,8,7,6,7,7,7,20,-7] and n is 3,
# the function should return True.
# Otherwise, it returns False
#
# Signature
#
#     def sevens_in_a_row(arr, n)
#
# Test examples
#
#     >>> sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3)
#     True
#     >>> sevens_in_a_row([1,7,1,7,7], 4)
#     False
#     >>> sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3)
#     True
#     >>> sevens_in_a_row([7,2,1,6,2], 1)
#     True

# IMPORTS
from sys import exit

# FUNCTIONS
def sevens_in_a_row(list, lenSevens):
    if list.count(7) >= lenSevens:
        return True

    return False

def inputList():
    print("Enter numbers. Type (S) to stop.")
    list = []
    userInput = ""

    while userInput.upper() != "S":
        userInput = input()

        if userInput.isdigit():
            list.append(int(userInput))

    return list

# main
def main():
    list = inputList()

    inputLenSevens = int(input("How many sevens in a row do you want to find: "))

    print("%d sevens in a row? %s" % (inputLenSevens, sevens_in_a_row(list, inputLenSevens)))


# PROGRAM RUN
main()