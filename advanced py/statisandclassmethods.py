class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    @classmethod
    def create_default_product(cls, name):
        return cls(name, 100)
    @staticmethod
    def is_valid_price(price):
        return price > 0

handy = Product.create_default_product('Mobile')
pen = Product.create_default_product('Montex')

print(f"Product: {handy.name}, Price: {handy.price}")
print(Product.is_valid_price(50))
print(Product.is_valid_price(-10))

cprod = Product("keyboard", 1000)
if Product.is_valid_price(cprod.price):
    print(f"Product: {cprod.name}, Price: {cprod.price}")
else:
    print("Negative proce, please enter a positive price")