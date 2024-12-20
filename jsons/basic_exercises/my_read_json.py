import json

with open("my_person.json", "r") as my_file:
    my_lines = json.load(my_file)

print(my_lines)