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
    with open(pathlib.Path(f'Player_Saves\\{charac_name}.txt'), 'w') as file:
        file.write(json.dumps(saved_data))


def leaderboards_load_save():
    list_ = os.listdir('C:/Users/jacks/PycharmProjects/Adventure-Mini-Game/SharkLearn/Player_Saves')
    lead_lvl = -1
    lead_lvl_name = f'Default: {lead_lvl}'
    lead_gold = -1
    lead_gold_name = f'Default: {lead_gold}'
    for i in list_:
        path = pathlib.Path(f'Player_Saves/{i}')
        with open(path, 'r') as file:
            data = json.load(file)
            if lead_lvl < data[0]:
                lead_lvl = data[0]
                lead_lvl_name = f'Highest Leveled Player: {path.stem} with {lead_lvl} levels!'
            if lead_gold < data[1]:
                lead_gold = data[1]
                lead_gold_name = f'Richest Player: {path.stem} with {lead_gold} gold!'
    print(f'\nLeaderboards:\n{lead_lvl_name}\n{lead_gold_name}')



character_name = None
globallevel = None
globalgold = None
globalxp = None
prev_req_xp = None
