# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-30---sort-array-of-fractions


# IMPORTS
from collections import OrderedDict
from operator import itemgetter


# FUNCTIONS
def sort_fractions(fractions):
    fractionsDictionary = {}

    for fraction in fractions:
        fractionsDictionary[fraction] = fraction[0] / fraction[1]

    orderedFractionsDict = OrderedDict(sorted(fractionsDictionary.items(), key=itemgetter(1)))
    outputOrderedFractions = []
    for fraction in orderedFractionsDict:
        outputOrderedFractions.append(fraction)

    return outputOrderedFractions


# main
def main():
    sort_fractions([(2, 3), (1, 2)])
    sort_fractions([(2, 3), (1, 2), (1, 3)])
    sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])

# PROGRAM RUN
main()
