from SharkLearn import AdventureLevels
import random
from random import randint
import time
import sys
import json

traps = (
    'fell into a pit trap!',
    'stepped onto a pressure plate, which shot down spikes from the ceiling!',
    'activated a trip wire, which proceeded to shoot spikes from the walls',
    'opened a booby-trapped trapdoor, with explosives!'
)

escape_chance = (
    1,
    1,
    1,
    0
)


exit_chance = (
    1,
    1,
    0
)


xp_possibilities = (
    1,
    2,
    3,
    4,
    5
)


class Player:
    def __init__(self, name, pw):
        self.level = AdventureLevels.globallevel
        self.name = name
        self.pw = pw
        pos = Position(start_pos.starting_x, start_pos.starting_y)
        self.position = pos


class Tile:
    def __init__(self, x, y):
        self.position = Position(x, y)

    def on_enter(self, name):
        pass

    def __str__(self):
        return self.__class__.__name__


class Trap(Tile):
    def on_enter(self, name):
        print(f'You {random.choice(traps)}')
        escape = random.choice(escape_chance)
        if escape == 0:
            print('\tBut you\033[32;10m ESCAPED!')
        elif escape == 1:
            print('\tYOU\033[31;10m DIED!')
            sys.exit(15)


class Trapdoor(Tile):
    def on_enter(self, name):
        print('You found the trapdoor to the next level. Congratulations')
        exit_ = random.choice(exit_chance)
        if exit_ == 1:
            xp_gained = random.choices(xp_possibilities, weights=(14, 10, 5, 3, 1), k=2)
            AdventureLevels.globalxp += sum(xp_gained)

            saved_data = (
                AdventureLevels.globallevel,
                AdventureLevels.globalgold,
                AdventureLevels.globalxp
            )
            with open('saved_data.txt', 'w') as file1:
                file1.write(json.dumps(saved_data))
            print(f'You gain {sum(xp_gained)} xp, you now have {AdventureLevels.globalxp} xp.')
            if AdventureLevels.globallevel * (AdventureLevels.globalxp / 2) >= AdventureLevels.globalxp:
                print(f'You leveled up, you are now level {AdventureLevels.globallevel + 1}')
                AdventureLevels.globallevel += 1
                # if 4 x 7.5 >= 15
                saved_data = (
                    AdventureLevels.globallevel,
                    AdventureLevels.globalgold,
                    AdventureLevels.globalxp
                )
                with open('saved_data.txt', 'w') as file1:
                    file1.write(json.dumps(saved_data))
            sys.exit(100)
        elif exit_ == 0:
            print(f'But you fumbled and fell in head first, you cracked your skull!')
            print('\tYOU\033[31;10m DIED!\033[30;0m ')
            sys.exit(-100)


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
