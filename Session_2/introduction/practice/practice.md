# Python Practice Tasks & Examples 🧪🐍

---

## 1. Output Prediction 🖨️

### 📝 Explanation (Arabic)
في الجزء ده بنشوف إيه اللي هيطلع في الـ output.
الكود اللي جوه الـ triple quotes (`'''`) متعتبر تعليق (multi-line comment) وبالتالي مش بيتنفذ.
علشان كده اللي هيظهر بس هو الأوامر اللي برا التعليق.

### 💻 Code
```python
'''
What Would the output be ? 

print("hello")
x = 5
print(x)
'''

print("world")
x = "Machine Leanring"
print("Testing", x)

# print(x)
```

### ✅ Output
```
world
Testing Machine Leanring
```

---

## 2. Create a Print Using Formatting 🎯

### 📝 Explanation (Arabic)
الجزء ده بيشرح طرق مختلفة لتنسيق النصوص باستخدام `.format()`  
تقدر تربط القيم بالمكان باستخدام:
- index
- الترتيب
- أسماء متغيرات

### 💻 Code
```python
print("my name is {0}, my age is {1}".format("omar", 22)) 
print("my name is {}, my age is {}".format("omar", 22)) 
print("my name is {x}, my age is {y}".format(x="omar", y=22)) 

name = "Oamr"
age = 22
uni = "GUC"

print("my name is {}, my age is {} and studying at the {}".format(name, age, uni))
```

---

## 3. Variables and Their Types 🧬

### 📝 Explanation (Arabic)
هنا بنعرّف متغيرات من أنواع مختلفة وبنستخدم `type()` علشان نعرف نوع كل متغير.

### 💻 Code
```python
x = 10          # int
y = 10.5        # float
z = "omar"      # string
w = [1,2,3,4]   # list
a = {1,2,3,4,5,6,6,7}  # set
b = ("omar",22,178)   # tuple
c = {1}         # set
d = True        # bool
person = {"name": "Omar", "age": 22, "city": "Cairo"}

print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(a))
print(type(b))
print(type(person))
```

---

## 4. String Manipulation ✂️🧵

### 📝 Explanation (Arabic)
الجزء ده بيشرح التعامل مع النصوص:
- slicing
- replace
- join
- split

### 💻 Code
```python
# Slicing
string = "Amit Learning Amit"
print(string[0:3:1])  

# Replace
string2 = string.replace("Amit", "Python")

print(string)
print(string2)

# join
words = ["Python", "is", "cool"]
print(" ".join(words))
print("-".join(words))

# split
print(string.split())
```

---

## 5. List Manipulation 📋

### 📝 Explanation (Arabic)
هنا بنشوف إزاي نشتغل على الـ lists:
- الوصول للعناصر
- التعديل
- الإضافة
- الحذف

### 💻 Code
```python
list_one = [1,2,3,4,"amit","learning",True,[1,2,3,"Ture",["m1","d1","ds"]]]

print(list_one)
print(type(list_one))
print(len(list_one))

print(list_one[7][1])  

list_one[7][1] = 4  

print(list_one[7][1])  

print(list("amit"))  

list_one.append("Machine Learning") 
print(list_one)

list_one.insert(1,"omar Gaber") 
print(list_one)

list_one.extend(["1.list_2","2. Testing"]) 
print(list_one)

list_one.remove("2. Testing") 
print(list_one)

x = list_one.pop() 

print(x) 
print(list_one)
```

---

## 6. Input Function + List Manipulation ⌨️🍎

### 📝 Explanation (Arabic)
المثال ده بيستخدم `input()` علشان ياخد قيمة من المستخدم
وبعدين يتحقق هل العنصر موجود في الـ list قبل ما يحذفه.

### 💻 Code
```python
fruits = ["apple","banana","cherry","kiwi"]

selected_fruit = input("Please Eneter Fruit you want to remove")

if fruits.count(selected_fruit):
    fruits.remove(selected_fruit)
else: 
    print("Not in our list")

print(fruits)
```

---

## 7. Tuple Manipulation 📦

### 📝 Explanation (Arabic)
الـ tuple مش قابلة للتعديل، علشان كده بنحوّلها لـ list الأول لو محتاجين نغيّر فيها.

### 💻 Code
```python
tuple_one = (1,2,3,4,"amit","learning",True,(1,2,3,"Ture",("m1","d1","ds")))

print(tuple_one)

list_two = list(tuple_one)

print(list_two)
```

---

## 8. Dictionary Manipulation 🗂️

### 📝 Explanation (Arabic)
هنا بنشرح التعامل مع الـ dictionaries:
- تعديل القيم
- إنشاء dict من list

### 💻 Code
```python
dict_one = {"key1": 12.5, "key2":"value2", "key3":"python", 4:[1,2,3,4]}
print(dict_one)

dict_one["key1"] = "Amit Learning"
print(dict_one)

key_value_list = [('a',1),('b',2)]
print(dict(key_value_list))
```
