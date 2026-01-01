# Python Data Types and Type Conversion 🔢

---

## 1. Integers (int)

Whole numbers without decimal points.

Can be positive, negative, or zero.

No size limit in Python.

Convert to int using `int()` – Converts strings, floats, booleans to integers.

```python
age = 25
temperature = -5
population = 1000000

print(age)
print(type(age))
print(temperature)
print(population)

print("\n" + "="*50 + "\n")

# Basic math
print(5 + 5)
print(10 - 2)
print(3 * 2)

print("\n" + "="*50 + "\n")

# Conversion to int
print(int("100"))      # From string
print(int(10.9))       # From float (truncates)
print(int(True))       # From boolean (True = 1)
print(int(False))      # From boolean (False = 0)
```

---

## 2. Floating Point Numbers (float)

Numbers with decimal points.

Convert to float using `float()`.

```python
price = 19.99
pi = 3.14159
g = 9.8

print(price)
print(type(price))

# Conversion to float
print(float("10.5"))   # From string
print(float(10))       # From int
```

---

## 3. Strings (str)

Text data enclosed in quotes (`" "` or `' '`).

Convert to string using `str()`.

```python
name = "Alice"
greeting = 'Hello, World!'
number_str = "123"

print(name)
print(type(name))

# String Concatenation
print("Hello " + name)

# Conversion to string
print(str(100))
print(type(str(100)))
```

---

## 4. Booleans (bool)

Represents `True` or `False`.

Result of comparisons.

```python
is_python_fun = True
is_raining = False

print(is_python_fun)
print(type(is_python_fun))

# Boolean expressions
print(10 > 5)   # True
print(10 < 5)   # False
```

---

## 5. Lists (list)

Ordered collection of items.

Mutable (can be changed).

Items can be of different types.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Hello", 3.14, True]

print(fruits)
print(type(fruits))
print(fruits[0])   # Access first item
```

---

## 6. Tuples (tuple)

Ordered collection of items.

Immutable (cannot be changed after creation).

```python
coordinates = (10, 20)
colors = ("red", "green", "blue")

print(coordinates)
print(type(coordinates))
print(coordinates[1])
```

---

## 7. Sets (set)

Unordered collection of unique items.

Does not allow duplicates.

```python
unique_numbers = {1, 2, 3, 3, 3, 4}
print(unique_numbers)   # Result: {1, 2, 3, 4}
print(type(unique_numbers))
```

---

## 8. Dictionaries (dict)

Collection of key-value pairs.

Keys must be unique.

```python
user = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(user)
print(type(user))
print(user["name"])   # Access value by key
```

---

## 9. NoneType (None)

Represents the absence of a value or a null value.

```python
result = None
print(result)
print(type(result))
```

---

## 10. Type Conversion

Convert between different data types.

Use `int()`, `float()`, `str()`, `list()`, etc.

Important for data manipulation.

```python
# String to int
age_str = "25"
age_int = int(age_str)
print(age_int, type(age_int))

# Int to string
num = 100
num_str = str(num)
print(num_str, type(num_str))

# List to set (removes duplicates)
numbers_list = [1, 2, 2, 3, 3, 3]
numbers_set = set(numbers_list)
print(numbers_set)

# List to tuple
numbers_tuple = tuple(numbers_list)
print(numbers_tuple)
```
