# Problem 32 - Goldbach Conjecture
# Implement a function, called goldbach(n) which returns a list of tupples,
# that is the goldbach conjecture for the given number n
#
# The Goldbach Conjecture states:
# Every even integer greater than 2 can be expressed as the sum of two primes.
# Keep in mind that there can be more than one combination of two primes,
# that sums up to the given number.
#
# The result should be sorted by the first item in the tuple.
#
# For example:
#
#     4 = 2 + 2
#     6 = 3 + 3
#     8 = 3 + 5
#     10 = 3 + 7 = 5 + 5
#     100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53
#
# Signature
#
#     def goldbach(n):
#         # Implementation
#
# Test examples
#
#     >>> goldbach(4)
#     [(2,2)]
#     >>> goldbach(6)
#     [(3,3)]
#     >>> goldbach(8)
#     [(3,5)]
#     >>> goldbach(10)
#     [(3,7), (5,5)]
#     >>> goldbach(100)
#     [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]

# IMPORTS

# FUNCTIONS
# reused from Problem-4-Is-Prime
def is_prime(number):
    if number <= 1:
        return False


    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            return False

        else:
            divisor += 1

    return True

def goldbach(n):
    goldbach = []

    for number in range(n):
        if is_prime(number) == True:
            if is_prime(n - number) == True:
                goldbach.append((number, n - number))

    for current in goldbach:
        for following in goldbach:
            if current[0] == following[0]:
                if goldbach.index(current) != goldbach.index(following):
                    del goldbach[goldbach.index(following)]
    return goldbach

# main
def main():
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(8))
    print(goldbach(10))
    print(goldbach(100))

# PROGRAM RUN
if __name__ == "__main__":
    main()
