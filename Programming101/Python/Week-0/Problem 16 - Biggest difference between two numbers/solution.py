# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-16---biggest-difference-between-two-numbers

# FUNCTIONS


def biggest_difference(list):
    minElement = min(list)
    maxElement = max(list)
    if maxElement > minElement:
        return minElement - maxElement
    else:
        return maxElement - minElement


# main
def main():
    biggest_difference([1, 2])
    biggest_difference([1, 2, 3, 4, 5])
    biggest_difference([-10, -9, -1])
    biggest_difference(range(100))


# PROGRAM RUN
if __name__ == '__main__':
    main()
