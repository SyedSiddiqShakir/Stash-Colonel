import json

#person class to create people as objects
class Person():
    number_of_people = 0

    #attributes of people
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        dic = {                                        #adds the person to a python dictionary
            "name": name, "age": age, "email": email
        }
        with open("people.json", "w") as file:         #dumps the data into the json file
            json.dump(dic, file, indent=4)
        Person.number_of_people += 1

    #view all listed people
    @classmethod
    def view_people(cls):                             #prints the json file
        with open("people.json", "r") as file:              
            to_print_people = json.load(file)
            print(to_print_people)
    
    @classmethod
    def no_of_people(cls):
        print(f"Number of people are: {cls.number_of_people}")

#multiple intances created but only the latest stored due to overlapping in json file
maaz = Person("siddiq", 25, "sss@gmail.com")   
baba = Person("abdussalam", 23, "sas@gmail.com")
k2 = Person("k2", 20, "k2@gmail.com")
omar = Person("omar", 26, "omar@gmail.com")

Person.view_people()
Person.no_of_people()