# DOCUMENTATION
# https://github.com/HackBulgaria/Programming101/blob/master/week2/problems2.md#problem-3---the-weapon


# IMPORTS
from random import random


class Weapon():
    def __init__(self, name, damage, critical_percent):
        self.name = name
        self.damage = damage

        if self.damage < 1:
            self.damage = 1

        self.critical_percent = critical_percent
        if self.critical_percent > 1:
            self.critical_percent = 1
        elif self.critical_percent < 0:
            self.critical_percent = 0

    def critical_hit(self):
        chance = random()
        if chance <= self.critical_percent:
            return True
        else:
            return False
