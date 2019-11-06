from SharkLearn import AdventureLevels
import random
from random import randint
import time
import sys
import json

enemy_possibilities_names = (
    'Ogre',
    'Dragon',
    'Troll',
    'Zombie',
    'Mutated Monster',
    'Goblin',
    'Gremlin Child'
)

enemy_possibilities_attack = (
    2,
    3,
    5,
    7
)


enemy_possibilities_health = (
    50,
    50
)

death_possibilities = (
    'But with your final breath, you lunged at the {}, finally killing it, you lie down, and go to sleep, forever.',
    'But as your eyes were closing for the final time, you saw the {} impale itself on a spike by accident.',
    'But the reason you died is because you killed the {}, and it fell on top of you, crushing you instantly',
    'But your ghost scared the {} so much, it died from a heart attack!'
)

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


class Enemy(Tile):
    def on_enter(self, name):
        enemy_health = random.choice(enemy_possibilities_health)
        enemy_name = random.choice(enemy_possibilities_names)
        print(
            f'You found a {enemy_name}, it has {str(enemy_health)} health and can deal '
            f'{" or ".join(map(str, enemy_possibilities_attack))} damage')
        player_health = 50
        while enemy_health > 0:
            player_attack = random.randint(7, 7)
            enemy_attack = random.randint(7, 7)
            time.sleep(1.5)
            player_health -= enemy_attack
            enemy_health -= player_attack
            print(f'You did {player_attack} damage, but received {enemy_attack} in return!\n'
                  f'You now have {player_health}, the {enemy_name} has {enemy_health}!\n')
            time.sleep(1)
            if player_health <= 0 and enemy_health <= 0:
                print(f'\033[31;10m You died\033[30;0m \n{random.choice(death_possibilities).format(enemy_name)}')
                sys.exit(15)
            elif player_health <= 0:
                print('AAGGHHHHhhhhhh...... \n'
                      '\033[31;10m You died \033[30;0m ')
                sys.exit(15)
        print(f'You killed the {enemy_name}, congratulation! Keep looking for the exit.')


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
