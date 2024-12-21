import json

class Person():
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(data["name"], data["age"], data["email"])
        
trash_string = '{"name": "siddiq", "age": 25, "email": "syedsiddiqshakir@gmail.com"}'
my_person = Person.from_json(trash_string)

print(f"Name: {my_person.name}")