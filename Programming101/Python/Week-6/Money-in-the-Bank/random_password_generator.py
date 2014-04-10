# Random password generator 1.0
# @variable passwordLength you can specify the length of the password
# @variable numPassword you can choose how many passwords to generate at this run of the program


# imports
from random import randint


# FUNCTIONS
## Return a string containing one character randomly chosen from a given string.as
# @param characters the string from which to randomly choose a character
# @return a random substring of length 1 from param characters
#
def randomCharacter(characters):
    lenChars = len(characters)
    rand = randint(0, lenChars - 1)
    return characters[rand]

## Inserts one string into another at a random position.
# @param string the string to insert into
# @param toInsert the string to be inserted
# @return a string, result from inserting toInsert into string
#
def insertAtRandom(string, toInsert):
    lenString = len(string)
    rand = randint(0, lenString)
    result = ""

    for i in range(rand):
        result += string[i]

    result += toInsert
    for i in range(rand, lenString):
        result += string[i]

    # return
    return result


## Generate a random password of user input length
# @param length an integer that specifies the length of the password
# @return a string containing the password of given length
#
def generatePassword(length):
    password = ""

    # add random amount of letters and numbers to the password
    for i in range(length):
        rand = randint(0, length)

        if rand % 2 == 0:
            password += randomCharacter("abcdefghijklmnopqrstuvwxyz")

        else:
            randomDigit = randomCharacter("0123456789")
            password = insertAtRandom(password, randomDigit)

    # return
    return password


# main fuction
def main():
    passwordLength = int(input("Password Length:"))
    numPasswords = int(input("How many passwords to generate?"))

    for i in range(numPasswords):
        print(generatePassword(passwordLength))


# RUN THE CODE
if __name__ == '__main__':
    main()
