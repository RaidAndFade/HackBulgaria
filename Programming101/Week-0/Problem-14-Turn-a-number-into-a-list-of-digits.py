# Problem 14 - Turn a number into a list of digits
#
# Implement a function, called number_to_list(n) which takes an integer n and returns a list, containing the digits of n
#
# Signature
#
# def number_to_list(n):
#     # Implementation
# Test Examples
#
# >>> number_to_list(123)
# [1, 2, 3]
# >>> number_to_list(99999)
# [9, 9, 9, 9, 9]
# >>> number_to_list(123023)
# [1, 2, 3, 0, 2, 3]

# FUNCTIONS
def number_to_list(number):
    outputList = [ ]
    number = str(number)
    numDigits = len(number)

    for i in range(numDigits):
        # digit = number % 10
        outputList.append(int(number[i]))
        # number = number // 10

    return outputList

# main
def main():
    exNum1 = 123
    exNum2 = 99999
    exNum3 = 123023
    print("Num 1:", exNum1, "\nNum 2:", exNum2, "\nNum 3:", exNum3)
    print(number_to_list(exNum1))
    print(number_to_list(exNum2))
    print(number_to_list(exNum3))

# PROGRAM RUN
main()