
# Python File Handling 📁

## 1. Opening a File
**شرح بالعربي:**  
فتح الملف هو أول خطوة للتعامل مع الملفات في بايثون، سواء قراءة أو كتابة أو إضافة بيانات. لازم دايمًا نقفل الملف بعد ما نخلص علشان نحافظ على الموارد 🧠.

**Syntax:**
```python
file = open("filename", "mode")  # 📂 Open file
```

**Purpose:**  
Open a file to read, write, or append data.

**Important:**  
- Always close the file using `file.close()` ❗  
- To check if file is closed use `file.closed`

**File Modes:**
- `"r"` Read 📖  
- `"w"` Write ✍️  
- `"a"` Append ➕  
- `"r+"` Read & Write 🔁  
- `"x"` Create 🆕

```python
file = open("example.txt", "r")  # 📖 Read mode
print(file.name)
print(file.mode)
file.close()  # 🔒 Close file
print(file.closed)
```

---

## 2. Reading a File
**شرح بالعربي:**  
القراءة بتسمحلك تجيب البيانات من الملف، يا إما كله مرة واحدة أو سطر سطر حسب احتياجك 👀.

### Reading Methods:
- `read()`  
- `read(n)`  
- `readline()`  
- `readlines()`

```python
file = open("example.txt", "r")
content = file.read()  # 📖 Read all
print(content)
file.close()
```

```python
file = open("example.txt", "r")
print(file.read(10))  # 🔢 First 10 chars
file.close()
```

```python
file = open("example.txt", "r")
print(file.readline())  # ➡️ Line 1
print(file.readline())  # ➡️ Line 2
file.close()
```

```python
file = open("example.txt", "r")
lines = file.readlines()  # 📋 List of lines
for line in lines:
    print(line.strip())
file.close()
```

---

## 3. Writing to a File
**شرح بالعربي:**  
الكتابة بتستخدم لحفظ بيانات جديدة أو تعديل بيانات قديمة. خلي بالك إن وضع `"w"` بيمسح القديم ⚠️.

```python
file = open("output.txt", "w")
file.write("Hello from Python!\n")
file.write("This is line 2")
file.close()
```

```python
file = open("output.txt", "a")  # ➕ Append
file.write("\nThis is line 3")
file.close()
```

```python
lines = ["First line\n", "Second line\n", "Third line"]
file = open("data.txt", "w")
file.writelines(lines)
file.close()
```

---

## 4. Reading + Writing (r+ mode)
**شرح بالعربي:**  
الوضع ده بيسمحلك تقرأ وتكتب في نفس الوقت بدون مسح المحتوى، لكن لازم الملف يكون موجود 📝.

```python
file = open("data.txt", "r+")
content = file.read()
print(content)
file.write("\nPython is awesome")
file.close()
```

```python
file = open("notes.txt", "r+")
file.read()
file.seek(0)  # 🔄 Move pointer
file.write("New Line")
file.close()
```

---

## 5. Using 'with' Statement (Best Practice)
**شرح بالعربي:**  
أفضل طريقة للتعامل مع الملفات 👍، بتقفل الملف أوتوماتيك حتى لو حصل Error.

```python
with open("example.txt", "r") as file:
    print(file.read())
```

```python
with open("output.txt", "w") as file:
    file.write("First line\nSecond line")
```

---

## 6. Checking if File Exists
**شرح بالعربي:**  
مهم جدًا تتأكد إن الملف موجود قبل ما تفتحه أو تمسحه علشان تتجنب Errors ❌.

```python
import os

if os.path.exists("example.txt"):
    with open("example.txt", "r") as file:
        print(file.read())
else:
    print("File does not exist!")
```

---

## 7. Deleting a File
**شرح بالعربي:**  
حذف الملفات لازم يكون بحذر ⚠️، ودايمًا اتأكد إن الملف موجود.

```python
import os

if os.path.exists("temp.txt"):
    os.remove("temp.txt")
    print("File deleted!")
else:
    print("File does not exist!")
```

---

## Extra Notes ⭐
- استخدم `with` دايمًا لو تقدر
- اقفل أي ملف بتفتحه
- اختار الـ mode الصح حسب هدفك

🔥 **كده أنت جاهز تتعامل مع الملفات في Python باحتراف**
