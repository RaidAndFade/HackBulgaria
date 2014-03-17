# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-23---count-words


# FUNCTIONS
def count_words(list):
    output_dictionary = {}
    for i in range(len(list)):
        output_dictionary[list[i]] = list.count(list[i])
    return output_dictionary


# main
def main():
    count_words(["apple", "banana", "apple", "pie"])
    count_words(["python", "python", "python", "ruby"])


# PROGRAM RUN
if __name__ == '__main__':
    main()
