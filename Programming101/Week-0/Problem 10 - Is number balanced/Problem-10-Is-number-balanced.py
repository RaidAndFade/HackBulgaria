# Problem 10 - Is number balanced?
#
# A number is called balanced, if we take the middle of it and the sum of the left and right parts are equal.
#
# For example, the number 1238033 is balanced, bacause it has a left part, equal to 123, and right part, equal ot 033.
#
# We have : 1 + 2 + 3 = 0 + 3 + 3 = 6
#
# A number with only one digit is always balanced.
#
# Implement a function, called is_number_balanced(n) which checks if the given number is balanced.
#
# Signature
#
# def is_number_balanced(n):
#     # Implementation
# Test examples
#
# >>> is_number_balanced(9)
# True
# >>> is_number_balanced(11)
# True
# >>> is_number_balanced(13)
# False
# >>> is_number_balanced(121)
# True
# >>> is_number_balanced(4518)
# True
# >>> is_number_balanced(28471)
# False
# >>> is_number_balanced(1238033)
# True

# FUNCTIONS
def is_number_balanced(number):
    number = str(number)
    middle = len(number) // 2
    firstHalf = number[:middle]
    secondHalf = number[middle:]
    lenFirstHalf = len(firstHalf)
    lenSecondHalf = len(secondHalf)

    firstHalfSum = 0
    secondHalfSum = 0

    for i in range(lenFirstHalf):
        firstHalfSum += int(firstHalf[i])

    for i in range(lenSecondHalf):
        secondHalfSum += int(secondHalf[i])

    if firstHalfSum == secondHalfSum:
        return True

    else:
        return False

# main
def main():
    inputNumber = int(input("Enter a number: "))
    print("Is %d balanced:" % inputNumber, end = " ")
    print(is_number_balanced(inputNumber))

# PROGRAM RUN
main()