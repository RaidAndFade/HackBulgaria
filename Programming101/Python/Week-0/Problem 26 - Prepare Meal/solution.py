# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-26---spam-and-eggs


# FUNCTIONS
def prepare_meal(number):
    output = []
    while number % 3 == 0:
        output.append("spam")
        number //= 3
    if number % 5 == 0:
        if output:
            output.append("and")
        output.append("eggs")
    return " ".join(output)


# main
def main():
    prepare_meal(5)
    prepare_meal(3)
    prepare_meal(27)
    prepare_meal(15)
    prepare_meal(45)
    prepare_meal(7)


# PROGRAM RUN
if __name__ == '__main__':
    main()
