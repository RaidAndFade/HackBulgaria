# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-2---sum-the-minimum-and-maximum-elements


# FUNCTIONS
def sum_of_min_and_max(list):
    if len(list) > 0:
        min_element = min(list)
        max_element = max(list)
        # too easy?
        return min_element + max_element
    else:
        # List is empty
        return False


# main
def main():
    sum_of_min_and_max([1, 2, 3, 4, 5, 6, 8, 9])
    sum_of_min_and_max([-10, 5, 10, 100])
    sum_of_min_and_max([1])


# PROGRAM RUN
if __name__ == '__main__':
    main()
