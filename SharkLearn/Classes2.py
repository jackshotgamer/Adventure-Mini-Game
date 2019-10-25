from SharkLearn.AdventureLevels import jacklevel, Sharkboundlevel, Psuedolevel, Annalevel
import random
from random import randint
import time


class Player:
    def __init__(self, name, pw, level):
        self.level = level
        self.name = name
        self.pw = pw
        pos = Position()
        self.position = pos


class Position:
    def __init__(self):
        self.x = start_pos.starting_x
        self.y = start_pos.starting_y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    @property
    def position(self):
        return self.x, self.y

    def __str__(self):
        return f'<Pos x={self.x} y={self.y}'


class RandomPos:
    def __init__(self, size):
        self.x_pos_random = randint(0, size)
        self.y_pos_random = randint(0, size)


class SizeAndPos:
    def __init__(self, size1, size2):
        self.size_of_room = random.randint(size1, size2)
        time.sleep(1)
        self.starting_x = random.randrange(self.size_of_room)
        self.starting_y = random.randrange(self.size_of_room)


class Levels:
    def open_trapdoor(self, player_level, player_name):
        adventure = open("AdventureLevels.py", "w")
        adventure.write(f'{pl1.name}level = {pl1.level}\n'
                        f'{pl2.name}level = {pl2.level}\n'
                        f'{pl3.name}level = {pl3.level}\n'
                        f'{pl4.name}level = {pl4.level}\n')
        adventure.close()


start_pos = SizeAndPos(5, 25)
pos_player = Position()
pl1 = Player('jack', 'main', jacklevel)
pl2 = Player('Sharkbound', 'Shark', Sharkboundlevel)
pl3 = Player('Psuedo', 'lmao', Psuedolevel)
pl4 = Player('Anna', '123', Annalevel)
pl1l = Levels()
pl2l = Levels()
pl3l = Levels()
pl4l = Levels()

# pl1l.open_trapdoor(pl1.name, pl1.level)
# pl2l.open_trapdoor(pl2.name, pl2.level)
# pl3l.open_trapdoor(pl3.name, pl3.level)
# pl4l.open_trapdoor(pl4.name, pl4.level)
