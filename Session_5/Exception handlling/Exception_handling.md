# Python Exception Handling 🛑🐍

## 1. Try & Except
### What is Try & Except?
شرح:
- بنستخدم try و except عشان نمسك الأخطاء (errors) بدل ما البرنامج يوقف فجأة ❌
- لو حصل Error جوه try، بايثون تدخل على except وتكمل تنفيذ البرنامج عادي ✅

```python
# 🔹 Example 1: Handling ZeroDivisionError
try:
    result = 10 / 0  # ⚠️ This will cause an error
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")  # 🚫 Division by zero

print("Program continues...")  # ✅ Program does not crash
```

```python
# 🔹 Example 2: Multiple except blocks
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid number!")  # 🔤 Wrong input
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")  # ➗❌
```

---

## 2. Generalized Exception
### What is a General Exception?
شرح:
- Exception هو catch عام يمسك أي نوع Error
- بنستخدمه لما مش متأكدين ايه نوع الخطأ
- الأفضل دايمًا نستخدم Specific Exceptions الأول 👌

```python
# 🔹 Basic generalized exception
try:
    x = 10 / 0
except Exception:
    print("Something went wrong!")  # ⚠️ Generic error
```

```python
# 🔹 Capturing error details
try:
    my_list = [1, 2, 3]
    print(my_list[10])  # ❌ Index error
except Exception as e:
    print(f"Error occurred: {e}")  # 🧾 Error message
    print(f"Error type: {type(e).__name__}")  # 🏷️ Error type
```

```python
# 🔹 Combining specific and general exceptions
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## 3. Try-Except-Else
### What is Else in Exception Handling?
شرح:
- else بتتنفذ بس لو try خلصت من غير أي Error ✅
- مفيدة للكود اللي لازم يتنفذ فقط في حالة النجاح

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
else:
    print(f"Success! Result is: {result}")  # 🎉 No errors happened
```

---

## 4. Try-Except-Finally
### What is Finally?
شرح:
- finally بتتنفذ دايمًا سواء حصل Error أو لا 🔒
- بنستخدمها في cleanup زي قفل الملفات

```python
# 🔹 File handling example
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleanup: This always runs!")  # 🧹 Always executed
```

```python
# 🔹 Finally without error
try:
    result = 10 / 2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Finally block always executes!")  # 🔁
```

---

## 5. Raise (Manually Raising Exceptions)
### What is Raise?
شرح:
- raise بتستخدم عشان تعمل Error بنفسك ✋
- مفيدة في التحقق من المدخلات أو القواعد المنطقية

```python
# 🔹 Simple raise example
age = -5

if age < 0:
    raise ValueError("Age cannot be negative!")  # 🚫 Invalid age
```

```python
# 🔹 Raise with try-except
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age > 120:
        raise ValueError("Age is too high!")
    else:
        print(f"Valid age: {age}")

try:
    check_age(150)
except ValueError as e:
    print(f"Error: {e}")
```

```python
# 🔹 Re-raising exception
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Caught an error, logging it...")
    raise  # 🔄 Re-raise the same error
```

---

## 6. Custom Exceptions
### Why Custom Exceptions?
شرح:
- بنعمل Custom Exception لما نحب نحدد Error خاص بالتطبيق
- بيخلي الكود أوضح وأسهل في الصيانة 🧠

```python
# 🔹 Define custom exception
class NegativeNumberError(Exception):
    pass

def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot calculate square root of negative number!")
    return number ** 0.5

try:
    result = calculate_square_root(-16)
except NegativeNumberError as e:
    print(f"Error: {e}")  # ❗ Custom error caught
```

---

## Extra Notes 📌
- Always prefer **specific exceptions** over generic Exception
- Use finally for cleanup actions
- Raise errors when invalid states occur
- Custom exceptions improve code readability

---

## Summary 🧾
- try/except → Handle errors safely
- Exception → Catch all errors
- else → Runs when no error occurs
- finally → Always runs
- raise → Create your own errors
- Custom Exceptions → Better error management
