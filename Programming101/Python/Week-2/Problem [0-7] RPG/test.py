# Unit test for Problem 0 - A hero


# IMPORTS
import hero
import weapon
import fight
import dungeon
import unittest


# main
class TestHuman(unittest.TestCase):
    def setUp(self):
        self.hero = hero.Human("Bat George", 9000, "the bagajnik ninja")

    def test_create_hero(self):
        # name
        self.assertEqual("Bat George", self.hero.name)
        # health
        self.assertEqual(9000, self.hero.health)
        self.assertEqual(9000, self.hero.max_health)
        # nickname
        self.assertEqual("the bagajnik ninja", self.hero.nickname)
        # damage
        self.assertEqual(0, self.hero.attack_damage)
        # weapon
        self.assertFalse(self.hero.has_weapon)
        # alive
        self.assertTrue(self.hero.alive)

    def test_hero_negative_health(self):
        dummy_hero = hero.Human("Cheater", -500, "cheats")
        self.assertEqual(1, dummy_hero.get_health())

    def test_known_as(self):
        self.assertEqual("Bat George the bagajnik ninja", self.hero.known_as())

    def test_has_weapon_without_weapon(self):
        self.assertFalse(self.hero.has_weapon)

    def test_equip_weapon(self):
        self.hero.equip_weapon(weapon.Weapon("Stick of Truth", 6, 0))
        self.assertEqual("Stick of Truth", self.hero.weapon.name)
        self.assertEqual(6, self.hero.weapon.damage)
        self.assertEqual(6, self.hero.attack_damage)
        self.assertEqual(0, self.hero.weapon.critical_percent)

    def test_has_weapon_with_weapon(self):
        self.hero.equip_weapon(weapon.Weapon("Broom", 1, 0.2))
        self.assertTrue(self.hero.has_weapon)

    def test_attack_with_no_weapon(self):
        self.assertEqual(0, self.hero.attack())

    def test_attack_with_weapon(self):
        self.hero.equip_weapon(weapon.Weapon("Broom", 1, 0))
        self.assertEqual(1, self.hero.attack())

    def test_get_health_current(self):
        self.assertEqual(9000, self.hero.get_health())

    def test_get_health_updated(self):
        self.hero.health = 6000
        self.assertEqual(6000, self.hero.get_health())

    def test_is_alive_when_alive(self):
        self.assertTrue(self.hero.is_alive())

    def test_is_alive_when_dead(self):
        self.hero.health = 0
        self.assertFalse(self.hero.is_alive())

    def test_take_damage_and_survive(self):
        self.hero.take_damage(5000)
        self.assertEqual(4000, self.hero.get_health())
        self.assertTrue(self.hero.is_alive())

    def test_take_damage_equal_to_health_and_die(self):
        self.hero.take_damage(9000)
        self.assertEqual(0, self.hero.get_health())
        self.assertFalse(self.hero.is_alive())

    def test_take_damage_exceeding_health_and_die(self):
        self.hero.take_damage(11000)
        self.assertEqual(0, self.hero.get_health())
        self.assertFalse(self.hero.is_alive())

    def test_take_damage_when_already_dead(self):
        self.hero.take_damage(15000)
        self.assertEqual("Don't poke the already dead Bat George", self.hero.take_damage(5000))

    def test_take_healing_when_max_health(self):
        self.hero.take_healing(1000)
        self.assertEqual(9000, self.hero.get_health())

    def test_take_healing_when_low_health(self):
        self.hero.health = 1000
        self.hero.take_healing(5000)
        self.assertEqual(6000, self.hero.get_health())

    def test_take_healing_exceeding_max_health_when_low_health(self):
        self.hero.health = 1000
        self.hero.take_healing(12000)
        self.assertEqual(9000, self.hero.get_health())

    def test_take_healing_when_already_dead(self):
        self.health = 0
        self.assertFalse(self.hero.take_healing(6000))


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.hero = hero.Orc("Grommash", 11000, 2)

    def test_create_hero(self):
        # name
        self.assertEqual("Grommash", self.hero.name)
        # health
        self.assertEqual(11000, self.hero.health)
        self.assertEqual(11000, self.hero.max_health)
        # berserk factor
        self.assertEqual(2, self.hero.berserk_factor)
        # damage
        self.assertEqual(0, self.hero.attack_damage)
        # weapon
        self.assertFalse(self.hero.has_weapon)
        # alive
        self.assertTrue(self.hero.alive)

    def test_hero_negative_health(self):
        dummy_hero = hero.Orc("Cheater", -500, 1)
        self.assertEqual(1, dummy_hero.get_health())

    def test_hero_berserk_factor_below_1(self):
        dummy_hero = hero.Orc("Cheater", 1000, -5)
        self.assertEqual(1, dummy_hero.berserk_factor)

    def test_hero_berserk_factor_over_2(self):
        dummy_hero = hero.Orc("Cheater", 1000, 5)
        self.assertEqual(2, dummy_hero.berserk_factor)

    def test_known_as(self):
        self.assertEqual("Grommash", self.hero.known_as())

    def test_has_weapon_without_weapon(self):
        self.assertFalse(self.hero.has_weapon)

    def test_equip_weapon(self):
        self.hero.equip_weapon(weapon.Weapon("Gorehowl", 60, 0.6))
        self.assertEqual("Gorehowl", self.hero.weapon.name)
        self.assertEqual(60, self.hero.weapon.damage)
        self.assertEqual(60, self.hero.attack_damage)
        self.assertEqual(0.6, self.hero.weapon.critical_percent)

    def test_has_weapon_with_weapon(self):
        self.hero.equip_weapon(weapon.Weapon("Gorehowl", 60, 0.6))
        self.assertTrue(self.hero.has_weapon)

    def test_attack_with_no_weapon(self):
        self.assertEqual(0, self.hero.attack())

    def test_attack_with_weapon(self):
        self.hero.equip_weapon(weapon.Weapon("Gorehowl", 60, 0))
        self.assertEqual(120, self.hero.attack())

    def test_get_health_current(self):
        self.assertEqual(11000, self.hero.get_health())

    def test_get_health_updated(self):
        self.hero.health = 6000
        self.assertEqual(6000, self.hero.get_health())

    def test_is_alive_when_alive(self):
        self.assertTrue(self.hero.is_alive())

    def test_is_alive_when_dead(self):
        self.hero.health = 0
        self.assertFalse(self.hero.is_alive())

    def test_take_damage_and_survive(self):
        self.hero.take_damage(5000)
        self.assertEqual(1000, self.hero.get_health())
        self.assertTrue(self.hero.is_alive())

    def test_take_damage_equal_to_health_and_die(self):
        self.hero.take_damage(5500)
        self.assertEqual(0, self.hero.get_health())
        self.assertFalse(self.hero.is_alive())

    def test_take_damage_exceeding_health_and_die(self):
        self.hero.take_damage(20000)
        self.assertEqual(0, self.hero.get_health())
        self.assertFalse(self.hero.is_alive())

    def test_take_damage_when_already_dead(self):
        self.hero.take_damage(15000)
        self.assertEqual("Don't poke the already dead Grommash", self.hero.take_damage(5000))

    def test_take_healing_when_max_health(self):
        self.hero.take_healing(1000)
        self.assertEqual(11000, self.hero.get_health())

    def test_take_healing_when_low_health(self):
        self.hero.health = 1000
        self.hero.take_healing(5000)
        self.assertEqual(6000, self.hero.get_health())

    def test_take_healing_exceeding_max_health_when_low_health(self):
        self.hero.health = 1000
        self.hero.take_healing(15000)
        self.assertEqual(11000, self.hero.get_health())

    def test_take_healing_when_already_dead(self):
        self.health = 0
        self.assertFalse(self.hero.take_healing(6000))


