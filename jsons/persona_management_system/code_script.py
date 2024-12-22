import json
class Persona:
    def __init__(self, name, age, email, occupation):                         # Main persona class
        self.name = name
        self.age = age
        self.email = email
        self.occupation = occupation

    @staticmethod
    def find_no_of_people():                                                  #Returns the number of people stored in the JSON file        
        try:
            with open("people.json", "r") as file:
                data = json.load(file)
                return len(data)                                              # Return the number of people
        except FileNotFoundError:
            print("No people found in the file.")
            return 0
        except json.JSONDecodeError:
            print("Error decoding JSON file.")
            return 0

    def to_dict(self):                                                        #Convert the Persona object to a dictionary
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "occupation": self.occupation
        }

    @classmethod
    def from_dict(cls, data):                                                 #Create a Persona object from a dictionary
        return cls(data["name"], data["age"], data["email"], data["occupation"])

class Person_Management:
    def __init__(self, filename="people.json"):
        self.filename = filename
        self.people = self.load_persons()

    def load_persons(self):                                                   #Load personas from the JSON file
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Persona.from_dict(person) for person in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty list.")
            return []

    def save_persons(self):                                                    #Save all personas to the JSON file        
        with open(self.filename, "w") as file:
            data = [person.to_dict() for person in self.people]
            json.dump(data, file, indent=4)

    def add_persona(self, name, age, email, occupation):                       #Add a new persona to the list
        data = Persona(name, age, email, occupation)
        self.people.append(data)
        self.save_persons()
        print(f"Person '{name}' added successfully.")

    def update_person(self, name, age=None, email=None, occupation=None):      #Update details of an existing person
        person = self.search_person(name)
        if person:
            if age:
                person.age = age
            if email:
                person.email = email
            if occupation:
                person.occupation = occupation
            self.save_persons()
            print(f"Person '{name}' updated successfully.")

    def delete_person(self, name):                                             #Delete a person by name        
        person = self.search_person(name)
        if person:
            self.people.remove(person)
            self.save_persons()
            print(f"Person '{name}' deleted successfully.")

    def search_person(self, name):                                             #Search for a person by name        
        for person in self.people:
            if person.name.lower() == name.lower():
                print(f"Found Person: Name: {person.name}, Age: {person.age}, Email: {person.email}, Occupation: {person.occupation}")
                return person
        print(f"No person with name '{name}' found.")
        return None

    def view_persons(self):                                                    #View all personas        
        if not self.people:
            print("No people found.")
        else:
            print("List of People:")
            for person in self.people:
                print(f"Name: {person.name}, Age: {person.age}, Email: {person.email}, Occupation: {person.occupation}")


def main():
    manager = Person_Management()

    while True:
        print("\n--- Persona Management System ---")
        print("1. Add Persona")
        print("2. View All Personas")
        print("3. Search Persona")
        print("4. Update Persona")
        print("5. Delete Persona")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            occupation = input("Enter occupation: ")
            manager.add_persona(name, age, email, occupation)

        elif choice == "2":
            manager.view_persons()

        elif choice == "3":
            name = input("Enter name to search: ")
            manager.search_person(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            age = input("Enter new age (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            occupation = input("Enter new occupation (leave blank to keep unchanged): ")
            manager.update_person(
                name,
                age=int(age) if age else None,
                email=email if email else None,
                occupation=occupation if occupation else None
            )

        elif choice == "5":
            name = input("Enter name to delete: ")
            manager.delete_person(name)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()