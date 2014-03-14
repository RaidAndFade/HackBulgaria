# DOCUMENTATION
# https://github.com/HackBulgaria/Programming101/blob/master/week2/problems2.md#problem-6---inside-the-dungeon


# IMPORTS
import hero


class Dungeon(object):
    def __init__(self, map_name):
        map_name = open(map_name, "r")
        self.dungeon_map = map_name.read()
        map_name.close()

    def print_map(self):
        # added a newline to make it more readable during tests
        print(self.dungeon_map + "\n")
        return self.dungeon_map

    def spawn(self, player_name, entity):
        spawned = False
        if self.dungeon_map.count("S") < 1:
            spawned = False
        else:
            if type(entity) is hero.Human:
                self.dungeon_map = self.dungeon_map.replace("S", "H", 1)
                spawned = True
            elif type(entity) is hero.Orc:
                self.dungeon_map = self.dungeon_map.replace("S", "O", 1)
                spawned = True

        return spawned
