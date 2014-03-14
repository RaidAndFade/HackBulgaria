# DOCUMENTATION
# https://github.com/HackBulgaria/Programming101/blob/master/week2/problems2.md

# IMPORTS
import weapon


class Entity():
    def __init__(self, name, health):
        self.attack_damage = 0
        self.alive = True
        self.has_weapon = False
        self.health = health
        self.max_health = health
        self.critical_hit = 1

        if self.health < 1:
            self.health = 1
            self.max_health = 1

        self.name = name

    def attack(self):
        if self.has_weapon is True:
            if self.weapon.critical_hit():
                self.critical_hit = 2
        else:
            self.critical_hit = 1
        return self.attack_damage * self.critical_hit

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.attack_damage = self.weapon.damage
        self.has_weapon = True

    def has_weapon(self):
        return self.has_weapon

    def known_as(self):
        return "%s" % self.name

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health < 1:
            self.heath = 0
            self.alive = False
            return False

        self.alive = True
        return True

    def take_damage(self, damage_points):
        if self.is_alive():
            if self.get_health() > damage_points:
                self.health -= damage_points
            else:
                self.alive = False
                self.health = 0
        else:
            return "Don't poke the already dead %s" % self.name

    def take_healing(self, healing_points):
        if self.is_alive() is False:
            return False

        self.health += healing_points
        if self.health > self.max_health:
            self.health = self.max_health


class Human(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname
        # self.max_health = health
        # self.alive = True

    def known_as(self):
        return "%s %s" % (self.name, self.nickname)


class Orc(Entity):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = berserk_factor
        if berserk_factor > 2:
            self.berserk_factor = 2
        elif berserk_factor < 1:
            self.berserk_factor = 1

    def attack(self):
        if self.has_weapon is True:
            if self.weapon.critical_hit():
                self.critical_hit = 2
        else:
            self.critical_hit = 1
        return self.attack_damage * self.critical_hit * self.berserk_factor

    def take_damage(self, damage_points):
        if self.is_alive():
            if self.get_health() > damage_points:
                self.health -= damage_points * self.berserk_factor
            else:
                self.alive = False
                self.health = 0
        else:
            return "Don't poke the already dead %s" % self.name
