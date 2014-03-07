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


# FUNCTIONS
def sevens_in_a_row(list, lenSevens):
    if 7 not in list:
        return False

    rowSevens = 1
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            rowSevens += 1

    if rowSevens == lenSevens:
        return True

    else:
        return False


# main
def main():
    print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
    print(sevens_in_a_row([1, 7, 1, 7, 7], 4))
    print(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))
    print(sevens_in_a_row([7, 2, 1, 6, 2], 1))

# PROGRAM RUN
if __name__ == '__main__':
    main()
