import json
class Person():
    def __init__(self, name, age: int, email):
        self.name = name
        self.age = age
        self.email = email

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "age": self.age,
            "email": self.email
        }, indent=4)
    
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(data["name"], data["age"], data["email"])


new_person = Person("siddiq", 25, "syedsiddiqshakir@gmail.com")
print(new_person.to_json())
