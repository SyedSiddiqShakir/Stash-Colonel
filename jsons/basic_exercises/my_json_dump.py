import json

pydic = {
    "name": "siddiq",
    "age": "25",
    "email": "syedsiddiqshakir@gmail.com"
}

json_string = json.dumps(pydic, indent=4)

print(json_string)
print(pydic)