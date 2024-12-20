import json
class Person():
    def __init__(self, name, age: int, email):
        self.name = name
        self.age = age
        self.email = email

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return 