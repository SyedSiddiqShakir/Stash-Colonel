import json

#main persona class
class Persona():
    def __init__(self, name, age, email, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.email = email
    
    #converts the persona object to a json string
    def add_persona(self):
        return json.dumps({
            "name": self.name,
            "age": self.age,
            "occupation": self.occupation,
            "email": self.email
        })
    
    #creates a Persona object from a json string
    @classmethod
    def from_json_string(cls, json_string):
        data = json.loads(json_string)
        return cls(data["name"], data["age"], data["email"], data["occupation"])