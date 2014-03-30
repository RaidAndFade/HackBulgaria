# Problem F6 - Count characters, words or lines
#
# Implement a Python script, called wc.py that takes two arguments:
#
# A command, that can be one of the following : chars, words, lines
# A filename
# The script should output, according to the command, the following:
#
# For the command chars, the number of characters in the file
# For the command words, the number of words in the file
# For the command lines, the number of lines in the file
# Examples
#
# Lets have the following text:
#
# story.txt:
#
# Now indulgence dissimilar for his thoroughly has terminated.
# Agreement offending commanded my an. Change wholly say why eldest period.
# Are projection put celebrated particular unreserved joy unsatiable its.
# In then dare good am rose bred or. On am in nearer square wanted.
#
# Of resolve to gravity thought my prepare chamber so.
# Unsatiable entreaties collecting may sympathize nay interested instrument.
# If continue building numerous of at relation in margaret. Lasted engage roused mother an am at.
# Other early while if by do to. Missed living excuse as be.
# Cause heard fat above first shall for. My smiling to he removal weather on anxious.
#
# Ferrars all spirits his imagine effects amongst neither. It bachelor cheerful of mistaken.
# Tore has sons put upon wife use bred seen. Its dissimilar invitation ten has discretion unreserved.
# Had you him humoured jointure ask expenses learning. Blush on in jokes sense do do.
# Brother hundred he assured reached on up no. On am nearer missed lovers.
# To it mother extent temper figure better.
#
# Print the chars:
#
# $ python wc.py chars story.txt
# 1032
# Print the words:
#
# $ python wc.py words story.txt
# 169
# Print the lines:
#
# $ python wc.py lines story.txt
# 6

# IMPORTS
from sys import argv, exit


# FUNCTIONS
def count_chars(filename):
    chars_count = 0
    try:
        opened_file = open(filename, "r")
    except IOError:
        return "Error: File not found!"

    for line in opened_file:
        chars_count += len(line)
    opened_file.close()
    return chars_count


def count_words(filename):
    words_list = []
    try:
        opened_file = open(filename, "r")
    except IOError:
        return "Error: File not found!"

    for line in opened_file:
        line = line.split()
        for word in line:
            words_list.append(word)
    opened_file.close()
    return len(words_list)


def count_lines(filename):
    try:
        opened_file = open(filename, "r")
    except IOError:
        return "Error: File not found!"

    contents = opened_file.read()
    # count the first line + the rest
    num_lines = contents.count("\n") + 1
    opened_file.close()
    return num_lines


# main
def main():
    if len(argv) != 3:
        exit("Invalid number of arguments")

    filename = argv[2]
    if argv[1] == "chars":
        print(count_chars(filename))

    elif argv[1] == "words":
        print(count_words(filename))

    elif argv[1] == "lines":
        print(count_lines(filename))

    else:
        exit("Invalid command given")


# PROGRAM RUN
if __name__ == '__main__':
    main()
