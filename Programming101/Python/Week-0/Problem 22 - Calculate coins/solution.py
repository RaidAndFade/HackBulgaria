# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-22---calculate-coins


# FUNCTIONS
def calculate_coins(money):
    money *= 100
    COINS = [100, 50, 20, 10, 5, 2, 1]
    output_dictionary = {}

    for coin in COINS:
        coinsNeeded = int(money / coin)
        output_dictionary[coin] = coinsNeeded
        money -= coin * coinsNeeded

    return output_dictionary


# main
def main():
    calculate_coins(0.53)
    calculate_coins(8.94)


# PROGRAM RUN
if __name__ == '__main__':
    main()
