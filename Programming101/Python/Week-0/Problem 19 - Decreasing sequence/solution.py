# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-19---descreasing-sequence


# FUNCTIONS
def is_decreasing(list):
    for i in range(len(list) - 1):
        if not list[i] > list[i + 1]:
            return False
    return True


# main
def main():
    is_decreasing([5, 4, 3, 2, 1])
    is_decreasing([1, 2, 3])
    is_decreasing([100, 50, 20])
    is_decreasing([1, 1, 1, 1])


# PROGRAM RUN
if __name__ == '__main__':
    main()
