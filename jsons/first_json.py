import json

file = "01_names.json"

with open (file, 'r') as json_file:
    data = json.load(json_file)
    print(data)