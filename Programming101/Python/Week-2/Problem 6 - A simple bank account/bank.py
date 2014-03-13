# DOCUMENTATION
# https://github.com/HackBulgaria/Programming101/blob/master/week2/problems.md#problem-6---a-simple-bank-account


class BankAccount():
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit_money(self, amount):
        if amount < 0:
            return False

        self.__balance += amount
        return True

    def withdraw_money(self, amount):
        if amount > self.__balance:
            return False

        self.__balance -= amount
        return True
