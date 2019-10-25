import random
import time
import sys
from SharkLearn.AdventureLevels import jacklevel, Sharkboundlevel, Psuedolevel, Annalevel
from SharkLearn.Classes2 import RandomPos, pl2, pl1, pl3, pl4, SizeAndPos, Position, start_pos, Levels

# Player Selection

player_selection = input("Select the number of a player:\n\t\033[1;34;10m"
                             "1.\033[0;10m jack\n\t\033[1;34;10m"
                             "2.\033[0;10m Sharkbound\n\t\033[1;34;10m"
                             "3.\033[0;10m Psuedo\n\t\033[1;34;10m"
                             "4.\033[0;10m Anna\n> ")
if player_selection == '1':
    player_level = jacklevel
    player = pl1

elif player_selection == '2':
    player_level = Sharkboundlevel
    player = pl2

elif player_selection == '3':
    player_level = Psuedolevel
    player = pl3

elif player_selection == '4':
    player_level = Annalevel
    player = pl4

else:
    print('Invalid Number')
    sys.exit(25)

# Starting text and level

print('You wake up in a dark room, with very faint torches on the walls, you stand up,'
      ' and walk through the door-frame in-front of you.....'
      )
time.sleep(1)
print(f'You are level {player_level}')

# Controls

print('\nThe controls are\033[34;10m w\033[30;0m (up),\033[34;10m a\033[30;0m (left),'
      '\033[34;10m s\033[30;0m (down),\033[34;10m d\033[30;0m (right) '
      'and\033[34;10m /size\033[30;0m (gets room size)\n')
time.sleep(0.5)

# Trap Code

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

trap = random.choice(traps)

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

trap_position = RandomPos(start_pos.size_of_room)
trapdoor_position1 = RandomPos(start_pos.size_of_room)
trapdoor_position2 = RandomPos(start_pos.size_of_room)
trapdoor_position3 = RandomPos(start_pos.size_of_room)
levels = Levels()


def touch_wall():
    if player.position.x == start_pos.size_of_room + 1 or player.position.y == start_pos.size_of_room + 1:
        print('\nYou touched the spike walls.\n\033[31;10m YOU DIED!')
        sys.exit(15)
    if player.position.x == -1 or player.position.y == -1:
        print('\nYou touched the spike walls.\n\033[31;10m YOU DIED!')
        sys.exit(15)


def touch_trap():
    if player.position.x == trap_position.x_pos_random and player.position.y == trap_position.y_pos_random:
        print(f'You {trap}')
        escape = random.choice(escape_chance)
        if escape == 0:
            print('\tBut you\033[32;10m ESCAPED!')
        elif escape == 1:
            print('\tYOU\033[31;10m DIED!')
            sys.exit(15)


def touch_trapdoor():
    if player.position.x == trapdoor_position1.x_pos_random and player.position.y == trapdoor_position1.y_pos_random:
        if player.position.x != trap_position.x_pos_random and player.position.y != trap_position.y_pos_random:
            print('You found the trapdoor to the next level. Congratulations')
            print(f'You have completed level {player_level}! Hooray! You are now level {player_level + 1}')
            player.level += 1
            levels.open_trapdoor(player.level, player.name)
            sys.exit(100)
        elif player.position.x == trapdoor_position2.x_pos_random and player.position.y == trapdoor_position2.y_pos_random:
            if player.position.x != trap_position.x_pos_random and player.position.y != trap_position.y_pos_random:
                print('You found the trapdoor to the next level. Congratulations')
                print(f'You have completed level {player_level}! Hooray! You are now level {player_level + 1}')
                player.level += 1
                levels.open_trapdoor(player.level, player.name)
                sys.exit(100)

            elif player.position.x == trapdoor_position3.x_pos_random and player.position.y == trapdoor_position3.y_pos_random:
                if player.position.x != trap_position.x_pos_random and player.position.y != trap_position.y_pos_random:
                    print('You found the trapdoor to the next level. Congratulations')
                    print(f'You have completed level {player_level}! Hooray! You are now level {player_level + 1}')
                    player.level += 1
                    levels.open_trapdoor(player.level, player.name)
                    sys.exit(100)


# print(f'{trapdoor_position1.x_pos_random}, {trapdoor_position1.y_pos_random} and {trapdoor_position2.x_pos_random}, {trapdoor_position2.y_pos_random} and {trapdoor_position3.x_pos_random}, {trapdoor_position3.y_pos_random}')
print(f'The room is {temp}, {brightness}, and there might be a trap!')
print(
    f'\nYou start in a room that is\033[32;10m {start_pos.size_of_room}\033[30;0m tiles wide and\033[32;10m {start_pos.size_of_room}\033[30;0m tiles high \n'
    f'Your starting position is x: \033[32;10m{start_pos.starting_x}\033[30;0m, and y: \033[32;10m{start_pos.starting_y}.\033[30;0m \n'
    f'You can go from\033[32;10m 0 to {start_pos.size_of_room}\033[30;0m in any direction.\n')
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
        touch_wall()
        touch_trap()
        touch_trapdoor()
        print(
            f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}\033[30;0m')

    elif direction1 == 's':
        player.position.move_down()
        touch_wall()
        touch_trap()
        touch_trapdoor()
        print(
            f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}\033[30;0m')

    elif direction1 == 'a':
        player.position.move_left()
        touch_wall()
        touch_trap()
        touch_trapdoor()
        print(
            f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}\033[30;0m')

    elif direction1 == 'd':
        player.position.move_right()
        touch_wall()
        touch_trap()
        touch_trapdoor()
        print(
            f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}\033[30;0m')
