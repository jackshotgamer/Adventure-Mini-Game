import random
import time
import sys
from SharkLearn import AdventureLevels
from SharkLearn.Classes import RandomPos, start_pos, Trap, Trapdoor, Enemy, Loot, Shop, Player

list_of_positions = []


def random_pos(size_of_rooms):
    while True:
        random_p = RandomPos(size_of_rooms)
        if random_p.position in list_of_positions:
            continue
        else:
            list_of_positions.append(random_p.position)
            #random.shuffle(list_of_positions)
            return random_p


# Player Selection ( Not Ready! Temp Solution! )

player_selection = input("Please input your character name: ")
AdventureLevels.load_charac(player_selection)
player = Player(player_selection)

# Starting text and level

player_level = AdventureLevels.globallevel

print('You wake up in a dark room, with very faint torches on the walls, you stand up,'
      ' and walk through the door-frame in-front of you.....'
      )
time.sleep(1)
print(
    f'You are level {player_level}, you have {AdventureLevels.globalgold} gold, and your xp count is '
    f'{AdventureLevels.globalxp}')

# Controls

print('\nThe controls are: \n\033[34;10m w\033[30;0m (up),\033[34;10m a\033[30;0m (left),'
      '\033[34;10m s\033[30;0m (down),\033[34;10m d\033[30;0m (right) \n'
      '\nThe commands you can use are: \n\033[34;10m /size\033[30;0m (Gets room size)\n'
      '\033[34;10m /help\033[30;0m (Shows the commands)\n'
      '\033[34;10m /positions\033[30;0m (Lists the random positions)\n'
      '\033[34;10m /leaderboard\033[30;0m (Shows the leaderboard)\n')
time.sleep(2.3)

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
    'bright',
    'bright',
    'bright',
    'bright',
    'bright',
    'dim',
    'dim',
    'dim',
    'pitch black'
)

brightness = random.choice(brights)

# Room Code

if player.level <= 5:
    tiles = [Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trapdoor(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position)]
elif player.level <= 10:
    tiles = [Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trapdoor(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position)]
elif player.level <= 20:
    tiles = [Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trapdoor(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position)]
elif player.level < 40:
    tiles = [Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trapdoor(*random_pos(start_pos.size_of_room).position.position),
             Trapdoor(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position)]
