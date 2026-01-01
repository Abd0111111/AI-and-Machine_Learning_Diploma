'''
session 7.1
'''
# الكلاس Product بيمثل منتج في المخزن،
# وبيحتوي على الاسم والسعر والكمية،
# ومعاه دوال لإعادة التخزين والبيع مع تحديث الكمية.

# What Python code manages a product with restock and sell operations

class Product:
    # creates a new product with name price quantity
    def __init__(self, name, price, quantity):
        self.name = name          # stores the product name
        self.price = price        # stores the product price
        self.quantity = quantity  # stores the product quantity

    # adds more units to the quantity
    def restock(self, amount):
        self.quantity += amount   # increases quantity by amount
        print(f"Restocked {self.name}. New quantity: {self.quantity}")  # shows the updated quantity

    # sells units from the product
    def sell(self, amount):
        if amount <= self.quantity:     # checks if enough stock exists
            self.quantity -= amount     # decreases quantity by amount
            print(f"Sold {amount} of {self.name}. Remaining quantity: {self.quantity}")  # shows remaining quantity
        else:
            print("Not enough stock to sell.")  # not enough stock message

# Example usage
product1 = Product("Laptop", 1200, 10)   # creates product with name price quantity
product1.restock(5)                      # restocks the product
product1.sell(3)                         # sells part of the quantity
product1.sell(20)                        # tries to sell more than available
