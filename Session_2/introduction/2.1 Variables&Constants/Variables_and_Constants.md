
# Variables and Constants in Python 📌

---

## Variables

متغير (Variable) هو مكان في الذاكرة يخزن بيانات يمكن تغييرها أثناء تنفيذ البرنامج.

### Declaration (Creating a Variable)

صيغة إنشاء المتغير:

```python
variable_name = value
```

أمثلة:

```python
name = "Alice"
age = 25
price = 19.99
```

### Using (Calling) a Variable

تستخدم `print()` لعرض قيمة المتغير.

يمكنك أيضاً كتابة اسم المتغير مباشرة في بيئة Jupyter ليعرض قيمته.

```python
name = "Bob"

print(name)    # Using print()
name           # Just the variable name
```

### Assigning New Values

يمكنك تغيير قيمة المتغير في أي وقت.

```python
score = 10
print(score)

score = 20      # Assign new value
print(score)

score = score + 5
print(score)
```

---

## Constants 🔒

الثابت (Constant) هو قيمة لا يجب أن تتغير بعد تعريفها.

### Declaration (Creating a Constant)

الثوابت تُكتب عادة بأحرف كبيرة كلها.

صيغة التعريف:

```python
CONSTANT_NAME = value
```

أمثلة:

```python
PI = 3.14159
MAX_SPEED = 120
TAX_RATE = 0.15
```

### Using (Calling) a Constant

تشبه طريقة استخدام المتغيرات، يمكنك طباعتها بنفس الطريقة.

```python
PI = 3.14159

print(PI)      # Using print()
PI             # Just the constant name
```

### Using Constants in Calculations

يمكن استخدام الثوابت في العمليات الحسابية بسهولة.

```python
PI = 3.14159
radius = 5

area = PI * radius ** 2
print("Area:", area)
```

---

## Comparison ⚖️

- **Variables**:  
  - أسماء بأحرف صغيرة أو مختلطة (lowercase names)  
  - قيمها قابلة للتغيير  
  - مثال: `age = 25`

- **Constants**:  
  - أسماء بأحرف كبيرة كلها (ALL_CAPS)  
  - يجب ألا تتغير بعد تعريفها  
  - مثال: `PI = 3.14`

- **Calling**:  
  - استخدم `print()` أو اكتب الاسم في بيئة Jupyter لعرض القيمة  

---

