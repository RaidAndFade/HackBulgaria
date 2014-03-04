# Problem 2
#
# Given an array of integers, write a function, called sum_of_min_and_max(arr), that calculates and returns the sum of the largest and the smallest integers in the array.
#
# Don't bother for the case when the array is empty.
#
# Signature
#
#     def sum_of_min_and_max(arr):
#         # implementation
#
# Test examples
#
#     >>> sum_of_min_and_max([1,2,3,4,5,6,8,9])
#     10
#     >>> sum_of_min_and_max([-10,5,10,100])
#     90
#     >>> sum_of_min_and_max([1])
#     2

# FUNCTIONS
def sum_of_min_and_max(list):
    if len(list) > 0:
        minList = min(list)
        maxList = max(list)

        # too easy?
        return minList + maxList

    else:
        print("List is empty")
        return


# main
def main():
    exampleList = [ 5, 6, 7, 8, 10, 15, -5, -2, 1]

    print("Given list")
    for element in exampleList:
        print(element, end = " ")

    print() # new line
    print("Min of list:", min(exampleList))
    print("Max of list:", max(exampleList))
    print() # new line
    print("Sum of min and max of list:", sum_of_min_and_max(exampleList))

# PROGRAM RUN
main()