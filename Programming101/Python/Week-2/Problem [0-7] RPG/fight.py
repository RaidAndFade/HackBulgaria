# DOCUMENTATION
# https://github.com/HackBulgaria/Programming101/blob/master/week2/problems2.md#problem-5---a-class-for-fighting


# IMPORTS
from random import randint


class Fight():
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.player_one_name = self.player_one.name
        self.player_two_name = self.player_two.name

        self.decide_first = randint(0, 100)
        self.attack_first = ""
        if self.decide_first < 50:
            self.attack_first = self.player_one_name
        else:
            self.attack_first = self.player_two_name

    def simulate_fight(self):
        if self.attack_first == self.player_one_name:
            self.player_two.take_damage(self.player_one.attack())
        else:
            self.player_one.take_damage(self.player_two.attack())

        while True:
            attack_turn = randint(0, 100)
            if attack_turn < 50:
                damage = self.player_one.attack()
                print("%s attacks for %s" % (self.player_one.name, damage))
                self.player_two.take_damage(damage)
            else:
                damage = self.player_two.attack()
                print("%s attacks for %s" % (self.player_two.name, damage))
                self.player_one.take_damage(damage)

            if self.player_one.is_alive() is False:
                print("%s is victorious" % self.player_one_name)
                break
            elif self.player_two.is_alive() is False:
                print("%s is victorious" % self.player_two_name)
                break

        return True
