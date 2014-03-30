# Problem F5 - Concatenate files into one
#
# Implement a Python script, called concat_files.py,
# that takes multiple filenames as arguments.
#
# The script should concatenate all file contents into a single file,
# called MEGATRON (Capslock is by choice :D)
#
# Every time you run the script, do not delete the old contents of MEGATRON,
# but append the new ones at the end of the file.
#
# Examples
#
# Again, let's have the following files:
#
# file1.txt:
#
# Python is an awesome language!
# You should try it.
# file2.txt:
#
# Also, you can use Python at a lot of different places!
# Running the script:
#
# $ python concat_files.py file1.txt file2.txt
# $ cat MEGATRON
# Python is an awesome language!
# You should try it.
#
# Also, you can use Python at a lot of different places!
# $ python concat_files.py file1.txt file2.txt
# $ cat MEGATRON
# Python is an awesome language!
# You should try it.
#
# Also, you can use Python at a lot of different places!
#
# Python is an awesome language!
# You should try it.
#
# Also, you can use Python at a lot of different places!

# IMPORTS
from sys import argv, exit


# FUNCTIONS
def concatenate(files):
    output_content = ""
    for filename in files:
        try:
            opened_file = open(filename, "r")
        except IOError:
            return "Error: File not found!"
        output_content += "{}\n".format(opened_file.read())
        opened_file.close()
    return output_content.rstrip()


def write_to_megatron(content):
    megatron = open("MEGATRON", "w")
    megatron.write(content)
    megatron.close()


# main
def main():
    if len(argv) == 1:
        exit("Invalid number of arguments")
    write_to_megatron(concatenate(argv[1:]))


# PROGRAM RUN
if __name__ == '__main__':
    main()
