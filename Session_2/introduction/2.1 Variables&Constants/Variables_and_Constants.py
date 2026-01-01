# ---------------------------------------------------------
# Python Variables and Constants Tasks
# ---------------------------------------------------------

### TASK 1: Variable Declaration
# Create three variables:
# 1. A variable named 'name' with the value "Alice"
# 2. A variable named 'age' with the value 25
# 3. A variable named 'price' with the value 19.99

name = "Alice"
age = 25
price = 19.99


### TASK 2: Using and Printing Variables
# Create a variable named 'name' with the value "Bob"
# Then, use the print() function to display its value

name = "Bob"
print(name)


### TASK 3: Assigning New Values
# 1. Create a variable named 'score' and set it to 10
# 2. Update the 'score' variable to 20
# 3. Add 5 to the current value of 'score'
# 4. Print the final score

score = 10
score = 20
score = score + 5
print(score)


### TASK 4: Constant Declaration
# Create three constants using the standard naming convention (ALL CAPS):
# 1. PI with the value 3.14159
# 2. MAX_SPEED with the value 120
# 3. TAX_RATE with the value 0.15

PI = 3.14159
MAX_SPEED = 120
TAX_RATE = 0.15


### TASK 5: Calculations using Constants
# 1. Define a constant PI = 3.14159
# 2. Define a variable radius = 5
# 3. Calculate the area using the formula: PI * radius squared
# 4. Print the result with the label "Area:"

PI = 3.14159
radius = 5
area = PI * radius ** 2
print("Area:", area)

# ---------------------------------------------------------
# Additional Tasks: Exploring Data Types and Variables
# ---------------------------------------------------------

### TASK 6: String Variables (Text)
# Create a variable to store a sentence and another for a single character.
# 1. Create a variable 'message' with the value "Hello Python World"
# 2. Create a variable 'grade' with the value "A"
# 3. Print both variables.

message = "Hello Python World"
grade = "A"
print(message)
print(grade)


### TASK 7: Integer and Float Variables (Numbers)
# Practice with whole numbers and decimals.
# 1. Create an integer 'items_count' with the value 50
# 2. Create a float 'temperature' with the value 36.5
# 3. Print the sum of items_count + 10

items_count = 50
temperature = 36.5
print(items_count + 10)


### TASK 8: Boolean Variables (True/False)
# Booleans represent logical values: True or False.
# 1. Create a variable 'is_logged_in' and set it to True
# 2. Create a variable 'has_permission' and set it to False
# 3. Print the status of 'is_logged_in'

is_logged_in = True
has_permission = False
print(is_logged_in)


### TASK 9: Constant for System Limits
# Use constants for values that define system boundaries.
# 1. Define a constant 'MIN_AGE' and set it to 18
# 2. Define a constant 'DATABASE_NAME' and set it to "users_db"
# 3. Print the DATABASE_NAME

MIN_AGE = 18
DATABASE_NAME = "users_db"
print(DATABASE_NAME)


### TASK 10: Dynamic String Formatting
# Combining variables inside a print statement.
# 1. Use the 'name' variable (from Task 1) and 'age' variable.
# 2. Print a sentence like: "User Alice is 25 years old."

name = "Alice"
age = 25
print(f"User {name} is {age} years old.")

#Strings (النصوص): كما في name = "Alice"، تُحاط دائماً بعلامات تنصيص.

#Integers (الأرقام الصحيحة): مثل age = 25.

#Floats (الأرقام العشرية): مثل price = 19.99 أو PI = 3.14159.

#Naming Convention (اتفاقية التسمية): تذكر دائماً أن المتغيرات تُكتب بأحرف صغيرة والثوابت بأحرف كبيرة لتمييزها في الكود.