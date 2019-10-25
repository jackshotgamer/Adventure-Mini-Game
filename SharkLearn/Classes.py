from SharkLearn import AdventureLevels
import random
from random import randint
import time


class Player:
    def __init__(self, name, pw):
        self.level = AdventureLevels.globallevel
        self.name = name
        self.pw = pw
        pos = Position(start_pos.starting_x, start_pos.starting_y)
        self.position = pos


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def __repr__(self):
        return f'<Pos x={self.x} y={self.y}'


class RandomPos:
    def __init__(self, size):
        self.position = Position(randint(0, size), randint(0, size))


class SizeAndPos:
    def __init__(self, size1, size2):
        self.size_of_room = random.randint(size1, size2)
        time.sleep(1)
        self.starting_x = random.randrange(self.size_of_room)
        self.starting_y = random.randrange(self.size_of_room)


start_pos = SizeAndPos(8, 25)
pos_player = Position(start_pos.starting_x, start_pos.starting_y)
pl1 = Player('jack', 'main', )
pl2 = Player('Sharkbound', 'Shark')
pl3 = Player('Psuedo', 'lmao')
pl4 = Player('Anna', '123')
