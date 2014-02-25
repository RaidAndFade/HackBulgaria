# Problem 16 - Biggest difference between two numbers
#
# Implement a function, called biggest_difference(arr), which takes an array of integers and returns the biggest difference between any two numbers from the array.
#
# For every two elements from the array a and b, we are looking for the minimum of a - b or b - a
#
# Signature
#
# def biggest_difference(arr):
#     # Implementation
# Test examples
#
# >>> biggest_difference([1,2])
# -1
# >>> biggest_difference([1,2,3,4,5])
# -4
# >>> biggest_difference([-10, -9, -1])
# -9
# >>> biggest_difference(range(100))
# -99

# FUNCTIONS
def biggest_difference(list):
    minElement = min(list)
    maxElement = max(list)

    return maxElement - minElement

# main
def main():
    exList1 = [1,2]
    exList2 = [1,2,3,4,5]
    exList3 = [-10, -9, -1]
    exList4 = list(range(100))

    print(exList1)
    print("Biggest difference:", biggest_difference(exList1))
    print(exList2)
    print("Biggest difference:", biggest_difference(exList2))
    print(exList3)
    print("Biggest difference:", biggest_difference(exList3))
    print(exList4)
    print("Biggest difference:", biggest_difference(exList4))

# PROGRAM RUN
main()