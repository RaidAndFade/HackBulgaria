# DOCUMENTATION
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#bonus-round-1---division-by-zero


# FUNCTIONS
def count_numbers(numbers_list):
    for a in numbers_list:
        for b in numbers_list:
            if a > b:
                c = a // b
                if c not in numbers_list:
                    numbers_list.append(c)
    return len(numbers_list)


# main
def main():
    print(count_numbers([9, 2]))


# PROGRAM RUN
if __name__ == "__main__":
    main()
