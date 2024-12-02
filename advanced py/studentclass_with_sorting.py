class Student():
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"{self.name} of {self.age} age has {self.grade} % of Marks"

allstudents = [Student('siddiq', 25, 85), Student('hadi', 23, 91), Student('jack', 24, 84), Student('shourya', 23, 78), Student('abdul', 24, 77)
, Student('Zhao', 26, 99), Student('peter', 21, 61), Student('pablo', 44, 87)]

newList = sorted(allstudents, key=lambda s: s.age)
print(newList)
