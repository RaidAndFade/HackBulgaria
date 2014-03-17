# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-29---simplify-fractions


# FUNCTIONS
def simplify_fraction(fractionTuple):
    nominator = fractionTuple[0]
    denominator = fractionTuple[1]

    def greatest_common_divisor(nominator, denominator):
        while denominator != 0:
            temp = denominator
            denominator = nominator % denominator
            nominator = temp
        return nominator

    greatest = greatest_common_divisor(nominator, denominator)
    nominator //= greatest
    denominator //= greatest
    return (nominator, denominator)


# main
def main():
    simplify_fraction((3, 9))
    simplify_fraction((1, 7))
    simplify_fraction((4, 10))
    simplify_fraction((63, 462))


# PROGRAM RUN
if __name__ == '__main__':
    main()
