class car():
    def __init__(self, company, model, year, color):                                                      #defines car
        self.company = company
        self.model = model
        self.year = year
        self.color = color
    
    def display_info(self):                                                                                #printing method
        print(f"It is a {self.company} {self.model} of {self.color} color made in {self.year}")
        
    def start_engine(self):                                                                                #waste method
        print("The car is now running")
    
    def change_color(self, new_color):                                                                #changes color
        self.color = new_color

mycar = car('toyota', 'civic', '2010', 'red')                                                              # createde mycar object 
mycar.display_info()                                                                                    # displays car info
mycar.start_engine()
mycar.change_color(input("Enter the new color of car:\n"))                                                                           # inputs a new car color
mycar.display_info()                                                                                    # display car infor with new color