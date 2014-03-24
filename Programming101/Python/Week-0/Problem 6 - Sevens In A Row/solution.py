# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-6---are-there-n-sevens-in-a-row


# FUNCTIONS
def sevens_in_a_row(list, consecutive_sevens):
    row_sevens = 0
    for number in list:
        if number == 7:
            row_sevens += 1
        elif row_sevens == consecutive_sevens:
            return True
        else:
            consecutive_sevens = 0
    return False


# main
def main():
    sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3)
    sevens_in_a_row([1, 7, 1, 7, 7], 4)
    sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3)
    sevens_in_a_row([7, 2, 1, 6, 2], 1)


# PROGRAM RUN
if __name__ == '__main__':
    main()
