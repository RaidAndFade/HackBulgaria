# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-24---unique-words


# FUNCTIONS
def unique_words_count(list):
    unique_list = []
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
    return len(unique_list)


# main
def main():
    unique_words_count(["apple", "banana", "apple", "pie"])
    unique_words_count(["python", "python", "python", "ruby"])
    unique_words_count(["HELLO!"] * 10)


# PROGRAM RUN
if __name__ == '__main__':
    main()