else:
    tiles = [Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trap(*random_pos(start_pos.size_of_room).position.position),
             Trapdoor(*random_pos(start_pos.size_of_room).position.position),
             Trapdoor(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Enemy(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Loot(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position),
             Shop(*random_pos(start_pos.size_of_room).position.position)]
shops = []
for a in tiles:
    if isinstance(a, Shop):
        shops.append(a.position)


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
    print(
        f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}'
        f'\033[30;0m')


print(f'The room is {temp}, {brightness}, and there might be a trap!\n')
print('The positions of random things are: ')
print(", ".join(map(str, list_of_positions)))
print(f'The Shops are at {", ".join(map(str , shops))}')
print(
    f'\nYou start in a room that is\033[32;10m {start_pos.size_of_room}\033[30;0m tiles wide and\033[32;10m'
    f' {start_pos.size_of_room}\033[30;0m tiles high \n'
    f'Your starting position is x: \033[32;10m{start_pos.starting_x}\033[30;0m, and y: '
    f'\033[32;10m{start_pos.starting_y}.\033[30;0m \n'
    f'You can go from\033[32;10m 0 to {start_pos.size_of_room}\033[30;0m in any direction.\n')
moves = 0
in_room = True
while in_room:
    w_a_s_d = input('Enter a control: ')
    if w_a_s_d == 'w':
        print(f'\nYou chose up')
        direction1 = 'w'
        if temp == 'freezing':
            moves += 1
            area = int(start_pos.size_of_room * start_pos.size_of_room) // 4
            print(f'Since the room is {temp}, you have {area - moves} moves left before the '
                  f'temperature kills you!')
            if moves >= int(start_pos.size_of_room * start_pos.size_of_room) // 4:
                print(f'Out of moves, you succumbed to the {temp} temperature')
                sys.exit(20)
        elif temp == 'boiling':
            moves += 1
            area = int(start_pos.size_of_room * start_pos.size_of_room) // 4
            print(f'Since the room is {temp}, you have {area - moves} moves left before the '
                  f'temperature kills you!')
            if moves >= int(start_pos.size_of_room * start_pos.size_of_room) // 4:
                print(f'Out of moves, you succumbed to the {temp} temperature')
                sys.exit(20)
    elif w_a_s_d == 'a':
        print(f'\nYou chose left')
        direction1 = 'a'
        if temp == 'freezing':
            moves += 1
            area = int(start_pos.size_of_room * start_pos.size_of_room) // 4
            print(f'Since the room is {temp}, you have {area - moves} moves left before the '
                  f'temperature kills you!')
            if moves >= int(start_pos.size_of_room * start_pos.size_of_room) // 4:
                print(f'Out of moves, you succumbed to the {temp} temperature')
                sys.exit(20)
        elif temp == 'boiling':
            moves += 1
            area = int(start_pos.size_of_room * start_pos.size_of_room) // 4
            print(f'Since the room is {temp}, you have {area - moves} moves left before the '
                  f'temperature kills you!')
            if moves >= int(start_pos.size_of_room * start_pos.size_of_room) // 4:
                print(f'Out of moves, you succumbed to the {temp} temperature')
                sys.exit(20)
    elif w_a_s_d == 's':
        print(f'\nYou chose down')
        direction1 = 's'
        if temp == 'freezing':
            moves += 1
            area = int(start_pos.size_of_room * start_pos.size_of_room) // 4
            print(f'Since the room is {temp}, you have {area - moves} moves left before the '
                  f'temperature kills you!')
            if moves >= int(start_pos.size_of_room * start_pos.size_of_room) // 4:
                print(f'Out of moves, you succumbed to the {temp} temperature')
                sys.exit(20)
        elif temp == 'boiling':
            moves += 1
            area = int(start_pos.size_of_room * start_pos.size_of_room) // 4
            print(f'Since the room is {temp}, you have {area - moves} moves left before the '
                  f'temperature kills you!')
            if moves >= int(start_pos.size_of_room * start_pos.size_of_room) // 4:
                print(f'Out of moves, you succumbed to the {temp} temperature')
                sys.exit(20)
    elif w_a_s_d == 'd':
        print(f'\nYou chose right')
        direction1 = 'd'
        if temp == 'freezing':
            moves += 1
            area = int(start_pos.size_of_room * start_pos.size_of_room) // 4
            print(f'Since the room is {temp}, you have {area - moves} moves left before the '
                  f'temperature kills you!')
            if moves >= int(start_pos.size_of_room * start_pos.size_of_room) // 4:
                print(f'Out of moves, you succumbed to the {temp} temperature')
                sys.exit(20)
        elif temp == 'boiling':
            moves += 1
            area = int(start_pos.size_of_room * start_pos.size_of_room) // 4
            print(f'Since the room is {temp}, you have {area - moves} moves left before the '
                  f'temperature kills you!')
            if moves >= int(start_pos.size_of_room * start_pos.size_of_room) // 4:
                print(f'Out of moves, you succumbed to the {temp} temperature')
                sys.exit(20)
    elif w_a_s_d == '/size':
        print(
            f'The room size is \033[32;10m{start_pos.size_of_room}\033[30;0m wide and \033[32;10m'
            f'{start_pos.size_of_room}\033[30;0m high.')
        print(
            f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}'
            f'\033[30;0m')
        continue
    elif w_a_s_d == '/help':
        print('\nThe controls are: \n\033[34;10m w\033[30;0m (up),\033[34;10m a\033[30;0m (left),'
              '\033[34;10m s\033[30;0m (down),\033[34;10m d\033[30;0m (right)'
              '\nThe commands you can use are: \n\033[34;10m /size\033[30;0m (Gets room size)'
              '\033[34;10m /help\033[30;0m (Shows the commands)\n'
              '\033[34;10m /positions\033[30;0m (Lists the random positions)\n'
              '\033[34;10m /leaderboard\033[30;0m (Shows the leaderboard)\n')
        print(
            f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}'
            f'\033[30;0m')
        continue
    elif w_a_s_d == '/positions':
        if brightness == 'bright':
            print('\nThe positions of random things are: ')
            print(", ".join(map(str, list_of_positions)), '')
            print(f'The Shops are at {", ".join(map(str, shops))}\n')
            print(
                f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}'
                f'\033[30;0m')
        else:
            print(f'The room is {brightness}, and you cannot make out anything')
            print(f'The Shops are at {", ".join(map(str, shops))}\n')
            print(
                f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}'
                f'\033[30;0m')
        continue
    elif w_a_s_d == '/leaderboard':
        AdventureLevels.leaderboards_load_save()
        print(
            f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}'
            f'\033[30;0m')
        continue
    else:
        print('\nInvalid Control')
        print(
            f'\033[30;0m You are now x: \033[32;10m{player.position.x}\033[30;0m, y: \033[32;10m{player.position.y}'
            f'\033[30;0m')
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
