from AGLevels import jacklevel, Sharkboundlevel, Psuedolevel, Annalevel, jackgold, Sharkboundgold, Psuedogold, Annagold
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
    @staticmethod
    def gain_level():
        adventure = open("AdventureLevels.py", "w")
        adventure.write(f'{pl1.name}level = {pl1.level}\n'
                        f'{pl2.name}level = {pl2.level}\n'
                        f'{pl3.name}level = {pl3.level}\n'
                        f'{pl4.name}level = {pl4.level}\n'
                        f'{pl1.name}gold = {pl1g}\n'
                        f'{pl2.name}gold = {pl2g}\n'
                        f'{pl3.name}gold = {pl3g}\n'
                        f'{pl4.name}gold = {pl4g}\n')
        adventure.close()


class Gold:
    def __init__(self, gold):
        self.gold = gold

    def gain_gold(self, gold_gained):
        self.gold += gold_gained
        adventure = open("AdventureLevels.py", "w")
        adventure.write(f'{pl1.name}level = {pl1.level}\n'
                        f'{pl2.name}level = {pl2.level}\n'
                        f'{pl3.name}level = {pl3.level}\n'
                        f'{pl4.name}level = {pl4.level}\n'
                        f'{pl1.name}gold = {pl1g}\n'
                        f'{pl2.name}gold = {pl2g}\n'
                        f'{pl3.name}gold = {pl3g}\n'
                        f'{pl4.name}gold = {pl4g}\n')
        adventure.close()


start_pos = SizeAndPos(8, 25)
pos_player = Position()
pl1 = Player('jack', 'main', jacklevel)
pl2 = Player('Sharkbound', 'Shark', Sharkboundlevel)
pl3 = Player('Psuedo', 'lmao', Psuedolevel)
pl4 = Player('Anna', '123', Annalevel)

pl1g = Gold(jackgold)
pl2g = Gold(Sharkboundgold)
pl3g = Gold(Psuedogold)
pl4g = Gold(Annagold)

pl1l = Levels()
pl2l = Levels()
pl3l = Levels()
pl4l = Levels()
