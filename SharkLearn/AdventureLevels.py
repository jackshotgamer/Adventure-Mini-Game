import json
import os
import pathlib
import SharkLearn.Player_Saves


def load_charac(charac_name):
    global globallevel, globalgold, globalxp, prev_req_xp, character_name
    character_name = charac_name
    if not pathlib.Path(f'Player_Saves/{charac_name}.txt').exists():
        with open(pathlib.Path(f'Player_Saves\\{charac_name}.txt'), 'w') as saved_data:
            saved_data.write('[1, 0, 0, 5]')
    with open(pathlib.Path(f'Player_Saves\\{charac_name}.txt'), 'r') as saved_data1:
        data = json.load(saved_data1)
        globallevel = data[0]
        globalgold = data[1]
        globalxp = data[2]
        prev_req_xp = data[3]


def save_charac(charac_name):
    saved_data = (
        globallevel,
        globalgold,
        globalxp,
        prev_req_xp
    )
    with open(pathlib.Path(f'Player_Saves\\{charac_name}.txt'), 'w') as file1:
        file1.write(json.dumps(saved_data))


def leaderboards_load_save():
    list_ = os.listdir('C:/Users/jacks/PycharmProjects/Adventure-Mini-Game/SharkLearn/Player_Saves')
    number_of_files = len(list_)
    for i in range(number_of_files):
        with open(pathlib.Path(f'Player_Saves/'), 'r') as file3:
            data = json.load(file3)
        with open(pathlib.Path(f'leaderboards.txt'), 'r+') as file4:
            file4.write(json.dumps(data))
    with open(pathlib.Path(f'leaderboards.txt'), 'r') as file5:
        data = json.load(file5)
        print(f'1: {data}')
        print('Highest leveled played: ')
leaderboards_load_save()

character_name = None
globallevel = None
globalgold = None
globalxp = None
prev_req_xp = None
