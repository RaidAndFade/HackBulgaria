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
# Now indulgence dissimilar for his thoroughly has terminated. Agreement offending commanded my an. Change wholly say why eldest period. Are projection put celebrated particular unreserved joy unsatiable its. In then dare good am rose bred or. On am in nearer square wanted.
#
# Of resolve to gravity thought my prepare chamber so. Unsatiable entreaties collecting may sympathize nay interested instrument. If continue building numerous of at relation in margaret. Lasted engage roused mother an am at. Other early while if by do to. Missed living excuse as be. Cause heard fat above first shall for. My smiling to he removal weather on anxious.
#
# Ferrars all spirits his imagine effects amongst neither. It bachelor cheerful of mistaken. Tore has sons put upon wife use bred seen. Its dissimilar invitation ten has discretion unreserved. Had you him humoured jointure ask expenses learning. Blush on in jokes sense do do. Brother hundred he assured reached on up no. On am nearer missed lovers. To it mother extent temper figure better.
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

# main
def main():
    if len(argv) != 3:
        exit("Invalid number of arguments")

    # count chars
    if argv[1] == "chars":
        charsCount =  0

        filename = argv[2]
        file = open(filename, "r")
        line = file.readline()

        while line != "":
            line = line.strip()
            charsCount += len(line)
            line = file.readline()

        print(charsCount)

    # count words
    elif argv[1] == "words":
        wordsList = []

        filename = argv[2]
        file = open(filename, "r")
        line = file.readline()

        while line != "":
            line = line.rsplit()
            for word in line:
                wordsList.append(word)
            line = file.readline()

        print(len(wordsList))

    # count lines
    elif argv[1] == "lines":
        numLines = 0

        filename = argv[2]
        file = open(filename, "r")
        line = file.readline()

        while line != "":
            numLines += 1
            line = file.readline()

        print(numLines)

    else:
        exit("Invalid command given")

# PROGRAM RUN
main()