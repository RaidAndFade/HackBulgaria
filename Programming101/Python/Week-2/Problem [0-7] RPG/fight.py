# DOCUMENTATION
# https://github.com/HackBulgaria/Programming101/blob/master/week2/problems2.md#problem-5---a-class-for-fighting


# IMPORTS
from random import randint


class Fight():
    def __init__(self, human, orc):
        self.human = human
        self.orc = orc

        self.decide_first = randint(0, 100)
        self.attack_first = ""
        if self.decide_first < 50:
            self.attack_first = "human"
        else:
            self.attack_first = "orc"

    def simulate_fight(self):
        if self.attack_first == "human":
            self.orc.take_damage(self.human.attack())
        else:
            self.human.take_damage(self.orc.attack())

        while True:
            attack_turn = randint(0, 100)
            if attack_turn < 50:
                damage = self.human.attack()
                print("Human attacks for %s" % damage)
                self.orc.take_damage(damage)
            else:
                damage = self.orc.attack()
                print("Orc attacks for %s" % damage)
                self.human.take_damage(damage)

            if self.human.is_alive() is False:
                print("Orc is victorious")
                break
            elif self.orc.is_alive() is False:
                print("Human is victorious")
                break

        return True
