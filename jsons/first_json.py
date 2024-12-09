import json

# file = "01_names.json"

def write_json(data, filename="new_json_file.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# with open (file, 'r') as json_file:
#     data = json.load(json_file)
#     write_json(data)

data = ["Bob", "Marley"]
write_json(data)