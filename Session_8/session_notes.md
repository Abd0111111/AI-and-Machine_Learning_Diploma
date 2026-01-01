# 🧬 Inheritance في بايثون

الوراثة مفهوم أساسي في البرمجة الشيئية OOP.  
بتسمح لك تعمل Class جديدة مبنية على Class موجودة قبل كده.  

👨‍👦 الفئة الأصلية  
Parent Class أو Base Class  

👶 الفئة التي ترث  
Child Class أو Derived Class  

🎯 الهدف من الوراثة  
♻️ إعادة استخدام الكود  
✂️ تقليل التكرار  
🧩 تسهيل التوسعة والتعديل  

---

## Single Inheritance  
الوراثة المفردة  

📌 فئة ابن واحدة بترث من فئة أب واحدة فقط.  
📌 أبسط وأكتر نوع استخدامًا.  

🧠 الفكرة  
Dog تعتبر نوع من Animal  
يعني تقدر تستخدم كل اللي في Animal  

```python
class Animal:
    def eat(self):
        print("The animal is eating.")

class Dog(Animal):
    def bark(self):
        print("The dog is barking.")

my_dog = Dog()
my_dog.eat()
my_dog.bark()
```

---
## Multilevel Inheritance
# الوراثة متعددة المستويات 

📌 الوراثة بتمشي على أكتر من مستوى.

📌 كل Class بيبني على اللي قبله.
# 🧠 الفكرة
SportsCar نوع من Car

و Car نوع من Vehicle

```python
class Vehicle:
    def drive(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def fill_fuel(self):
        print("Car is being fueled.")

class SportsCar(Car):
    def turbo(self):
        print("Turbo engaged.")

my_car = SportsCar()
my_car.drive()
my_car.fill_fuel()
my_car.turbo()

```
---


## Hierarchical Inheritance
# الوراثة الهرمية 
📌 أكتر من Class ابن

📌 كلهم بيشتركوا في نفس Class أب

# 🧠 الفكرة
Child1 و Child2

الاتنين أبناء Parent

```python
class Parent:
    def greet(self):
        print("Hello from the Parent.")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()
obj1.greet()
obj2.greet()

```
---
## Multiple Inheritance
# الوراثة المتعددة
📌 Class واحدة بترث من أكتر من Class أب.

📌 بتجمع سلوكيات مختلفة في كيان واحد.

## 🧠 الفكرة

# SmartDevice
موبايل 📞
وكاميرا 📷 في نفس الوقت

```python
class Phone:
    def make_call(self):
        print("Calling...")

class Camera:
    def take_photo(self):
        print("Photo taken.")

class SmartDevice(Phone, Camera):
    def operate(self):
        print("Device is operating.")

my_device = SmartDevice()
my_device.make_call()
my_device.take_photo()
my_device.operate()

```
---
## Hybrid Inheritance
# الوراثة المختلطة 

📌 مزيج من أكتر من نوع وراثة.

📌 مستخدمة في الأنظمة الكبيرة.

# 🧠 الفكرة
وراثة متعددة

مع وراثة متعددة المستويات

```python
class A:
    def a(self):
        print("A")

class B(A):
    def b(self):
        print("B")

class C:
    def c(self):
        print("C")

class D(B, C):
    def d(self):
        print("D")

obj = D()
obj.a()
obj.b()
obj.c()
obj.d()
```

---
ندخل بقي علي جزء تاني 
---
# 🔒 Encapsulation في بايثون

Encapsulation واحد من أهم أعمدة OOP.  
فكرته الأساسية حماية البيانات والتحكم في الوصول ليها.  

Encapsulation =  
جمع البيانات  
والدوال اللي بتتعامل معاها  
داخل Class واحد  
مع منع التعديل المباشر على البيانات الحساسة  

---

## 💡 ليه Encapsulation مهم؟

🛡️ حماية الداتا من التعديل الغلط  
🧠 فرض منطق معين للتعامل مع القيم  
🧩 كود أنضف وأسهل في الصيانة  
🔁 تقليل الأخطاء في المشاريع الكبيرة  

---

## 🟢 Public Members

أي متغير أو Method من غير underscore.  
متاح من أي مكان في البرنامج.  

📌 الاستخدام  
للحاجات اللي مفيش مشكلة تتشاف أو تتغير مباشرة.  

### مثال

```python
class User:
    def __init__(self, name):
        self.name = name

u = User("Ahmed")
print(u.name)
u.name = "Ali"
print(u.name)
```
هنا مفيش أي حماية.

التعديل مباشر.
 ___
## 🟡 Protected Members
### underscore واحدة قبل الاسم.
معناها
يفضل استخدامها داخل Class
أو Classes الأبناء.

### مثال 
```python
class Employee:
    def __init__(self, salary):
        self._salary = salary

```
```python
class Manager(Employee):
    def show_salary(self):
        print(self._salary)

```
### Protected ينفع مع الوراثة.

---

## 🔴 Private Members

