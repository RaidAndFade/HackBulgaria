# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-18---increasing-sequence


# FUNCTIONS
def is_increasing(list):
    for i in range(len(list) - 1):
        if not list[i] < list[i + 1]:
            return False
    return True


# main
def main():
    is_increasing([1,2,3,4,5])
    is_increasing([1])
    is_increasing([5,6,-10])
    is_increasing([1,1,1,1])


# PROGRAM RUN
if __name__ == '__main__':
    main()
