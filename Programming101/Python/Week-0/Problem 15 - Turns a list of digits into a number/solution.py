# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-15---turn-a-list-of-digits-into-a-number


# FUNCTIONS
def list_to_number(list):
    output_number = ""
    for element in list:
        output_number += str(element)

    return int(output_number)


# main
def main():
    list_to_number([1,2,3])
    list_to_number([9,9,9,9,9])
    list_to_number([1,2,3,0,2,3])


# PROGRAM RUN
if __name__ == '__main__':
    main()
