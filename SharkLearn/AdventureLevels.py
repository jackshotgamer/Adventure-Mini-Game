import json
import os


if not os.path.exists('saved_data.txt'):
    with open('saved_data.txt', 'w') as saved_data:
        saved_data.write('[1, 0, 0, 5]')
with open('saved_data.txt', 'r') as saved_data1:
    data = json.load(saved_data1)
    globallevel = data[0]
    globalgold = data[1]
    globalxp = data[2]
    prev_req_xp = data[3]
