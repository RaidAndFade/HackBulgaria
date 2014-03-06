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
    print(sum_of_min_and_max([1,2,3,4,5,6,8,9]))
    print(sum_of_min_and_max([-10,5,10,100]))
    print(sum_of_min_and_max([1]))

# PROGRAM RUN
main()