# Python Control Flow & Loop Control 🧠🐍

---

## 1. If Statement

### 📝 Explanation (Arabic)
جملة **If** بتستخدم علشان تنفذ كود معين *فقط* لو الشرط اتحقق وطلع **True**.

### 💻 Code
```python
# If Statement Example ✅
age = 18

if age >= 18:
    print("You are an adult")  # 🧑‍🦱 الشخص بالغ
```

```python
# Check if Number is Positive ➕
number = 10

if number > 0:
    print("The number is positive")  # 🔢 رقم موجب
```

```python
# Check Password 🔐
password = "1234"

if password == "1234":
    print("Access granted")  # ✅ تم السماح بالدخول
```

---

## 2. If-Else Statement

### 📝 Explanation (Arabic)
هنا بنستخدم **if-else** علشان نختار بين مسارين:
- مسار لو الشرط True
- ومسار تاني لو False

### 💻 Code
```python
# Basic If-Else 🧩
age = 15

if age >= 18:
    print("You are an adult")  # 🧑‍🦱 بالغ
else:
    print("You are a minor")  # 👶 قاصر
```

```python
# Even or Odd Number 🔢
number = 7

if number % 2 == 0:
    print("Even number")  # ⚖️ زوجي
else:
    print("Odd number")   # 🔹 فردي
```

```python
# Pass or Fail 🎓
score = 45

if score >= 50:
    print("Pass")  # ✅ ناجح
else:
    print("Fail")  # ❌ راسب
```

---

## 3. If-Elif-Else Statement

### 📝 Explanation (Arabic)
الـ **elif** معناها *else if*  
بتستخدم لما يكون عندنا أكتر من شرط وعايزين نختبرهم بالترتيب.

### 💻 Code
```python
# Grading System 📊
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

```python
# Age Categories 👶🧑‍🦱👴
age = 35

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

```python
# Traffic Light 🚦
light = "yellow"

if light == "green":
    print("Go")
elif light == "yellow":
    print("Slow down")
elif light == "red":
    print("Stop")
else:
    print("Invalid light color")
```

---

## 4. Match Statement (Switch Case)

### 📝 Explanation (Arabic)
الـ **match-case** بديل أنضف لـ if-elif-else  
متاح من Python 3.10+ وبيستخدم لمطابقة القيم.

### 💻 Code
```python
# Match Day 🗓️
day = "Monday"

match day:
    case "Monday":
        print("Start of the work week")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Midweek day")
```

```python
# HTTP Status Codes 🌐
status_code = 404

match status_code:
    case 200:
        print("OK - Success")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case 403:
        print("Forbidden")
    case _:
        print("Unknown status code")
```

```python
# Menu Selection 📋
choice = 2

match choice:
    case 1:
        print("You selected: New File")
    case 2:
        print("You selected: Open File")
    case 3:
        print("You selected: Save File")
    case 4:
        print("You selected: Exit")
    case _:
        print("Invalid choice")
```

```python
# Grading System with Match 🎯
grade = "B"

match grade:
    case "A":
        print("Excellent! 90-100")
    case "B":
        print("Good! 80-89")
    case "C":
        print("Average! 70-79")
    case "D":
        print("Below Average! 60-69")
    case "F":
        print("Failed! Below 60")
    case _:
        print("Invalid grade")
```

```python
# Color Categories 🎨
color = "red"

match color:
    case "red" | "orange" | "yellow":
        print("Warm color")
    case "blue" | "green" | "purple":
        print("Cool color")
    case "black" | "white" | "gray":
        print("Neutral color")
    case _:
        print("Unknown color")
```

---

## 5. Break Statement

### 📝 Explanation (Arabic)
الـ **break** بتستخدم علشان توقف اللوب فورًا حتى لو الشرط لسه متحقق.

### 💻 Code
```python
# Break in For Loop ⛔
for i in range(1, 11):
    print(i)
    if i == 5:
        print("Found 5! Breaking the loop.")
        break
```

```python
# Break in While Loop 🔄
count = 0

while count < 10:
    count += 1
    print(f"Count: {count}")
    
    if count == 3:
        print("Breaking at 3")
        break
```

```python
# Search in a List 🔍
fruits = ["apple", "banana", "orange", "grape", "mango"]
search = "orange"

for fruit in fruits:
    print(f"Checking: {fruit}")
    if fruit == search:
        print(f"Found {search}!")
        break
```

```python
# Password Attempts 🔐
correct_password = "secret123"
attempts = ["wrong1", "wrong2", "secret123", "wrong3"]

for attempt in attempts:
    print(f"Trying password: {attempt}")
    
    if attempt == correct_password:
        print("Access granted!")
        break
    else:
        print("Wrong password")
```

---

## 📌 Summary
- **if**: تنفيذ كود بشرط
- **if-else**: اختيار بين مسارين
- **if-elif-else**: اختيار بين عدة حالات
- **match-case**: بديل switch (Python 3.10+)
- **break**: إيقاف اللوب فورًا
