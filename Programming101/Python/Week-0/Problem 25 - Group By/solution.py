# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-25---group-by


# FUNCTIONS
def groupby(func, seq):
    output_dictionary = {}

    for element in seq:
        key = func(element)
        if key not in output_dictionary:
            output_dictionary[key] = [element]
        else:
            output_dictionary[key].append(element)

    return output_dictionary


# main
def main():
    groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7])
    groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])
    groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7])


# PROGRAM RUN
if __name__ == '__main__':
    main()
