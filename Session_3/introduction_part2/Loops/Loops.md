# Python Loops – For & While 🔁🐍

---

## 1. Basic For Loop 🔂
🔹 **شرح بالعربي:**  
حلقة `for` تُستخدم لتكرار تنفيذ كود عددًا محددًا من المرات، أو للتكرار على عناصر داخل تسلسل مثل list أو string.

Repeats code a specific number of times  
Iterates over a sequence (list, string, range, etc.)  

### Format
```python
for variable in sequence:
    # code block 🔁
```

### Simple For Loop with List
```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)  # 🍎 Printing each fruit
```

### Example: Print Each Character in a String
```python
word = "Python"

for letter in word:
    print(letter)  # 🔤 Printing each character
```

---

## 2. For Loop with Range 🔢
🔹 **شرح بالعربي:**  
الدالة `range()` تُنشئ تسلسل أرقام وتُستخدم كثيرًا مع حلقات `for`.

- `range(stop)` → من 0 إلى stop-1  
- `range(start, stop)` → من start إلى stop-1  
- `range(start, stop, step)` → بخطوة محددة  

### Range with One Argument
```python
# Print numbers 0 to 4
for i in range(5):
    print(i)  # 🔢
```

### Range with Start and Stop
```python
# Print numbers 1 to 5
for i in range(1, 6):
    print(i)
```

### Range with Step
```python
# Print even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)  # ⚖️ Even numbers
```

### Example: Countdown
```python
# Count down from 5 to 1
for i in range(5, 0, -1):
    print(i)
print("Blast off!")  # 🚀
```

---

## 3. For Loop with Lists 📋
🔹 **شرح بالعربي:**  
تُستخدم للتكرار على عناصر القوائم، ويمكن الحصول على العنصر ورقمه باستخدام `enumerate()`.

### Basic List Iteration
```python
colors = ["red", "green", "blue"]

for color in colors:
    print(f"I like {color}")  # 🎨
```

### Using Enumerate (Index + Value)
```python
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")  # 🔢 + 🍓
```

### Example: Calculate Total
```python
prices = [10, 25, 30, 15]
total = 0

for price in prices:
    total += price  # ➕ Adding prices

print(f"Total: ${total}")  # 💰
```

---

## 4. Nested For Loops 🔁🔁
🔹 **شرح بالعربي:**  
حلقة داخل حلقة، مفيدة للتعامل مع الجداول والبيانات الثنائية.

### Basic Nested Loop
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")  # 📊
```

### Example: Multiplication Table
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")  # ✖️
    print()  # ⬜ Line break
```

---

## 5. For-Else Statement 🧠
🔹 **شرح بالعربي:**  
الـ `else` تعمل فقط إذا انتهت الحلقة بدون استخدام `break`.

### Loop Completes (Else Runs)
```python
for i in range(1, 6):
    print(i)
else:
    print("Loop completed successfully!")  # ✅
```

### Loop Breaks (Else Does NOT Run)
```python
for i in range(1, 6):
    print(i)
    if i == 3:
        print("Breaking at 3")  # ⛔
        break
else:
    print("This will NOT print")
```

---

## 6. Break Statement in For Loop 🛑
🔹 **شرح بالعربي:**  
`break` تُستخدم لإيقاف الحلقة فورًا عند تحقق شرط معين.

```python
for i in range(1, 11):
    if i == 5:
        print("Found 5! Stopping the loop.")  # 🎯
        break
    print(i)
```

---

# While Loops 🔄

## 7. Basic While Loop
🔹 **شرح بالعربي:**  
حلقة `while` تستمر طالما الشرط صحيح.

```python
count = 1

while count <= 5:
    print(count)
    count += 1  # ➕ Increment
```

### Example: Countdown
```python
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Blast off!")  # 🚀
```

---

## 8. While True (Infinite Loop) ♾️
🔹 **شرح بالعربي:**  
تعمل بلا توقف حتى نستخدم `break`.

```python
count = 0

while True:
    count += 1
    print(count)
    
    if count >= 5:
        print("Reached 5, breaking loop")  # 🛑
        break
```

---

## 9. While-Else Statement 🧠
🔹 **شرح بالعربي:**  
الـ `else` تعمل فقط إذا لم يتم كسر الحلقة.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
else:
    print("Loop completed successfully!")  # ✅
```

---

## 10. While vs For Loop ⚖️
🔹 **شرح بالعربي:**  
- استخدم `for` عندما تعرف عدد التكرارات  
- استخدم `while` عندما يعتمد التكرار على شرط  

```python
print("For Loop:")
for i in range(1, 6):
    print(i)

print("\nWhile Loop:")
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

## ✅ Summary
- for loop: تكرار على تسلسل  
- while loop: تكرار بشرط  
- break: إيقاف الحلقة  
- else: يعمل فقط بدون break  

