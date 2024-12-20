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
new_person = Person("siddiq", 25, "syedsiddiqshakir@gmail.com")
print(new_person.to_json())