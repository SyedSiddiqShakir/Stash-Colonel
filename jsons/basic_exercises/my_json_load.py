import json

json_string = '{"name": "siddiq", "age": 25, "uni": "WHZ"}'

person = json.loads(json_string)

#print(person['name'])
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"University: {person['uni']}")