### underscore مرتين قبل الاسم.
بايثون بتمنع الوصول المباشر ليها.

### 📌 تستخدم لحماية البيانات الحساسة. 

```python
class User:
    def __init__(self, password):
        self.__password = password

```
```python
u = User("1234")
# print(u.__password) ❌

```
### مينفعش توصل لها مباشرة. 

---

## 📥 Getter Methods
### دوال لقراءة المتغيرات الخاصة.
من غير ما تكشفها مباشرة.

### مثال

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

```

```python
acc = BankAccount(1000)
print(acc.get_balance())

```

## 📤 Setter Methods
### دوال لتعديل القيم.
### مع شروط ومنطق.

📌 أهم جزء في Encapsulation.

### مثال 

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount


```

```python
acc = BankAccount(1000)
acc.set_balance(500)

```
### كده منعت القيم الغلط.

--- 

## 🏦 مثال شامل
### Encapsulation في سيناريو حقيقي

سيناريو
حساب بنكي.

المطلوب

منع السحب الزيادة

منع الرصيد السالب

عدم التعديل المباشر

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

```

```python
acc = BankAccount("Ali", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())


```
### ده Encapsulation صح.

---

## ✨ Property Decorator
### طريقة أحدث وأنضف من getter و setter.
تخليك تتعامل مع المتغير كأنه عادي.
## مثال

```python
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value


```
```python
p = Product(100)
p.price = 200
print(p.price)


```
## 🧬 Encapsulation مع Inheritance
### Private
لا يورث مباشرة.
### Protected
يورث عادي.
## مثال
```python
class Parent:
    def __init__(self):
        self._x = 10
        self.__y = 20

class Child(Parent):
    def show(self):
        print(self._x)
        # print(self.__y) ❌


```
---
## ✅ الخلاصة
### Encapsulation بيعلمك
تحمي الداتا

تتحكم في التعديل

تفرض منطق

وتكتب كود احترافي

---

## 🔥 مثال شامل  
Encapsulation + Inheritance مع بعض

### 🎯 فكرة المثال

عاوزين نعمل **نظام حسابات بنكية** فيه الآتي:

- كل حساب له  
  اسم صاحب الحساب  
  رقم حساب  
  رصيد

- الرصيد  
  ❌ ممنوع يتعدل مباشرة  
  ✅ يتعدل بس عن طريق دوال  

- عندنا نوعين حسابات  
  حساب عادي  
  حساب توفير  

- حساب التوفير  
  بيرث من الحساب العادي  
  ويضيف فائدة على الرصيد  

يعني هنطبق:

🔒 Encapsulation  
- Private variables  
- Getter  
- Setter  
- منطق تحكم  

🧬 Inheritance  
- Class أب  
- Class ابن  
- إعادة استخدام الكود  

---

## 🧠 تصميم الكلاسات

- BankAccount  
  الكلاس الأب  
  فيه البيانات الأساسية  
  ويتحكم في الرصيد  

- SavingsAccount  
  كلاس ابن  
  بيستخدم كل اللي في الأب  
  ويضيف behavior جديد  

---

## 💻 الكود الكامل مع الشرح

```python
class BankAccount:
    def __init__(self, owner, account_number, balance):
        # بيانات عامة عادي نستخدمها
        self.owner = owner
        self.account_number = account_number
        
        # رصيد خاص ❌ ممنوع التعديل المباشر
        self.__balance = balance

    def deposit(self, amount):
        # إضافة فلوس بشرط تكون قيمة صحيحة
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        # سحب فلوس بشرط
        # 1. المبلغ أكبر من صفر
        # 2. المبلغ أقل من أو يساوي الرصيد
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        # Getter
        # قراءة الرصيد بدون كشفه
        return self.__balance
```
### 🔒 هنا Encapsulation واضح
### __balance خاص
### مفيش وصول مباشر
### كل تعديل بيعدي على منطق
```python
class SavingsAccount(BankAccount):
    def __init__(self, owner, account_number, balance, interest_rate):
        # استدعاء constructor بتاع الكلاس الأب
        super().__init__(owner, account_number, balance)
        
        # خاصية جديدة لحساب التوفير
        self.interest_rate = interest_rate

    def add_interest(self):
        # حساب الفائدة بناءً على الرصيد الحالي
        interest = self.get_balance() * self.interest_rate
        
        # استخدام دالة من الكلاس الأب
        self.deposit(interest)

```
## 🧬 هنا Inheritance
### SavingsAccount ورثت من BankAccount
### استخدمت
### get_balance
### deposit
### وأضافت behavior جديد

---
## ▶️ تجربة النظام
```python
# إنشاء حساب توفير
account = SavingsAccount(
    owner="Ali",
    account_number="12345",
    balance=1000,
    interest_rate=0.05
)

# إيداع فلوس
account.deposit(500)

# سحب فلوس
account.withdraw(300)

# إضافة فائدة
account.add_interest()

# عرض الرصيد النهائي
print(account.get_balance())

```









