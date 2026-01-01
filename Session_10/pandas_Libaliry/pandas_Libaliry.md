# Pandas Basics – Session Breakdown (Part 1 & Part 2)

> 📘 **Based strictly on what was covered in the session**
>
> الشرح هنا مبني على الأكواد اللي اشتغلتوا بيها فعلًا، مع تبسيط + أمثلة إضافية **من غير ما نقلل أي محتوى**.

---

## 🔹 Part 1: Pandas Core Basics (Series & DataFrame)

---

## 1️⃣ Introduction to Pandas

**Pandas** هي مكتبة في Python بتستخدم لتحليل البيانات (Data Analysis).

بتشتغل بشكل أساسي على نوعين من البيانات:

* **Series** → بيانات في بعد واحد (1D)
* **DataFrame** → بيانات في بعدين (2D – Rows & Columns)

```python
import pandas as pd  # 📦 Import Pandas library
```

---

## 2️⃣ Python List vs Pandas Series

### 🔸 Python List

```python
a1 = [1, 2, 4, 3]
print(a1)
```

* مجرد قائمة عادية
* مفيش Index مخصص

---

### 🔸 Pandas Series

```python
s1 = pd.Series(a1)
print(s1)
```

📌 **Series**:

* شكلها عمود واحد
* كل قيمة ليها **Index** تلقائي يبدأ من 0

```python
print(s1[1])  # Access by index
```

---

## 3️⃣ Custom Index in Series

```python
a2 = [1, 2, 3, 4]
s2 = pd.Series(a2, index=['day_1', 'day_2', 'day_3', 'day_4'])
print(s2)
```

✅ تقدر تحدد الـ index بنفسك

```python
print(s2['day_2'])
```

---

## 4️⃣ Series from Dictionary

```python
calories = {
    "day": "calories",
    "Day 1": 1650,
    "day_2": 1650,
    "day_3": 1650,
    "day_4": 1650
}

s3 = pd.Series(calories)
print(s3)
```

📌 **Key → Index**
📌 **Value → Data**

---

## 5️⃣ Introduction to DataFrame

### 🔸 Create DataFrame from Dictionary

```python
d1 = {
    "calories": [1258, 1259, 1678, 1654],
    "time": [2, 5, 6, 8]
}

s4 = pd.DataFrame(d1)
print(s4)
```

📊 **DataFrame**:

* Rows + Columns
* كل Column هو Series

---

## 6️⃣ Selecting Rows with loc[]

```python
print(s4.loc[1])        # Single row
print(s4.loc[[1, 2]])   # Multiple rows
print(s4.loc[1:3])      # Slice rows
```

📌 `loc[]` بيشتغل بالـ **labels** (index)

---

## 7️⃣ DataFrame with Custom Index

```python
data = {
    "Name": ["Ahmed", "Mohamed", "Hossam", "Heba", "Mostafa"],
    "Age": [25, 30, 35, 40, 28],
    "City": ["Cairo", "Alex", "Giza", "Luxor", "Aswan"]
}

df3 = pd.DataFrame(data, index=["a", "b", "c", "d", "e"])
print(df3)
```

---

## 8️⃣ Access Specific Data using loc

```python
print(df3.loc["b", "City"])  # Specific cell

print(df3.loc["a":"d", ["Age", "City"]])
```

---

## 9️⃣ Filtering Data (Conditions)

```python
print(df3.loc[df3["Age"] > 30])
```

📌 Filtering مهم جدًا في تحليل البيانات

---

# 🔹 Part 2: Working with CSV Files & Data Cleaning

---

## 🔟 Reading CSV File

```python
data4 = pd.read_csv("data.csv")
print(data4)
```

📌 CSV = Comma Separated Values

---

## 1️⃣1️⃣ Exploring Data

```python
data4.head()      # First 5 rows
data4.tail(15)    # Last 15 rows
data4.info()      # Info about data
data4.describe()  # Statistics
```

---

## 1️⃣2️⃣ Creating New Column using apply()

```python
data4['Calorilevel'] = data4['Calories'].apply(
    lambda x: 'High' if x > 400 else 'Normal'
)

data4.head()
```

📌 `apply()` بتشتغل عنصر عنصر

---

## 1️⃣3️⃣ Handling Missing Values (NaN)

### 🔸 Drop missing values

```python
data5 = data4.dropna()
```

⚠️ بيحذف الصف بالكامل

---

### 🔸 Fill missing values with mean

```python
datanew = pd.read_csv("data.csv")

mean = datanew['Calories'].mean()
print(mean)

datanew.fillna({"Calories": mean}, inplace=True)
```

📌 دي أفضل طريقة في أغلب الحالات

---

## ✅ Summary

### ✔ What You Learned:

* Series vs DataFrame
* Indexing & loc
* Filtering data
* Reading CSV files
* Exploring data
* Creating new columns
* Handling missing values

📈 **ده الأساس الحقيقي لأي شغل Data Analysis باستخدام Pandas**

---

## 🔍 Extra Section: Understanding `data.info()` & `data.describe()`

---

## 📊 Understanding `data.info()`

```python
data4.info()
```

### What `info()` Shows:

* **RangeIndex** → عدد الصفوف (Rows)
* **Columns** → أسماء الأعمدة
* **Non-Null Count** → عدد القيم غير الفارغة (مش NaN)
* **Dtype** → نوع البيانات (int, float, object)
* **Memory usage** → حجم البيانات في الذاكرة

### Why `info()` is Important?

* 🔍 اكتشاف القيم الناقصة (Missing Values)
* 🧠 معرفة نوع كل عمود قبل التحليل
* ⚠️ تحديد الأعمدة اللي محتاجة Cleaning

---

## 📈 Understanding `data.describe()`

```python
data4.describe()
```

### What `describe()` Shows (for numeric columns):

| Metric | Meaning                               |
| ------ | ------------------------------------- |
| count  | عدد القيم غير الفارغة                 |
| mean   | المتوسط الحسابي                       |
| std    | الانحراف المعياري (مدى تشتت البيانات) |
| min    | أقل قيمة                              |
| 25%    | الربع الأول (Q1)                      |
| 50%    | الوسيط (Median)                       |
| 75%    | الربع الثالث (Q3)                     |
| max    | أكبر قيمة                             |

---

## 🧠 How to Use These Values Practically

### 🔹 mean (Average)

```python
avg_calories = data4['Calories'].mean()
print(avg_calories)
```

✔ يستخدم في:

* تعويض القيم الناقصة
* مقارنة البيانات

---

### 🔹 max & min

```python
print(data4['Calories'].max())
print(data4['Calories'].min())
```

✔ يستخدم في:

* معرفة أعلى وأقل قيمة
* اكتشاف Outliers

---

### 🔹 median (50%)

```python
print(data4['Calories'].median())
```

✔ أفضل من mean لو البيانات فيها قيم شاذة

---

### 🔹 std (Standard Deviation)

```python
print(data4['Calories'].std())
```

✔ يوضح مدى تشتت البيانات

---

## 📌 Summary of info() vs describe()

| Function   | Use                        |
| ---------- | -------------------------- |
| info()     | Structure & Missing Values |
| describe() | Statistics & Distribution  |

---

✨ Ready for next step: **Advanced Pandas (groupby, merge, plotting)**
