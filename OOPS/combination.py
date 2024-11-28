class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_info(self):
        return f"{self.name} is {self.age} years old and is {self.gender}"

class Student(Person):
    def __init__(self, name, age, gender, sem):
        super().__init__(name, age, gender)
        self.sem = sem
    def get_info(self):
        return f"{super().get_info()} and is enrolled in {self.sem} semester"

class Teacher(Person):
    def __init__(self, name, age, gender, subject, year):
        super().__init__(name, age, gender)
        self.subject = subject
        self.year = year
    def get_info(self):
        return f"{super().get_info()} who teaches {self.subject} since {self.year}"

siddiq = Student('siddiq', 25, 'male', 'Master\'s first')
wasinger = Teacher('Rainer', 40, 'male', 'HCI', 2007)
sandra = Teacher('braun', 38, 'female', 'deutsch', 2012)
baum = Person('Heiko', 50, 'male')

print(siddiq.get_info())
print(wasinger.get_info())
print(sandra.get_info())
print(baum.get_info())