class TestWeapon(unittest.TestCase):
    def test_create_weapon(self):
        self.weapon = weapon.Weapon("Stick of Truth", 6, 0.5)
        self.assertEqual("Stick of Truth", self.weapon.name)
        self.assertEqual(6, self.weapon.damage)
        self.assertEqual(0.5, self.weapon.critical_percent)

    def test_negative_damage(self):
        dummy_weapon = weapon.Weapon("Fork", -5, 1)
        self.assertEqual(1, dummy_weapon.damage)

    def test_critical_percent_below_0(self):
        dummy_weapon = weapon.Weapon("Fork", -5, -5)
        self.assertEqual(0, dummy_weapon.critical_percent)

    def test_critical_percent_over_100(self):
        dummy_weapon = weapon.Weapon("Fork", -5, 3)
        self.assertEqual(1, dummy_weapon.critical_percent)

    def test_critical_hit_100_percent(self):
        self.weapon = weapon.Weapon("Stick of Truth", 6, 1)
        self.assertTrue(self.weapon.critical_hit())

    def test_critical_hit_0_percent(self):
        self.weapon = weapon.Weapon("Stick of Truth", 6, 0)
        self.assertFalse(self.weapon.critical_hit())


class TestFight(unittest.TestCase):
    def setUp(self):
        self.dummy_human = hero.Human("Human", 2500, "the common")
        self.dummy_orc = hero.Orc("Orc", 3300, 1.3)
        self.fight = fight.Fight(self.dummy_human, self.dummy_orc)

        self.dummy_human.equip_weapon(weapon.Weapon("Sword of a Thousand Truths", 480, 0.4))
        self.dummy_orc.equip_weapon(weapon.Weapon("Aeglos", 390, 0.1))

    def test_attack_first(self):
        if self.fight.attack_first == 'human':
            self.assertEqual('human', self.fight.attack_first)
        else:
            self.assertEqual('orc', self.fight.attack_first)

    def test_fight_simulation(self):
        self.assertTrue(self.fight.simulate_fight())


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.dungeon_map = dungeon.Dungeon("dungeon_map.txt")
        self.human = hero.Human("Dorah", 150, "the Explorer")
        self.orc = hero.Orc("Can't think of a name", 200, 1.2)

    def test_print_map(self):
        self.assertEqual("S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S", self.dungeon_map.print_map())

    def test_spawn_human(self):
        self.assertTrue(self.dungeon_map.spawn("a human", self.human))
        self.assertEqual("H.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S", self.dungeon_map.print_map())

    def test_spawn_orc(self):
        self.assertTrue(self.dungeon_map.spawn("an orc", self.orc))
        self.assertEqual("O.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S", self.dungeon_map.print_map())

    def test_spawn_human_and_orc(self):
        self.dungeon_map.spawn("a human", self.human)
        self.dungeon_map.spawn("an orc", self.orc)
        self.assertEqual("H.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####O", self.dungeon_map.print_map())

    def test_spawn_more_heroes_than_map_spawn_points(self):
        self.dungeon_map.spawn("a human", self.human)
        self.dungeon_map.spawn("an orc", self.orc)

        third_wheel = hero.Human("Harry Potter", 150, "the child who survived")
        self.assertFalse(self.dungeon_map.spawn("Harry Potter", third_wheel))


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
