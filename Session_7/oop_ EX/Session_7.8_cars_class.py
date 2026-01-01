# The code below shows how to store make model year and if the car is rented or not
# It explains how to rent the car only if available
# It explains how to return the car only if it was rented
# This helps manage car availability in a simple rental system
'''
الكلاس ده بيمثل سيارة في نظام تأجير.

بيخزن معلومات عن السيارة: الماركة، الموديل، والسنة.

بيتابع إذا كانت السيارة مؤجرة أو لا.

بيسمح لك تأجر السيارة فقط لو مش مؤجرة.

بيسمح لك ترجع السيارة لو كانت مؤجرة.

بيطبع رسالة توضح حالة التأجير أو الإرجاع في كل مرة.
'''

class Car:
    def __init__(self, make, model, year):   # creates a car with details
        self.make = make                     # stores manufacturer
        self.model = model                   # stores model name
        self.year = year                     # stores production year
        self.is_rented = False               # tracks if rented

    def rent(self):                         # rents the car if available
        if not self.is_rented:              # checks if not rented
            self.is_rented = True           # marks rented
            print(f"{self.make} {self.model} rented.")  # confirms rental
        else:
            print(f"{self.make} {self.model} is already rented.")  # says already rented

    def return_car(self):                   # returns the car if rented
        if self.is_rented:                  # checks if rented
            self.is_rented = False          # marks available
            print(f"{self.make} {self.model} returned.")  # confirms return
        else:
            print(f"{self.make} {self.model} was not rented.")  # says not rented before

# Example usage
car1 = Car("Toyota", "Corolla", 2020)   # creates a car object
car1.rent()                             # rents the car
car1.rent()                             # tries to rent again
car1.return_car()                       # returns the car
car1.return_car()                       # tries to return again