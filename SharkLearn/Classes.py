from SharkLearn import AdventureLevels
import random
from random import randint
import time
import sys

enemy_possibilities_names = (
    'Ogre',
    'Dragon',
    'Troll',
    'Zombie',
    'Mutated Monster',
    'Goblin',
    'Gremlin Child',
    'Karen'
)

enemy_possibilities_attack = (
    2,
    3,
    5,
    7
)


player_possibilities_attack = [
    2,
    3,
    5,
    7
]


enemy_possibilities_health = (
    60,
    45,
    50,
    55
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

gold_possibilities = (
    20,
    25,
    40,
    50,
    75,
    90,
    110
)


def check_xp(charac_name):
    while True:
        if AdventureLevels.globalxp >= AdventureLevels.prev_req_xp * 1.5:
            print(f'{charac_name} leveled up, {charac_name} is now level {AdventureLevels.globallevel + 1}')
            AdventureLevels.prev_req_xp *= 1.5
            AdventureLevels.globallevel += 1
            AdventureLevels.save_charac(charac_name)
        else:
            print(f'{charac_name} needs '
                  f'{int((AdventureLevels.prev_req_xp * 1.5) + 0.9999999999999999999999999) - AdventureLevels.globalxp}'
                  f' more xp to level up')
            return



def random_loot(charac_name, loot_choice=None):
    if loot_choice is None:
        loot_table = (
            'xp',
            'gold',
            'junk',
            'junk',
            'item'
        )
        loot = random.choice(loot_table)
        if loot == 'xp':
            xp_amount = random.choice(xp_possibilities)
            print(f'You found an experience potion, it contains a total of {xp_amount} xp!')
            AdventureLevels.globalxp += xp_amount
            AdventureLevels.save_charac(charac_name)
            check_xp(charac_name)
        elif loot == 'gold':
            gold_amount = random.choice(gold_possibilities)
            print(f'You found a pile of gold, it contains a total of {gold_amount} gold!')
            AdventureLevels.globalgold += gold_amount
            AdventureLevels.save_charac(charac_name)
        elif loot == 'junk':
            junk = (
                'a empty tin can.',
                'a rotten banana.',
                'a skull.',
                'some bones and a fake piece of gold.',
                'a bunch of cobwebs.'
            )
            print(f'You found {random.choice(junk)} You throw it away.')
        elif loot == 'item':
            print(f'You found a weapon!')
            item_choice = str(random.choices((1, 2, 3, 4), k=1, weights=(6, 4, 2, 1))[0])
            if item_choice == '1':
                name = 'Rusty Knife'
                damage1 = 3
                damage2 = 8
                cost = 50
                AdventureLevels.globalgold += 50
            elif item_choice == '2':
                name = 'Iron knife'
                damage1 = 4
                damage2 = 9
                cost = 100
                AdventureLevels.globalgold += 100
            elif item_choice == '3':
                name = 'Iron Short-Sword'
                damage1 = 6
                damage2 = 11
                cost = 250
                AdventureLevels.globalgold += 250
            else:
                name = 'Iron Broad-Sword'
                damage1 = 10
                damage2 = 17
                cost = 500
                AdventureLevels.globalgold += 500
            purchase = Weapon(name, cost, damage1, damage2)
            purchase.buy()
            AdventureLevels.save_charac(charac_name)


class Player:
    def __init__(self, name):
        self.level = AdventureLevels.globallevel
        self.name = name
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


class Loot(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.entered = False

    def on_enter(self, name):
        if self.entered:
            print(f'You found a chest, you approach it carefully...')
            print('You discover that you have already opened this chest!')
        else:
            print(f'You found a chest, you approach it carefully...')
            random_loot(AdventureLevels.character_name)
            self.entered = True


class Enemy(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.enemy_name = random.choice(enemy_possibilities_names)
        self.entered = False

    def on_enter(self, name):
        enemy_health = random.choice(enemy_possibilities_health)
        if self.entered:
            print(f'You found a dead {self.enemy_name}. It is currently being eaten by a grue, but it runs'
                  f' away as you approach.')
        else:
            print(
                f'You found a {self.enemy_name}, it has {str(enemy_health)} health and can deal '
                f'{" or ".join(map(str, enemy_possibilities_attack))} damage')
            player_health = 50
            while enemy_health > 0:
                player_attack = random.choice(player_possibilities_attack)
                chance = random.random()
                if chance <= 1 / 6:
                    player_attack = int(player_attack * 1.5)
                    critical = True
                else:
                    critical = False
                enemy_attack = random.choice(enemy_possibilities_attack)
                time.sleep(1.5)
                player_health -= enemy_attack
                enemy_health -= player_attack
                print(f'You did {player_attack} damage {"which was a CRITICAL HIT"if critical else""}, but received {enemy_attack} in return!\n'
                      f'You now have {player_health} health, the  {self.enemy_name} has {enemy_health} health!\n')
                time.sleep(1.5)
                if player_health <= 0 and enemy_health <= 0:
                    print(f'\033[31;10m You died\033[30;0m \n{random.choice(death_possibilities).format(self.enemy_name)}')
                    sys.exit(15)
                elif player_health <= 0:
                    print('AAGGHHHHhhhhhh...... \n'
                          '\033[31;10m You died \033[30;0m ')
                    sys.exit(15)
            print(f'You killed the {self.enemy_name}, congratulations! Keep looking for the exit.')
            gold_gained = random.choices(gold_possibilities, weights=(7, 6, 5, 4, 3, 2, 1), k=1)
            AdventureLevels.globalgold += gold_gained[0]
            print(f'You gained {gold_gained[0]} gold! You now have {AdventureLevels.globalgold} gold!')
            AdventureLevels.save_charac(AdventureLevels.character_name)
            self.entered = True


class Trapdoor(Tile):
    def on_enter(self, name):
        print('You found the trapdoor to the next level. Congratulations')
        exit_ = random.choice(exit_chance)
        if exit_ == 1:
            xp_gained = random.choices(xp_possibilities, weights=(14, 10, 5, 3, 1), k=2)
            AdventureLevels.globalxp += sum(xp_gained)
            print(f'You gain {sum(xp_gained)} xp, you now have {AdventureLevels.globalxp} xp.')
            AdventureLevels.save_charac(AdventureLevels.character_name)
            check_xp(AdventureLevels.character_name)
            sys.exit(100)

        elif exit_ == 0:
            print(f'But you fumbled and fell in head first, you cracked your skull!')
            print('\tYOU\033[31;10m DIED!\033[30;0m ')
            sys.exit(-100)


class Shop(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.foo = Shopping()

    def on_enter(self, name):
        print('You found the shop!')
        print(f'Welcome to the shop, you have {AdventureLevels.globalgold} gold to spend!')
        time.sleep(0.8)
        items = [
            'Rusty Knife (3 - 8 dmg) = 25 Gold',
            'Iron Knife (4 - 9 dmg) = 60 Gold',
            'Iron Short-sword (6 - 11 dmg) = 100 Gold',
            'Iron Broad-sword (10 - 17 dmg) = 200 Gold'
        ]
        print(f'\nThe items and gear you can buy are: ')
        for f in items:
            print(f)
            time.sleep(1)
        self.foo.item_choose()


class Shopping:
    def __init__(self):
        self.bought = False

    def item_choose(self):
        self.item_choice = input('\nEnter 1 for Rusty Knife.\nEnter 2 for Iron Knife.\nEnter 3 for Iron Short-sword.'
                                 '\nEnter 4 for Iron Broad-sword.\nEnter 5 to Exit.\n> ')
        if self.item_choice == '1':
            name = 'Rusty Knife'
            damage1 = 3
            damage2 = 8
            cost = 25
        elif self.item_choice == '2':
            name = 'Iron knife'
            damage1 = 4
            damage2 = 9
            cost = 60
        elif self.item_choice == '3':
            name = 'Iron Short-Sword'
            damage1 = 6
            damage2 = 11
            cost = 100
        elif self.item_choice == '4':
            name = 'Iron Broad-Sword'
            damage1 = 10
            damage2 = 17
            cost = 200
        elif self.item_choice == '5':
            print('Goodbye, if you ever want something else, just pop by again!')
            return
        else:
            print('Incorrect number, please leave then re-enter this tile to refresh the shop.')
            return
        purchase = Weapon(name, cost, damage1, damage2)
        purchase.buy()


class Weapon:
    def __init__(self, name, cost, damage1, damage2):
        self.damage2 = damage2
        self.damage1 = damage1
        self.cost = cost
        self.name = name

    @property
    def can_buy(self):
        return AdventureLevels.globalgold >= self.cost

    def buy(self):
        if self.can_buy:
            print(f'Successfully bought {self.name} for {self.cost}!')
            AdventureLevels.globalgold -= self.cost
            global player_possibilities_attack
            player_possibilities_attack = [*range(self.damage1, self.damage2 + 1)]
            AdventureLevels.save_charac(AdventureLevels.character_name)
        else:
            print(f'You do not have enough gold, you need {self.cost - AdventureLevels.globalgold} more gold.')


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
        return f'x=\033[36;10m{self.x}\033[0;10m y=\033[36;10m{self.y}\033[0;10m'


class RandomPos:
    def __init__(self, size):
        self.position = Position(randint(0, size), randint(0, size))


class SizeAndPos:
    def __init__(self, size1, size2):
        self.size_of_room = random.randint(size1, size2)
        time.sleep(1)
        self.starting_x = random.randrange(self.size_of_room)
        self.starting_y = random.randrange(self.size_of_room)


start_pos = SizeAndPos(17, 35)
pos_player = Position(start_pos.starting_x, start_pos.starting_y)
