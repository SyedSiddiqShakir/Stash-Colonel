import json

pydic = {
    "name": "Charlie",
    "age": 28,
    "email": "charlie@example.com"
}

with open("my_person.json", "w") as my_file:
    json.dump(pydic, my_file, indent=4)

print("JSON data saved to 'person.json'.")

