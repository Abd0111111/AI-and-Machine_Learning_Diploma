# Types of Errors in Python 🐞

---

## 1. Syntax Error

**Definition:** Wrong syntax. You do not follow the language rules.

**When it occurs:** Before the code runs (at compile / parse time).

**How to fix:** Read the error message carefully and correct the syntax.

### Common Types of Syntax Errors

### a) Missing Colon (:) ❌

```python
# ❌ WRONG: Missing colon after if statement
# if x > 5
#     print("Greater")
# SyntaxError: expected ':'

# ✅ CORRECT
x = 10
if x > 5:
    print("Greater")  # 👍 Proper syntax
```

---

### b) Indentation Error 📐

```python
# ❌ WRONG: Incorrect indentation
# def greet():
# print("Hello")
# IndentationError: expected an indented block

# ✅ CORRECT
def greet():
    print("Hello")  # 👍 Correct indentation

greet()
```

---

### c) Missing Brackets / Parentheses 🔒

```python
# ❌ WRONG: Missing closing parenthesis
# print("Hello"
# SyntaxError: '(' was never closed

# ✅ CORRECT
print("Hello")

# ❌ WRONG: Missing closing bracket
# my_list = [1, 2, 3
# SyntaxError: '[' was never closed

# ✅ CORRECT
my_list = [1, 2, 3]
```

---

### d) Invalid Variable Names 🚫

```python
# ❌ WRONG: Variable name starts with a number
# 1name = "Alice"
# SyntaxError: invalid decimal literal

# ✅ CORRECT
name1 = "Alice"

# ❌ WRONG: Using a reserved keyword
# class = "Math"
# SyntaxError: invalid syntax

# ✅ CORRECT
class_name = "Math"
```

---

## 2. Logical Error 🧠

**Definition:** Code runs without crashing but produces wrong or unexpected results.

**When it occurs:** During execution.

**How to fix:** Trace the logic and correct the algorithm.

```python
# ❌ WRONG LOGIC
def calculate_average(a, b):
    return a + b / 2  # ❌ Wrong order of operations

# ✅ CORRECT LOGIC
# def calculate_average(a, b):
#     return (a + b) / 2

result = calculate_average(10, 20)
print(f"Average: {result}")  # Outputs wrong result
```

📝 **Note:** Logical errors are the hardest to detect because Python does not raise an error.

---

## 3. Runtime Error ⚠️

**Definition:** Syntax is correct, but an error occurs while the program is running.

**When it occurs:** During execution.

**How to fix:** Fix the condition or use `try / except` blocks.

### a) ZeroDivisionError ➗

```python
# ❌ WRONG
# result = 10 / 0

# ✅ CORRECT
x = 10
y = 2
result = x / y
print(result)
```

---

### b) TypeError 🔄

```python
# ❌ WRONG
# result = "5" + 10

# ✅ CORRECT
result = "5" + str(10)
print(result)
```

---

### c) ValueError 🔢

```python
# ❌ WRONG
# number = int("abc")

# ✅ CORRECT
number = int("123")
print(number)
```

---

### d) IndexError 📋

```python
my_list = [1, 2, 3]

# ❌ WRONG
# item = my_list[5]

# ✅ CORRECT
item = my_list[2]
print(item)
```

---

### e) KeyError 🗝️

```python
person = {"name": "Alice", "age": 25}

# ❌ WRONG
# city = person["city"]

# ✅ CORRECT
city = person.get("city", "Unknown")
print(city)
```

---

### f) FileNotFoundError 📂

```python
import os

# ❌ WRONG
# file = open("nonexistent_file.txt", "r")

# ✅ CORRECT
if os.path.exists("myfile.txt"):
    file = open("myfile.txt", "r")
    print(file.read())
    file.close()
else:
    print("File not found!")
```

---

## Extra Notes 📝

* 🔴 **Syntax Errors** stop your program before it runs.
* 🟡 **Logical Errors** give wrong results but no crash.
* 🔵 **Runtime Errors** crash the program while running.

### Best Practices to Avoid Errors ✅

* Use meaningful variable names
* Test your code step by step
* Read error messages carefully
* Use `print()` for debugging
* Use `try / except` for runtime safety

---

🎯 **Summary**

| Error Type    | Happens When     | Example           |
| ------------- | ---------------- | ----------------- |
| Syntax Error  | Before execution | Missing colon     |
| Logical Error | During execution | Wrong calculation |
| Runtime Error | During execution | Division by zero  |

---

💡 Understanding errors is a key step to becoming a professional Python developer 🚀
