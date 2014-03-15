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

        # convert map to matrix
        self.new_dungeon_map = []
        for line in self.dungeon_map:
            line_characters = []
            for char in line:
                line_characters.append(char)
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
                for i in range(len(self.dungeon_map)):
                    for j in range(len(self.dungeon_map[i])):
                        if self.dungeon_map[i][j] == "S":
                            self.dungeon_map[i][j] = "H"
                            self.players_on_map[player_name] = i, j
                            return True

            elif type(entity) is hero.Orc:
                for i in range(len(self.dungeon_map)):
                    for j in range(len(self.dungeon_map[i])):
                        if self.dungeon_map[i][j] == "S":
                            self.dungeon_map[i][j] = "O"
                            self.players_on_map[player_name] = i, j
                            return True

    def list_players(self):
        print("Players on the map:")
        for key in self.players_on_map:
            print(key, self.players_on_map[key])
        print("\n")

    def move(self, player_name, direction):
        player_pos_x = self.players_on_map[player_name][0]
        player_pos_y = self.players_on_map[player_name][1]

        if direction is "right":
            try:
                if self.dungeon_map[player_pos_x][player_pos_y+1] != "#":
                    player_pos_y += 1
                    self.players_on_map[player_name] = player_pos_y, player_pos_x
                    self.dungeon_map[player_pos_x][player_pos_y], self.dungeon_map[player_pos_x][player_pos_y-1] = self.dungeon_map[player_pos_x][player_pos_y-1], self.dungeon_map[player_pos_x][player_pos_y]
                    return True
                else:
                    return False
            except Exception:
                return False

        elif direction is "left":
            if self.dungeon_map[player_pos_x][player_pos_y-1] != "#":
                player_pos_y -= 1
                self.players_on_map[player_name] = player_pos_y, player_pos_x
                self.dungeon_map[player_pos_x][player_pos_y], self.dungeon_map[player_pos_x][player_pos_y+1] = self.dungeon_map[player_pos_x][player_pos_y+1], self.dungeon_map[player_pos_x][player_pos_y]
                return True
            else:
                return False

        elif direction is "down":
            if self.dungeon_map[player_pos_x+1][player_pos_y] != "#":
                player_pos_x += 1
                self.players_on_map[player_name] = player_pos_y, player_pos_x
                self.dungeon_map[player_pos_x][player_pos_y], self.dungeon_map[player_pos_x-1][player_pos_y] = self.dungeon_map[player_pos_x-1][player_pos_y], self.dungeon_map[player_pos_x][player_pos_y]
                return True
            else:
                return False

        elif direction is "up":
            if self.dungeon_map[player_pos_x-1][player_pos_y] != "#":
                player_pos_x -= 1
                self.players_on_map[player_name] = player_pos_y, player_pos_x
                self.dungeon_map[player_pos_x][player_pos_y], self.dungeon_map[player_pos_x+1][player_pos_y] = self.dungeon_map[player_pos_x+1][player_pos_y], self.dungeon_map[player_pos_x][player_pos_y]
                return True
            else:
                return False
        return False
