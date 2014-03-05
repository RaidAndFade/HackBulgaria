# Problem 31 - Fibonacci lists
# Implement a function, called nth_fib_lists(listA, listB, n)
# which takes two list of integers as listA and listB and returns
# the n-th member of the fibonacci sequence, that is created by the
# following algorithm:
#     for n = 1, it's listA
#     for n = 2, it's listB
#     for n = 3, it's listA + listB where + is list concatenation
#     and so on, just like a fibonacci
#
# Signature
#
#     def nth_fib_lists(listA, listB, n)
#
# Test examples
#
#     >>> nth_fib_lists([1], [2], 1)
#     [1]
#     >>> nth_fib_lists([1], [2], 2)
#     [2]
#     >>> nth_fib_lists([1, 2], [1, 3], 3)
#     [1, 2, 1, 3]
#     >>> nth_fib_lists([], [1, 2, 3], 4)
#     [1, 2, 3, 1, 2, 3]
#     >>> nth_fib_lists([], [], 100)
#     []

# IMPORTS

# FUNCTIONS
def nth_fib_lists(listA, listB, n):
    if n < 3:
        return 1

    position = 2 # 3 in list
    while position < len(n) + 1:
        following = listA + listB
        listA = listB
        listB = following
        position += 1

        if listB == n:
            return True

    return False

# main
def main():
    print("\nExpected: [1]")
    print("Output:", nth_fib_lists([1], [2], 1))

    print("\nExpected: [2]")
    print("Output:", nth_fib_lists([1], [2], 2))

    print("\nExpected: [1, 2, 1, 3]")
    print("Output:", nth_fib_lists([1, 2], [1, 3], 3))

    print("\nExpected: [1, 2, 3, 1, 2, 3]")
    print("Output:", nth_fib_lists([], [1, 2, 3], 4))

    print("\nExpected: []")
    print("Output:", nth_fib_lists([], [], 100))

# PROGRAM RUN
if __name__ == "__main__":
    main()
