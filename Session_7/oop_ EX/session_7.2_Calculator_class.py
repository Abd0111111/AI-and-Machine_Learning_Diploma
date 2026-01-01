# The code below shows a simple structure for a calculator you can reuse in any program
# It explains how each operation works directly on two numbers
# It shows how to prevent division when the second number is zero
# This structure helps you practice creating methods and handling simple errors
# You can apply the same idea when building larger math tools

class Calculator:
    def add(self, a, b):     # returns sum of a and b
        return a + b

    def subtract(self, a, b):  # returns difference between a and b
        return a - b

    def multiply(self, a, b):  # returns product of a and b
        return a * b

    def divide(self, a, b):     # handles division with error control
        try:
            return a / b        # tries to divide
        except ZeroDivisionError:
            return "Error: Division by zero"  # handles zero division

# Example usage
calc = Calculator()              # creates calculator object
print(calc.add(10, 5))           # prints sum
print(calc.subtract(10, 5))      # prints difference
print(calc.multiply(10, 5))      # prints product
print(calc.divide(10, 2))        # prints division result
print(calc.divide(10, 0))        # prints error message