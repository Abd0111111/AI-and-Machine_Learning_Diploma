#Tasks for print(), comments, format, f-strings
# Task 1:
# Print your name and age using the print() function.
# Store the values in variables first.

name = "Omar"
age = 22
print(name)
print(age)
# Task 2:
# Print a sentence that includes your name and age using .format().

name = "Omar"
age = 22
print("My name is {}, and I am {} years old".format(name, age))
# Task 3:
# Print the same sentence using an f-string.

name = "Omar"
age = 22
print(f"My name is {name}, and I am {age} years old")

# ---------------------------------------------------------
#Tasks for type()

# Task 4:
# Create three variables with different data types
# and print the type of each one.

x = 10
y = 3.5
z = "Python"

print(type(x))
print(type(y))
print(type(z))

# ---------------------------------------------------------
#Tasks for len()

# Task 5:
# Create a list and a string
# then print the length of each one using len().

numbers = [1, 2, 3, 4, 5]
word = "Hello"

print(len(numbers))
print(len(word))

# ---------------------------------------------------------
#Tasks for input()

# Task 6:
# Ask the user for their name and age
# then print a greeting message.

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello {name}, you are {age} years old")

# ---------------------------------------------------------
#Tasks for int(), float(), str()

# Task 7:
# Convert a string number to an integer
# then add 10 to it and print the result.

number = "20"
number = int(number)
print(number + 10)

# Task 8:
# Convert an integer to a string
# and print it with some text.

age = 25
age_str = str(age)
print("My age is " + age_str)

# ---------------------------------------------------------
# Tasks for range()

# Task 9:
# Use range() to print numbers from 0 to 4.

for i in range(5):
    print(i)

# Task 10:
# Print even numbers from 0 to 10 using range().

for i in range(0, 11, 2):
    print(i)

# ---------------------------------------------------------
# Tasks for sum(), min(), max()

# Task 11:
# Create a list of numbers
# then print the sum, minimum, and maximum values.

numbers = [3, 7, 1, 9, 4]

print(sum(numbers))
print(min(numbers))
print(max(numbers))

# ---------------------------------------------------------
# Tasks for abs() and round()

# Task 12:
# Use abs() to get the absolute value of a negative number.

number = -15
print(abs(number))

# Task 13:
# Round a float number to 2 decimal places.

value = 3.14159
print(round(value, 2))


# ---------------------------------------------------------
# Tasks for sorted()
# Task 14:
# Sort a list of numbers in ascending and descending order.

numbers = [5, 2, 9, 1, 7]

print(sorted(numbers))
print(sorted(numbers, reverse=True))

# ---------------------------------------------------------
#Tasks for list(), tuple(), set(), dict()

# Task 15:
# Convert a range into a list and print it.

numbers = list(range(5))
print(numbers)

# Task 16:
# Create a set from a list with duplicate values.

values = [1, 2, 2, 3, 3, 4]
unique_values = set(values)
print(unique_values)

# ---------------------------------------------------------
#Tasks for enumerate()

# Task 17:
# Use enumerate() to print index and value of a list.

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# ---------------------------------------------------------
# Tasks for zip()

# Task 18:
# Use zip() to combine names and ages
# and print them in a sentence.

names = ["Ali", "Sara", "Omar"]
ages = [20, 25, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# ---------------------------------------------------------
# Tasks for map() and filter()

# Task 19:
# Use map() to square all numbers in a list.

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Task 20:
# Use filter() to keep only even numbers from a list.

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# ---------------------------------------------------------
#Tasks for all(), any(), isinstance()

# Task 21:
# Check if all values in a list are True.

values = [True, True, False]
print(all(values))

# Task 22:
# Check if a variable is of type int using isinstance().

value = 10
print(isinstance(value, int))

