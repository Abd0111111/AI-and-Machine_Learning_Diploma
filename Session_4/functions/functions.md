# Python Function Arguments 🎯🐍

---

## 1. Positional Argument Function 📌
🔹 **شرح بالعربي:**  
الـ Positional Arguments معناها إن ترتيب القيم اللي بنبعتها للفنكشن لازم يكون **نفس ترتيب الباراميترز** اللي متعرفة في الفنكشن، وأي تغيير في الترتيب ممكن يسبب نتايج غلط.

During a function call, values passed through arguments should be in the same order as the defined function parameters.

```python
def introduce(name, age, city):
    print(f"Hi, I'm {name}, {age} years old, from {city}")  # 👋

# CORRECT ORDER ✅
introduce("Alice", 25, "New York")
introduce("Bob", 30, "London")

# WRONG ORDER ❌
introduce(25, "Alice", "New York")  # 😕
```

---

## 2. Keyword Argument Function 🏷️
🔹 **شرح بالعربي:**  
في الـ Keyword Arguments بنحدد اسم الباراميتر مع القيمة، وبالتالي الترتيب مش مهم خالص.

```python
def introduce(name, age, city):
    print(f"Hi, I'm {name}, {age} years old, from {city}")  # 🧍‍♂️

introduce(name="Alice", age=25, city="New York")
introduce(age=25, city="New York", name="Alice")
```

---

## 3. Default Argument Function ⚙️
🔹 **شرح بالعربي:**  
الـ Default Arguments بتدي قيمة افتراضية للباراميتر.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")  # 👋

greet("Alice")
greet("Bob", "Hi")
greet("Charlie", greeting="Hey")
```

---

## 4. *args 📦

🔹 **شرح بالعربي:**   
*args في بايثون بتستخدم لما تحب تبعت للدالة عدد متغير من القيم كوسائط.

*args بتجمع كل القيم اللي بتتبعت للدالة في شكل tuple

تقدر تستخدمهم جوه الدالة زي أي قائمة أو مجموعة بيانات

بتخليك تكتب دوال مرنة مش محتاجة تحدد عدد الوسائط مسبقاً
```python
def add_numbers(*args):
    print(sum(args))

add_numbers(1, 2, 3)
```

---

## 5. **kwargs 🧾
🔹 **شرح بالعربي:** 
**kwargs في بايثون بتستخدم لما تحب تبعت للدالة عدد متغير من الوسائط المسماة (key-value pairs).

**kwargs بتجمع كل الوسائط المسماة في شكل dictionary

تقدر تستخدمهم داخل الدالة عشان تتعامل مع كل مفتاح وقيمة على حدة

بتخليك تكتب دوال مرنة تستقبل أي عدد من الوسائط المسماة بدون تحديد مسبق
```python
def print_info(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

print_info(name="Alice", age=25)
```

---

## 6. Combined Arguments 🔀
🔹 **شرح بالعربي:** 
الكود ده بيستخدم 3 أنواع من الوسائط في دالة واحدة:

name: وسيط عادي مطلوب

*hobbies: بيجمع أي عدد من الوسائط غير المسماة الإضافية في tuple

age=18: وسيط مسمى له قيمة افتراضية (لو ما اتكتبش، بياخد 18)

**details: بيجمع أي عدد من الوسائط المسماة الإضافية في dictionary
```python
def make_profile(name, *hobbies, age=18, **details):
    print(name, hobbies, age, details)

make_profile("Alice", "Reading", age=25, city="NYC")
```

---

## Summary ✅
All function argument types explained.
