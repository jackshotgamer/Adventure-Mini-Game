import random
import time
import sys
from SharkLearn import AdventureLevels
from SharkLearn.Classes import RandomPos, pl2, pl1, pl3, pl4, SizeAndPos, Position, start_pos, Trap, Trapdoor
import json

list_of_positions = []


def random_pos(size_of_rooms):
    while True:
        random_p = RandomPos(size_of_rooms)
        if random_p.position in list_of_positions:
            continue
        else:
            list_of_positions.append(random_p.position)
            # random.shuffle(list_of_positions)
            return random_p


# Player Selection

player_selection = input("Select the number of a player:\n\t\033[1;34;10m"
                         "1.\033[0;10m jack\n\t\033[1;34;10m"
                         "2.\033[0;10m Sharkbound\n\t\033[1;34;10m"
                         "3.\033[0;10m Psuedo\n\t\033[1;34;10m"
                         "4.\033[0;10m Anna\n> ")
if player_selection == '1':
    player_level = AdventureLevels.globallevel
    player = pl1

elif player_selection == '2':
    player_level = AdventureLevels.globallevel
    player = pl2

elif player_selection == '3':
    player_level = AdventureLevels.globallevel
    player = pl3

elif player_selection == '4':
    player_level = AdventureLevels.globallevel
    player = pl4

else:
    print('Invalid Number')
    sys.exit(25)

# Starting text and level

print('You wake up in a dark room, with very faint torches on the walls, you stand up,'
      ' and walk through the door-frame in-front of you.....'
      )
time.sleep(1)
print(
    f'You are level {player_level}, you have {AdventureLevels.globalgold} gold, and your xp count is {AdventureLevels.globalxp}')

# Controls

print('\nThe controls are\033[34;10m w\033[30;0m (up),\033[34;10m a\033[30;0m (left),'
      '\033[34;10m s\033[30;0m (down),\033[34;10m d\033[30;0m (right) '
      'and\033[34;10m /size\033[30;0m (gets room size)\n')
time.sleep(1.9)

# Gold Code

gold_possibilities = (
    5,
    10,
    15,
    25,
    50,
    75,
    100,
    150
)

# Enemy Code

enemy_possibilities_health = (
    10,
    20,
    30,
    40,
    50
)
enemy_health = random.choice(enemy_possibilities_health)

enemy_possibilities_attack = (
    2,
    3,
    5,
    6
)
enemy_attack = random.choice(enemy_possibilities_attack)

enemy_possibilities_names = (
    'Ogre',
    'Dragon',
    'Troll',
    'Zombie',
    'Super-Mob'
)
enemy_name = random.choice(enemy_possibilities_names)

# Temperature

temps = (
    'cold',
    'hot',
    'cold',
    'hot',
    'cold',
    'hot',
    'freezing',
    'boiling',
)
temp = random.choice(temps)

# Brightness

brights = (
    'dim',
    'dim',
    'dim',
    'dim',
    'bright',
    'bright',
    'bright',
    'just about see-able'
)

brightness = random.choice(brights)

# Room Code

tiles = [Trap(*random_pos(start_pos.size_of_room).position.position),
         Trapdoor(*random_pos(start_pos.size_of_room).position.position)]


enemy_position = random_pos(start_pos.size_of_room)


def touch_enemy():
    if player.position == enemy_position.position:
        print(
            f'You found a {enemy_name}, it has {str(enemy_health)} health and can deal {" or ".join(map(str, enemy_possibilities_attack))} damage')


def on_move():
    if player.position.x == start_pos.size_of_room + 1 or player.position.y == start_pos.size_of_room + 1:
        print('\nYou touched the spike walls.\n\033[31;10m YOU DIED!')
        sys.exit(15)
    if player.position.x == -1 or player.position.y == -1:
        print('\nYou touched the spike walls.\n\033[31;10m YOU DIED!')
        sys.exit(15)
    for x in tiles:
        if player.position == x.position:
            x.on_enter(player.name)
    touch_enemy()
    print(
        f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}\033[30;0m')


print(f'{tiles[1].position}')
print(f'The room is {temp}, {brightness}, and there might be a trap!')
print(
    f'\nYou start in a room that is\033[32;10m {start_pos.size_of_room}\033[30;0m tiles wide and\033[32;10m {start_pos.size_of_room}\033[30;0m tiles high \n'
    f'Your starting position is x: \033[32;10m{start_pos.starting_x}\033[30;0m, and y: \033[32;10m{start_pos.starting_y}.\033[30;0m \n'
    f'You can go from\033[32;10m 0 to {start_pos.size_of_room}\033[30;0m in any direction.\n')
print(list_of_positions)
in_room = True
while in_room:
    w_a_s_d = input('Enter a control: ')
    if w_a_s_d == 'w':
        print(f'\nYou chose up')
        direction1 = 'w'
    elif w_a_s_d == 'a':
        print(f'\nYou chose left')
        direction1 = 'a'
    elif w_a_s_d == 's':
        print(f'\nYou chose down')
        direction1 = 's'
    elif w_a_s_d == 'd':
        print(f'\nYou chose right')
        direction1 = 'd'
    elif w_a_s_d == '/size':
        print(
            f'The room size is \033[32;10m{start_pos.size_of_room}\033[30;0m wide and \033[32;10m{start_pos.size_of_room}\033[30;0m high.')
        continue
    else:
        print('\nInvalid Control')
        continue
    # if choosing

    if direction1 == 'w':
        player.position.move_up()

    elif direction1 == 's':
        player.position.move_down()

    elif direction1 == 'a':
        player.position.move_left()

    elif direction1 == 'd':
        player.position.move_right()
    on_move()
