# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-31---fibonacci-lists


# FUNCTIONS
def nth_fib_lists(listA, listB, n):
    position = 2
    while position < n + 1:
        following = listA + listB
        listA = listB
        listB = following
        position += 1

    return listA


# main
def main():
    nth_fib_lists([1], [2], 1)
    nth_fib_lists([1], [2], 2)
    nth_fib_lists([1, 2], [1, 3], 3)
    nth_fib_lists([], [1, 2, 3], 4)
    nth_fib_lists([], [], 100)


# PROGRAM RUN
if __name__ == "__main__":
    main()
