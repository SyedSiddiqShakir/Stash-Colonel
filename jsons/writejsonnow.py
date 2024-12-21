import json

#function to open json file and dump data in it
def write_json(data, filename="01_names.json"):
    with open (filename, "w")as f:
        json.dump(data, f, indent=4)

#codeblock opens json file and adds data to json file
with open("01_names.json") as json_file:
    data = json.load(json_file)
    temp = data["names"]
    y = {"firstname": "Biden", "age": 93}
    temp.append(y)
write_json(data)