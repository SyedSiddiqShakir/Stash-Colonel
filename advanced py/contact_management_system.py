#a new empty dict for contacts
directory = {}

#reading contacts in a file
contact_file = open('contact_list.txt', 'r')
contact_list = str(contact_file.readlines())

#writing contacts in a file
contact_file = open('contact_list.txt', 'a')

#func to add a new contact
def add_contact(name, email, phone_number):
    if name in directory:
        print(f'{name} already exists.')
    else:
        directory[name] = {'Phone': phone_number, 'Email': email}
        print(f"Contact {name} added successfully.")
        contact_file.write(f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}")

#func to search for a new contact and display the details
def search_contact(name):
    if name in directory:
        print(f"Contact found: Name: {name}\nPhone: {directory[name]['Phone']},\nEmail: {directory[name]['Email']} ")
    else:
        print(f"Contact {name} not found")

#func to update old contacts
def update_contact(name, email=None, phone_number=None):
    if name in directory:
        if email:
            directory[name]['Email'] = email
        if phone_number:
            phone_number = directory[name]['Phone']
        print(f"Contact {name} updated succesfully")
    else:
        print(f"Contact {name} not found.")

#func to delete a contact
def delete_contact(name):
    if name in directory:
        del directory[name]
        print(f"Contact {name} deleted successfully")
    else:
        print(f"Contact {name} not found.")

#func to display all contacts
def display_contact():
    if not directory:
        print("No contacts available")
    else:
        print("All contacts:\n")
        for name, details in directory.items():
            print(f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']} ")

#Exec program
while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name:")
        email = input("Enter Email:")
        phone_number = input("Enter Phone Number:")
        add_contact(name, email, phone_number)
    elif choice == '2':
        name = input("Enter name:") 
        search_contact(name)
    elif choice == '3':
        name = input("Enter name:")
        email = input("Enter Email:")
        phone_number = input("Enter Phone Number:")
        update_contact(name, email, phone_number)
    elif choice == '4':
        name = input("Enter name:")
        delete_contact(name)
    elif choice == '5':
        display_contact()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid Choice, Please try again.")