 # DOCUMENTATION
# https://github.com/HackBulgaria/Programming101/blob/master/week2/problems2.md#problem-6---inside-the-dungeon


# IMPORTS
import hero


class Dungeon(object):
    def __init__(self, map_name):
        self.map_name = map_name
        map_file = open(self.map_name, "r")
        # add the maps as a list split by newline
        self.dungeon_map = map_file.read()
        self.dungeon_map = self.dungeon_map.split("\n")

        # get map width and height
        self.map_width = 0
        self.map_height = 0

        # convert map to matrix
        self.new_dungeon_map = []
        for line in self.dungeon_map:
            self.map_height += 1
            line_characters = []
            for char in line:
                line_characters.append(char)
                self.map_width += 1
            self.new_dungeon_map.append(line_characters)
        self.dungeon_map = self.new_dungeon_map
        map_file.close()
        # players on the map
        self.players_on_map = {}

    def print_map(self):
        # convert map matrix back to list
        output_list = []
        for element in self.dungeon_map:
            output_string = ""
            for char in element:
                output_string += char
            output_list.append(output_string)

        # print("\n".join(output_list))
        return "\n".join(output_list)

    def get_spawn_points(self):
        map_file = open(self.map_name, "r")
        contents = map_file.read()
        count = contents.count("S")
        map_file.close()
        return count

    def spawn(self, player_name, entity):
        spawn_points = self.get_spawn_points()
        if spawn_points < 1:
            return False
        else:
            if type(entity) is hero.Human:
                for x in range(len(self.dungeon_map)):
                    for y in range(len(self.dungeon_map[x])):
                        if self.dungeon_map[x][y] == "S":
                            self.dungeon_map[x][y] = "H"
                            self.players_on_map[player_name] = x, y
                            return True

            elif type(entity) is hero.Orc:
                for x in range(len(self.dungeon_map)):
                    for y in range(len(self.dungeon_map[x])):
                        if self.dungeon_map[x][y] == "S":
                            self.dungeon_map[x][y] = "O"
                            self.players_on_map[player_name] = x, y
                            return True

    def list_players(self):
        print("Players on the map:")
        for key in self.players_on_map:
            print(key, self.players_on_map[key])
        print("\n")

    def is_move_valid(self, player_name, direction):
        x = self.players_on_map[player_name][0]
        y = self.players_on_map[player_name][1]

        try:
            if direction is "right":
                if self.dungeon_map[x][y+1] != "#" and y + 1 < self.map_width:
                    return True
            elif direction is "left":
                if self.dungeon_map[x][y-1] != "#" and y - 1 >= 0:
                    return True
            elif direction is "down":
                if self.dungeon_map[x+1][y] != "#" and x + 1 < self.map_height:
                    return True
            elif direction is "up":
                if self.dungeon_map[x-1][y] != "#" and x - 1 > -1:
                    return True
        except IndexError:
            return False

    def update_position(self, player_name, direction):
        x = self.players_on_map[player_name][0]
        y = self.players_on_map[player_name][1]
        if direction is "right":
            y += 1
            self.players_on_map[player_name] = x, y
            self.dungeon_map[x][y], self.dungeon_map[x][y-1] = self.dungeon_map[x][y-1], self.dungeon_map[x][y]
        elif direction is "left":
            y -= 1
            self.players_on_map[player_name] = x, y
            self.dungeon_map[x][y], self.dungeon_map[x][y+1] = self.dungeon_map[x][y+1], self.dungeon_map[x][y]
        elif direction is "down":
            x += 1
            self.players_on_map[player_name] = x, y
            self.dungeon_map[x][y], self.dungeon_map[x-1][y] = self.dungeon_map[x-1][y], self.dungeon_map[x][y]
        elif direction is "up":
            x -= 1
            self.players_on_map[player_name] = x, y
            self.dungeon_map[x][y], self.dungeon_map[x+1][y] = self.dungeon_map[x+1][y], self.dungeon_map[x][y]

    def move(self, player_name, direction):
        if direction is "right":
            if self.is_move_valid(player_name, direction) is True:
                self.update_position(player_name, direction)
                return True

        elif direction is "left":
            if self.is_move_valid(player_name, direction) is True:
                self.update_position(player_name, direction)
                return True

        elif direction is "down":
            if self.is_move_valid(player_name, direction) is True:
                self.update_position(player_name, direction)
                return True

        elif direction is "up":
            if self.is_move_valid(player_name, direction) is True:
                self.update_position(player_name, direction)
                return True
        else:
            return False
