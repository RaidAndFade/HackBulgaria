# Problem 20 - What is the sign?
#
# This problem is from the Python 2013 course in FMI.
#
# Implement a function, called what_is_my_sign(day, month),
# which takes two integer (one for the day and one for the month)
# and returns the name of the zodiac for the given time period.
#
# Consider the following zodiac table (Or check wikipedia):
#   Aries: 21 March – 20 April
#   Taurus: 21 April – 21 May
#   Gemini: 22 May – 21 June
#   Cancer: 22 June – 22 July
#   Leo: 23 July – 22 August
#   Virgo: 23 August – 23 September
#   Libra: 24 September – 23 October
#   Scorpio: 24 October – 22 November
#   Sagittarius: 23 November – 21 December
#   Capricorn: 22 December – 20 January
#   Aquarius: 21 January – 19 February
#   Pisces: 20 February – 20 March
#
# Signature
#
# def what_is_my_sign(day, month):
#     # Implementation
# Test examples
#
# >>> what_is_my_sign(5, 8)
# "Leo"
# >>> what_is_my_sign(29, 1)
# "Aquarius"
# >>> what_is_my_sign(30, 6)
# "Cancer"
# >>> what_is_my_sign(31, 5)
# "Gemini"
# >>> what_is_my_sign(2, 2)
# "Aquarius"
# >>> what_is_my_sign(8, 5)
# "Taurus"
# >>> what_is_my_sign(9, 1)
# "Capricorn"

# IMPORTS
from sys import exit

# FUNCTIONS
def what_is_my_sign(day, month):
    if month > 12 or month < 1:
        exit("Invalid month number.")

    if month == 1:
        if day > 20:
            return "Aquarius"
        else:
            return "Capricorn"

    elif month == 2:
        if day > 19:
            return "Pisces"
        else:
            return "Aquarius"

    elif month == 3:
        if day > 20:
            return "Aries"
        else:
            return "Pisces"

    elif month == 4:
        if day > 20:
            return "Taurus"
        else:
            return "Aries"

    elif month == 5:
        if day > 21:
            return "Gemini"
        else:
            return "Taurus"

    elif month == 6:
        if day > 21:
            return "Cancer"
        else:
            return "Gemini"

    elif month == 7:
        if day > 22:
            return "Leo"
        else:
            return "Cancer"

    elif month == 8:
        if day > 22:
            return "Virgo"
        else:
            return "Leo"

    elif month == 9:
        if day > 23:
            return "Libra"

        else:
            return "Virgo"

    elif month == 10:
        if day > 23:
            return "Scorpio"
        else:
            return "Libra"

    elif month == 11:
        if day > 22:
            return "Sagittarius"
        else:
            return "Scorpio"

    else:
        if day > 21:
            return "Capricorn"
        else:
            return "Sagittarius"

# main
def main():
    print(what_is_my_sign(5, 8))
    print(what_is_my_sign(29, 1))
    print(what_is_my_sign(30, 6))
    print(what_is_my_sign(31, 5))
    print(what_is_my_sign(2, 2))
    print(what_is_my_sign(8, 5))
    print(what_is_my_sign(9, 1))

# PROGRAM RUN
if __name__ == '__main__':
    main()