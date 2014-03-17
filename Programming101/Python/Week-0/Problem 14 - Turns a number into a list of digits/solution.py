# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-14---turn-a-number-into-a-list-of-digits


# FUNCTIONS
def number_to_list(number):
    output_list = []
    for digit in str(number):
        output_list.append(int(digit))
    return output_list


# main
def main():
    number_to_list(123)
    number_to_list(99999)
    number_to_list(123023)

# PROGRAM RUN
if __name__ == '__main__':
    main()
