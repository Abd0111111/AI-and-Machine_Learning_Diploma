# Arithmetic Operators in Python ➕

---

## 1. Addition (+) ➕

Adds two numbers together.

Can also concatenate strings.

Can concatenate lists.

```python
# Adding numbers
print(10 + 5)      # 15
print(3.5 + 2.5)   # 6.0
print(-10 + 5)     # -5

# String concatenation
print("Hello" + " " + "World")  # Hello World

# List concatenation
print([1, 2] + [3, 4])  # [1, 2, 3, 4]
```

---

## 2. Subtraction (-) ➖

Subtracts one number from another.

Returns the difference between two numbers.

```python
# Subtracting numbers
print(10 - 5)        # 5
print(3.5 - 1.5)     # 2.0
print(-10 - 5)       # -15
```

---

## 3. Multiplication (*) ✖️

Multiplies two numbers.

Can repeat strings.

Can repeat lists.

```python
# Multiplying numbers
print(10 * 5)     # 50
print(3.5 * 2)    # 7.0

# String repetition
print("Hello" * 3)   # HelloHelloHello

# List repetition
print([1, 2] * 3)    # [1, 2, 1, 2, 1, 2]
```

---

## 4. Division (/) ➗

Divides one number by another.

Always returns a float, even if the result is a whole number.

```python
print(10 / 2)   # 5.0
print(10 / 3)   # 3.3333333333333335
print(7 / 2)    # 3.5
```

---

## 5. Floor Division (//) 🔢

Divides and rounds down to the nearest whole number.

Returns an integer if both operands are integers.

```python
print(10 // 3)   # 3
print(7 // 2)    # 3
print(-7 // 2)   # -4
```

---

## 6. Modulo (%) 🔄

Returns the remainder of division.

Useful to check even or odd numbers.

```python
print(10 % 3)   # 1
print(10 % 2)   # 0
print(7 % 2)    # 1
```

---

## 7. Exponentiation (**) 🧮

Raises a number to the power of another number.

Can be used to calculate square roots (power of 0.5).

```python
print(2 ** 3)    # 8
print(5 ** 2)    # 25
print(9 ** 0.5)  # 3.0
```

---

## 8. Order of Operations (PEMDAS) 📐

Python follows the standard order of operations:

1. Parentheses ()
2. Exponents **
3. Multiplication *, Division /, //, % (left to right)
4. Addition + and Subtraction - (left to right)

```python
print(10 + 2 * 5)      # 20
print((10 + 2) * 5)    # 60
print(10 / 2 ** 2)     # 2.5
```

---

## 9. Practical Examples 💡

Common real-world calculations using arithmetic operators.

```python
# Rectangle area
length = 10
width = 5
area = length * width
print("Area:", area)  # 50

# Average calculation
num1, num2, num3 = 80, 90, 85
average = (num1 + num2 + num3) / 3
print("Average:", average)  # 85.0

# Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print("Temperature:", fahrenheit, "°F")  # 77.0 °F

# Total price with tax
price = 100
tax_rate = 0.15
total = price + (price * tax_rate)
print("Total with tax:", total)  # 115.0

# Discount calculation
original_price = 200
discount_percent = 20
discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount
print("Final Price:", final_price)  # 160.0

# Splitting a bill
total_bill = 150
num_people = 4
per_person = total_bill / num_people
print("Each person pays:", per_person)  # 37.5
```
