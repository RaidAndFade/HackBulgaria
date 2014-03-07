# Problem 30 - Sort array of fractions

# Implement a function, called sort_fractions(fractions)
# where fractions is a list of tuples of the form (nominator, denominator).
# Both the nominator and the denominator are integers.
# The function should return the list, sorted in increasing order.

# Signature

# def sort_fractions(fractions):
#     # Implementation

# Test examples

#     >>> sort_fractions([(2, 3), (1, 2)])
#     [(1, 2), (2, 3)]
#     >>> sort_fractions([(2, 3), (1, 2), (1, 3)])
#     [(1, 3), (1, 2), (2, 3)]
#     >>> sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])
#     [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]

# IMPORTS
from collections import OrderedDict
from operator import itemgetter


# FUNCTIONS
def sort_fractions(fractions):
    fractionsDictionary = {}

    for fraction in fractions:
        fractionsDictionary[fraction] = fraction[0] / fraction[1]

    orderedFractionsDict = OrderedDict(sorted(fractionsDictionary.items(), key = itemgetter(1)))

    outputOrderedFractions = []
    for fraction in orderedFractionsDict:
        outputOrderedFractions.append(fraction)

    return outputOrderedFractions


# main
def main():
    print(sort_fractions([(2, 3), (1, 2)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))

# PROGRAM RUN
main()
