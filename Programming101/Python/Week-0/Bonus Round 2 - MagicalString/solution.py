# DOCUMENTATION
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#bonus-round-2---magic-string


# FUNCTIONS
def minimal_moves(string):
    moves_needed = 0
    middle = len(string) // 2
    for char in range(middle):
        if string[char] == "<":
            moves_needed += 1
    for char in range(middle, len(string)):
        if string[char] == ">":
            moves_needed += 1
    return moves_needed


# main
def main():
    print()


# PROGRAM RUN
if __name__ == "__main__":
    main()
