# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-315---is-member-of-nth-fibonacci-lists


# FUNCTIONS
def member_of_nth_fib_lists(listA, listB, needle):
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
    member_of_nth_fib_lists([1, 2], [3, 4], [5, 6])
    member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4])
    member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2])
    member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7])


# PROGRAM RUN
if __name__ == "__main__":
    main()
