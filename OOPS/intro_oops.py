class employee(object):
    def __init__(self, name, age: int, gender, salary: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
    
    def get_details(self):
        print(f"{self.name} is {self.age} years old, is {self.gender} and earns {self.salary}$/month")

emp1 = employee('Maaz', 25, 'Male', 1200)
emp2 = employee('K2', 20, 'Female', 1400)

emp1.get_details()
emp2.get_details()

# class Employee:
#     def __init__(self, name, age, department):
#         self.name = name
#         self.age = age
#         self.department = department

#     def get_details(self):
#         return f"Name: {self.name}, Age: {self.age}, Department: {self.department}"

# # Create objects
# emp1 = Employee("Alice", 30, "HR")
# emp2 = Employee("Bob", 25, "Engineering")

# # Print details
# print(emp1.get_details())
# print(emp2.get_details())
