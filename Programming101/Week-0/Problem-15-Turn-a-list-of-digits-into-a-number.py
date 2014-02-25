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
    exList1 = [ 1, 2, 3 ]
    exList2 = [ 9, 9, 9, 9, 9 ]
    exList3 = [ 1, 2, 3, 0, 2, 3 ]
    print("Ex list1", exList1)
    print("Ex list2", exList2)
    print("Ex list3", exList3)

    print("\nOutput as 1 number")
    print(list_to_number(exList1))
    print(list_to_number(exList2))
    print(list_to_number(exList3))
# PROGRAM RUN
main()