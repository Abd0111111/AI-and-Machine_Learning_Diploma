
# Object-Oriented Programming (OOP) in Python 🧱🐍

---

## 1️⃣ Creating a Class (Class Definition)

### Definition
A **class** is a blueprint or template that defines the properties (attributes) and behaviors (methods) of an object.

📌 **In Arabic:**  
الكلاس هو قالب بنحدد فيه الخصائص والدوال اللي أي كائن (Object) هيستخدمها.

### Syntax
```python
class Person:
    def __init__(self, name, age):
        self.name = name      # 🧾 Attribute
        self.age = age        # 🧾 Attribute
```

📝 **Notes:**
- `__init__` is called a **constructor**
- `self` refers to the current object

---

## 2️⃣ Creating an Object (Object Instantiation)

### Definition
An **object** is a real instance created from a class.

📌 **In Arabic:**  
الكائن هو نسخة حقيقية من الكلاس وبنستخدمه فعليًا في البرنامج.

### Example
```python
p1 = Person("Ali", 25)
print(p1.name)   # Output: Ali
print(p1.age)    # Output: 25
```

🧠 Each object has its **own data**, even if created from the same class.

---

## 3️⃣ Methods (Functions Inside Class)

### Definition
Methods are functions defined inside a class and describe the behavior of the object.

📌 **In Arabic:**  
الميثودز هي دوال بتخلي الكائن يعمل أفعال معينة.

### Example
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name} 👋")
```

### Usage
```python
p = Person("Sara")
p.greet()  # Hello, my name is Sara 👋
```

---

## 4️⃣ Inheritance (Code Reusability)

### Definition
Inheritance allows a class to reuse attributes and methods from another class.

📌 **In Arabic:**  
التوريث بيسمح لكلاس جديد يستخدم كود كلاس قديم بدل ما نكتبه من جديد.

---

### 🔹 Single Inheritance

```python
class Animal:
    def speak(self):
        print("Animal sound 🐾")

class Dog(Animal):
    def speak(self):
        print("Bark 🐶")
```

---

### 🔹 Multiple Inheritance

```python
class Flyer:
    def fly(self):
        print("I can fly ✈️")

class Swimmer:
    def swim(self):
        print("I can swim 🏊")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()
```

⚠️ Python resolves conflicts using **MRO (Method Resolution Order)**.

---

### 🔹 Multilevel Inheritance

```python
class Vehicle:
    def move(self):
        print("Moving 🚗")

class Car(Vehicle):
    def wheels(self):
        print("4 wheels")

class ElectricCar(Car):
    def fuel(self):
        print("Electric power ⚡")
```

---

### 🔹 Hybrid Inheritance

📌 Combination of more than one inheritance type.

```python
class Engine:
    def start(self):
        print("Engine started")

class Electric:
    def charge(self):
        print("Charging battery")

class Tesla(Car, Electric):
    pass
```

---

## 5️⃣ Comprehensive Inheritance Example

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying 📚")

s = Student("Mohamed")
s.greet()
s.study()
```

---

## 🔍 Additional OOP Concepts (Bonus)

### ✔️ Encapsulation
Protecting data using private attributes.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private

    def get_balance(self):
        return self.__balance
```

---

### ✔️ Polymorphism
Same method name, different behavior.

```python
class Bird:
    def sound(self):
        print("Bird sound")

class Cat:
    def sound(self):
        print("Meow 🐱")

for animal in (Bird(), Cat()):
    animal.sound()
```

---

## ✅ Summary

- Class = Blueprint
- Object = Instance
- Method = Behavior
- Inheritance = Reusability
- OOP helps build clean, scalable, and organized code 🧠✨

---

📘 **This file is designed as a Doctor's Reference Model**
