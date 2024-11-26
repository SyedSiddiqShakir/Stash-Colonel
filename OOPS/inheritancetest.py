class Vehicle():
    def __init__(self, make, model, year: int):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"It is a {self.make} of {self.model} and made in year {self.year}"
    
class Car(Vehicle):
    def __init__(self, make, model, year: int, nod):
        super().__init__(make, model, year)
        self.nod = nod
        
    def get_info(self):
        return f"{super().get_info()} with {self.nod} doors"

access = Vehicle('bike', 'Access_125', 2018)
i10 = Car('hatchback', 'magna', 2012, 4)

print(access.get_info())
print(i10.get_info())