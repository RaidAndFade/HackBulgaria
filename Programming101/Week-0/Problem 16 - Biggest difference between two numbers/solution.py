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
    print(biggest_difference([1,2]))
    print(biggest_difference([1,2,3,4,5]))
    print(biggest_difference([-10, -9, -1]))
    print(biggest_difference(range(100)))

# PROGRAM RUN
main()