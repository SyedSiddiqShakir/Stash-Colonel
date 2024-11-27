class Calculator:
    def __add__(self, a, b, c=0):
        if c != 0:
            return a+b+c 
        return a+b
calc = Calculator()    
print(calc.__add__(5, 2))