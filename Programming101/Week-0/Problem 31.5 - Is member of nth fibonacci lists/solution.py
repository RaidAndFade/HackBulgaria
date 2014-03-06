# Problem 31.5 - Is member of nth fibonacci lists
# Implement a function, called member_of_nth_fib_lists(listA, listB, needle)
# which checks if needle is a part of the fibonacci sequence,
# created by listA and listB for the first two elements.
#
# Signature
#
#     def member_of_nth_fib_lists(listA, listB, needle):
#         # Implement
#
# Test examples
#
#     >>> member_of_nth_fib_lists([1, 2], [3, 4], [5, 6])
#     False
#     >>> member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4])
#     True
#     >>> member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2])
#     True
#     >>> member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7])
#     False

# FUNCTIONS
def member_of_nth_fib_lists(listA, listB, needle):
    if needle < 3:
        return 1

    # 3rd element
    position = 2
    while position < len(needle) + 1:
        following = listA + listB
        listA = listB
        listB = following
        position += 1

        if listB == needle:
            return True

    return False

# main
def main():
    print(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
    print(member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
    print(member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))
    print(member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))

# PROGRAM RUN
if __name__ == "__main__":
    main()
