import json

def write_json(data, filename="01_names.json"):
    with open (filename, "w")as f:
        json.dump(data, f, indent=4)

with open("01_names.json") as json_file:
    data = json.load(json_file)
    temp = data["names"]
    y = {"firstname": "Biden", "age": 93}
    temp.append(y)
write_json(data)