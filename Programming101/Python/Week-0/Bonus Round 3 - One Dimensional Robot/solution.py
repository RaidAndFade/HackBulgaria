# DOCUMENTATION
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#bonus-round-3---one-dimensional-robot


# FUNCTIONS
def final_position(commands, a, b):
    final_position = 0
    for command in commands:
        if command == "L":
            if final_position > -a:
                final_position -= 1
        elif command == "R":
            if final_position < b:
                final_position += 1
    return final_position


# main
def main():
    print()


# PROGRAM RUN
if __name__ == "__main__":
    main()
