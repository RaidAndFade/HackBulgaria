# Problem 29 - Simplify fractions
#
# Implement a function, called simplify_fraction(fraction) 
# that takes a tuple of the form (nominator, denominator) and simplifies the fraction.
#
# The function should return the fraction in it's irreducible form.
#
# For example, a fraction 3/9 can be reduced by dividing both the nominator 
# and the denominator by 3. We end up with 1/3 which is irreducible.
#
# Signature
#
# def simplify_fraction(fraction):
#     # Implementation
# Test examples
#
# >>> simplify_fraction((3,9))
# (1,3)
# >>> simplify_fraction((1,7))
# (1,7)
# >>> simplify_fraction((4,10))
# (2,5)
# >>> simplify_fraction((63,462))
# (3,22)

# FUNCTIONS
def simplify_fraction(fractionTuple):
    nominator = fractionTuple[0]
    denominator = fractionTuple[1]

    def greatestCommonDiv(nominator, denominator):
        while denominator != 0:
            temp = denominator
            denominator = nominator % denominator
            nominator = temp

        return nominator

    greatest = greatestCommonDiv(nominator, denominator)
    nominator //= greatest
    denominator //= greatest

    return (nominator,denominator)

# main
def main():
    print(simplify_fraction((3,9)))
    print(simplify_fraction((1,7)))
    print(simplify_fraction((4,10)))
    print(simplify_fraction((63,462)))

# PROGRAM RUN
if __name__ == '__main__':
    main()