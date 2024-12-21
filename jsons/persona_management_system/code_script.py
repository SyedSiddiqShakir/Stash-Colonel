import json

#main persona class
class Persona():
    no_of_people = 0
    def __init__(self, name, age, email, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.email = email
    
    def to_dict(self):                            #to convert instance information to a dictionary 
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "occupation": self.occupation
        }
    
    @classmethod
    def from_dict(cls, data):                     #to convert dictionary to an instance
        return cls(data["name"], data["age"], data["email"], data["occupation"])

class Person_Management():                         #class dedicated only for managing the personas
    def __init__(self, filename="people.json"):
        self.filename = filename
        self.people = self.load_person()
    
    def load_person(self):                         #loads the existing personas to json
        try:
            with open(self.filename, "r") as file:
                loaded_people = json.load(file)
                for person in file:
                    return Persona.to_dict(person)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:                
            print("Error decoding JSON, starting with a new list")
            return []
        
    # def save_person(self):                         #saves all personas to JSON
    #     with open(self.filename, "w") as file:
    #         for persons in self.people:
    #             data = Persona.to_dict(persons)    
    #         json.dump(data, file, indent=4)
            
    def add_persona(self, name, age, email, occupation):
        data = Persona.to_dict()
        self.people.append(data)
        with open(self.filename, "w") as file:
            for persons in self.people:
                    data = Persona.to_dict(persons)    
            json.dump(data, file, indent=4)

            
            

    # #converts the persona object to a json string
    # def add_persona(self):
    #     return json.dumps({
    #         "name": self.name,
    #         "age": self.age,
    #         "occupation": self.occupation,
    #         "email": self.email
    #     })
    
    # #creates a Persona object from a json string
    # @classmethod
    # def from_json_string(cls, json_string):
    #     data = json.loads(json_string)
    #     return cls(data["name"], data["age"], data["email"], data["occupation"])