# Essential Python Built-in Functions and Concepts 🐍

---

## 1. print() & Comments 🖨️💬

`print()` يعرض النتائج في الكونسول.

تقدر تطبع متغيرات، نصوص، أرقام، أو أكثر من عنصر بنفس الوقت.

**التعليقات (Comments)** هي نصوص داخل الكود لا تُنفذ، تُستخدم لشرح أو توضيح.

```python
age = 25
name = "Alice"

print(age)
print(name)
print("My name is", name, "and I am", age, "years old")

''' 
This is a multi-line comment.
You can write multiple lines here.
'''

# This is a single-line comment using hash (#)
```

---

## 1.2 Print using .format() and Placeholders 🧩

تستخدم `{}` كأماكن لوضع القيم في النص.

يمكن تعيين القيم حسب الفهرس، الترتيب، أو أسماء المتغيرات.

```python
# Index-based assignment
print("My name is {0}, my age is {1}".format("Omar", 22))
print("I have {0} cats and {1} dogs. {0} is more than {1}".format(3, 2))

# Order-based assignment (automatic)
print("My name is {}, my age is {}".format("Omar", 22))

# Named assignment
print("My name is {x}, my age is {y}".format(x="Omar", y=22))
print("Product: {item}, Price: ${price}".format(item="Laptop", price=999))

# Using variables
name = "Sarah"
age = 28
city = "Cairo"
print("My name is {}, I am {} years old, I live in {}".format(name, age, city))
print("Name: {0}, City: {2}, Age: {1}".format(name, age, city))
```

---

## 1.3 F-Strings (Shortcut to .format()) ⚡

أسهل طريقة لإدخال متغيرات داخل النص.

ضع `f` قبل علامات التنصيص واستخدم `{}` مباشرة.

متاح من Python 3.6+

```python
name = "Omar"
age = 22

# باستخدام f-string
print(f"My name is {name}, my age is {age}")

# أمثلة أخرى
name = "Sarah"
age = 28
city = "Cairo"
print(f"My name is {name}, I am {age} years old, I live in {city}")
print(f"Price: ${100 * 5}")
print(f"With 10% tax: ${100 * 5 * 1.1:.2f}")  # يعرض رقمين عشريين فقط
```

### Comparison: .format() vs F-Strings ⚔️

```python
item = "Laptop"
price = 999

print("Product: {}, Price: ${}".format(item, price))
print(f"Product: {item}, Price: ${price}")
```

---

## 2. type() 🧬

تعرف نوع البيانات لأي قيمة أو متغير.

```python
print(type(10))
print(type(10.5))
print(type("Hello"))
print(type([1, 2, 3]))
```

---

## 3. len() 📏

ترجع عدد العناصر داخل كائن مثل قائمة أو نص.

```python
my_list = [1, 2, 3, 4, 5]
my_string = "Hello World"

print(len(my_list))
print(len(my_string))
```

---

## 4. input() ⌨️

تأخذ إدخال من المستخدم دائمًا كنص.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

---

## 5. int(), float(), str() 🔄

تحويل بين أنواع البيانات.

```python
print(int("10"))
print(int(10.9))

print(float("10.5"))
print(float(10))

print(str(10))
print(str(10.5))
```

---

## 6. range() 🔢

ينشئ سلسلة أرقام، يُستخدم كثيرًا في الحلقات.

```python
print(list(range(5)))
print(list(range(2, 7)))
print(list(range(0, 10, 2)))
```

---

## 7. sum() ➕

يجمع كل العناصر داخل iterable.

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
```

---

## 8. min() and max() 🔽🔼

```python
numbers = [10, 5, 20, 15, 3]

print(min(numbers))
print(max(numbers))
```

---

## 9. abs() ➖➕

```python
print(abs(-10))
print(abs(10))
print(abs(-3.5))
```

---

## 10. round() 🔄

```python
print(round(3.7))
print(round(3.14159, 2))
print(round(3.14159, 3))
```

---

## 11. sorted() 🔃

```python
numbers = [5, 2, 8, 1, 9]
names = ["Charlie", "Alice", "Bob"]

print(sorted(numbers))
print(sorted(names))
print(sorted(numbers, reverse=True))
```

---

## 12. list(), tuple(), set(), dict() 🗂️

```python
my_list = list(range(5))
print(my_list)

my_tuple = tuple([1, 2, 3])
print(my_tuple)

my_set = set([1, 2, 2, 3, 3, 3])
print(my_set)

my_dict = dict(name="Alice", age=25)
print(my_dict)
```

---

## 13. enumerate() 🔢

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

## 14. zip() 🔗

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

---

## 15. map() 🗺️

```python
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))
print(squared)

str_numbers = ["1", "2", "3"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)
```

---

## 16. filter() 🚦

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
```

---

## 17. all() and any() ✅❎

```python
values1 = [True, True, True]
values2 = [True, False, True]
values3 = [False, False, False]

print(all(values1))
print(all(values2))

print(any(values2))
print(any(values3))
```

---

## 18. reversed() 🔄

```python
numbers = [1, 2, 3, 4, 5]
print(list(reversed(numbers)))

word = "hello"
print(list(reversed(word)))
```

---

## 19. isinstance() 🧐

```python
age = 25
name = "Alice"

print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(age, str))
```
