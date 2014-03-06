# Problem 15 - Turn a list of digits into a number
#
# Implement a function, called list_to_number(digits) which takes a list of digits (integers) and returns the number, containing those digits.
#
# Signature
#
# def list_to_number(digits):
#     # Implementation
# Test Examples
#
# >>> list_to_number([1,2,3])
# 123
# >>> list_to_number([9,9,9,9,9])
# 99999
# >>> list_to_number([1,2,3,0,2,3])
# 123023

# FUNCTIONS
def list_to_number(list):
    outputNumber = ""

    for i in range(len(list)):
        outputNumber += str(list[i])

    return outputNumber
    
# main
def main():
    print(list_to_number([1,2,3]))
    print(list_to_number([9,9,9,9,9]))
    print(list_to_number([1,2,3,0,2,3]))

# PROGRAM RUN
main()
