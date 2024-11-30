li = [1, 2, 3, 4, 6, 2, 4, 3]

def func(x):
    return x+2
d = list(map(func, li))
print(d)

#new program

even_numbers= [2, 4, 6, 8, 10]
def sqrt(x):
    return x**x
result = list(map(sqrt, even_numbers))
print(result)