import json
import os

source_file = f'{os.getcwd()}/items.en.json'
target_file = f'{os.getcwd()}/short_names.txt'

with open(source_file, 'r') as f:
    data = json.load(f)

short_names = []

for item in data:
    shortName = data[item]['shortName']
    short_names.append(shortName)

with open(target_file, 'w') as f:
    for name in short_names:
        f.write(name+'\n')

