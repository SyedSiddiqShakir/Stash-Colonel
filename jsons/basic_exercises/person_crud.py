import json

class Person():
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email
        }

    @classmethod    
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["email"])
    
class PersonManager():
    def __init__(self, filename="person.json"):
        self.filename = filename
        self.persons = self.load_persons()
        
    def load_persons(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Person.from_dict(person) for person in data]
        except FileNotFoundError:
            return []  # Start with an empty list if file doesn't exist
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty list.")
            return []
    
    def save_person(self):
        with open(self.filename, "w") as file:
            data = [person.to_dict() for person in self.persons]
            json.dump(data, file, indent=4)
    
    def add_person(self, name, age, email):
        self.persons.append(Person(name, age, email))
        self.save_person()
        print(f"Person '{name}' saved.")
    
    def view_persons(self):
        if not self.persons:
            print("No person found")
        else:
            for person in self.persons:
                print(f"Found Person: Name: {person.name}, Age: {person.age}, Email: {person.email}")
    
    def search_person(self, name):
        for person in self.persons:
            if person.name.lower() == name.lower():
                print(f"Found Person: Name: {person.name}, Age: {person.age}, Email: {person.email}")
                return person
        print(f"No person with name '{name}' found.")
        return None
    
    def delete_person(self, name):
        person = self.search_person(name)
        if person:
            self.persons.remove(person)
            self.save_person()
            print(f"Person '{name}' deleted.")

    def update_person(self, name, age=None, email=None):
        """Update details of an existing person."""
        person = self.search_person(name)
        if person:
            if age:
                person.age = age
            if email:
                person.email = email
            self.save_persons()
            print(f"Person '{name}' updated successfully!")
def main():
    manager = PersonManager()

    while True:
        print("\n--- Person Data Manager ---")
        print("1. Add Person")
        print("2. View All Persons")
        print("3. Search Person")
        print("4. Update Person")
        print("5. Delete Person")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            manager.add_person(name, age, email)

        elif choice == "2":
            manager.view_persons()

        elif choice == "3":
            name = input("Enter name to search: ")
            manager.search_person(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            age = input("Enter new age (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            manager.update_person(
                name,
                age=int(age) if age else None,
                email=email if email else None,
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