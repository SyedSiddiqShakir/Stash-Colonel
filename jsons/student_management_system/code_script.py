import json

class Student():
    def __init__(self, id, name, age, grade, email):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.email = email
    def get_details(self):
        print(f"{self.name} with ID number of {self.id} is {self.age} yrs old and is in the {self.grade} grade and has email {self.email}")