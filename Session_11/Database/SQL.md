# SQL Basics – Structured Query Language

## What is SQL?

SQL (Structured Query Language) هي لغة قياسية تُستخدم للتعامل مع قواعد البيانات العلائقية (Relational Databases).

نستخدم SQL من أجل:

* إنشاء قواعد بيانات وجداول
* إدخال البيانات
* قراءة البيانات (Queries)
* تعديل البيانات
* حذف البيانات

---

## What is a Relational Database?

قاعدة البيانات العلائقية بتكون عبارة عن جداول (Tables).
كل جدول:

* بيتكون من أعمدة (Columns)
* وكل صف (Row) يمثل Record

مثال على جدول Students:

| id | name  | age |
| -- | ----- | --- |
| 1  | Ahmed | 20  |
| 2  | Sara  | 22  |

---

## SQL Database Management Systems (DBMS)

أشهر أنظمة قواعد بيانات SQL:

* MySQL
* PostgreSQL
* SQLite
* SQL Server
* Oracle

---

## SQL Data Types (Basic)

### Common Data Types

* INT : أرقام صحيحة
* FLOAT / DOUBLE : أرقام عشرية
* VARCHAR(n) : نص بطول محدد
* TEXT : نص طويل
* DATE : تاريخ
* BOOLEAN : true / false

Example:

```sql
CREATE TABLE users (
    id INT,
    name VARCHAR(50),
    age INT,
    is_active BOOLEAN
);
```

---

## CREATE TABLE

نستخدمها لإنشاء جدول جديد.

```sql
CREATE TABLE students (
    id INT,
    name VARCHAR(100),
    age INT
);
```

---

## INSERT INTO

نستخدمها لإدخال بيانات داخل الجدول.

```sql
INSERT INTO students VALUES (1, 'Ahmed', 20);
INSERT INTO students VALUES (2, 'Mona', 22);
```

---

## SELECT (Reading Data)

نستخدمها لقراءة البيانات من الجدول.

```sql
SELECT * FROM students;
```

اختيار أعمدة محددة:

```sql
SELECT name, age FROM students;
```

---

## WHERE (Filtering Data)

نستخدمها لتصفية البيانات.

```sql
SELECT * FROM students WHERE age > 20;
```

---

## ORDER BY

ترتيب النتائج.

```sql
SELECT * FROM students ORDER BY age ASC;
SELECT * FROM students ORDER BY age DESC;
```

---

## LIMIT

تحديد عدد النتائج.

```sql
SELECT * FROM students LIMIT 2;
```

---

## UPDATE

تعديل بيانات موجودة.

```sql
UPDATE students
SET age = 21
WHERE name = 'Ahmed';
```

---

## DELETE

حذف بيانات.

```sql
DELETE FROM students WHERE id = 2;
```

---

## Primary Key

مفتاح أساسي يميز كل Record.

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

---


## Database Relationships (Very Important ⭐)

العلاقات بين الجداول هي أساس تصميم أي Database صح.
العلاقة معناها: إزاي جدول مرتبط بجدول تاني باستخدام مفاتيح (Keys).

---

## 1️⃣ One To One Relationship

علاقة واحد لواحد.

🔹 كل صف في الجدول الأول ليه صف واحد بس في الجدول التاني.

### Example

* Person ↔ Passport

### Tables

Persons Table:
| id | name |

Passports Table:
| id | passport_number | person_id |

```sql
CREATE TABLE persons (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE passports (
    id INT PRIMARY KEY,
    passport_number VARCHAR(20) UNIQUE,
    person_id INT UNIQUE,
    FOREIGN KEY (person_id) REFERENCES persons(id)
);
```

📌 UNIQUE هنا مهمة علشان تضمن إن كل شخص ليه باسبور واحد بس.

---

## 2️⃣ One To Many Relationship (الأشهر 🔥)

🔹 صف واحد في جدول مرتبط بعدة صفوف في جدول تاني.

### Example

* Student → Courses
* Department → Employees

### Tables Example

Students Table:
| id | name |

Courses Table:
| id | course_name | student_id |

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE courses (
    id INT PRIMARY KEY,
    course_name VARCHAR(50),
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
```

📌 هنا الطالب الواحد ممكن يكون له أكتر من كورس.

---

## 3️⃣ Many To Many Relationship

🔹 كل صف في الجدول الأول مرتبط بعدة صفوف في الجدول التاني والعكس.

### Example

* Students ↔ Subjects

📌 الحل هنا لازم **جدول وسيط (Junction Table)**.

### Tables

Students:
| id | name |

Subjects:
| id | subject_name |

Student_Subjects (Junction Table):
| student_id | subject_id |

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE subjects (
    id INT PRIMARY KEY,
    subject_name VARCHAR(50)
);

CREATE TABLE student_subjects (
    student_id INT,
    subject_id INT,
    PRIMARY KEY (student_id, subject_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);
```

📌 الجدول الوسيط هو اللي بيحقق العلاقة Many to Many.

---

## JOIN (Combining Tables)

الـ JOIN بيستخدم علشان نعرض بيانات من أكتر من جدول مع بعض.

---

### INNER JOIN

بيرجع الصفوف اللي ليها تطابق في الجدولين.

```sql
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.id = courses.student_id;
```

---

### LEFT JOIN

بيرجع كل بيانات الجدول الأول حتى لو مفيش تطابق.

```sql
SELECT students.name, courses.course_name
FROM students
LEFT JOIN courses
ON students.id = courses.student_id;
```

---

### RIGHT JOIN

بيرجع كل بيانات الجدول التاني.

```sql
SELECT students.name, courses.course_name
FROM students
RIGHT JOIN courses
ON students.id = courses.student_id;
```

---

## Aggregate Functions

دوال بتشتغل على مجموعة بيانات.

* COUNT
* SUM
* AVG
* MIN
* MAX

```sql
SELECT COUNT(*) FROM students;
SELECT AVG(age) FROM students;
SELECT MIN(age), MAX(age) FROM students;
```

---

## GROUP BY

بتجمع البيانات حسب عمود معين.

```sql
SELECT age, COUNT(*)
FROM students
GROUP BY age;
```

---

## HAVING

فلترة بعد GROUP BY.

```sql
SELECT age, COUNT(*)
FROM students
GROUP BY age
HAVING COUNT(*) > 1;
```

---

## Constraints (Rules on Columns)

* PRIMARY KEY
* FOREIGN KEY
* UNIQUE
* NOT NULL
* CHECK

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT CHECK (age >= 18)
);
```

---
## Final Summary

في الجزئين دول اتعلمنا أساسيات SQL بشكل متكامل، وبقينا فاهمين إزاي نتعامل مع قواعد البيانات العلائقية خطوة بخطوة:

### 🔹 أساسيات SQL

* يعني إيه SQL وليه بنستخدمها
* يعني إيه Relational Database
* فكرة الجداول (Tables) والصفوف (Rows) والأعمدة (Columns)
* إنشاء الجداول باستخدام `CREATE TABLE`
* إدخال البيانات باستخدام `INSERT INTO`
* قراءة البيانات باستخدام `SELECT`
* التصفية باستخدام `WHERE`
* الترتيب باستخدام `ORDER BY`
* التعديل باستخدام `UPDATE`
* الحذف باستخدام `DELETE`

### 🔹 العلاقات بين الجداول (Relationships)

* أنواع العلاقات:

  * One To One
  * One To Many
  * Many To Many
* استخدام Junction Tables في علاقات Many To Many
* مفهوم الـ Primary Key والـ Foreign Key
* ربط الجداول ببعض باستخدام Foreign Key

### 🔹 التعامل مع أكثر من جدول

* استخدام `JOIN` بأنواعه:

  * INNER JOIN
  * LEFT JOIN
  * RIGHT JOIN
* فهم الفرق بين أنواع الـ JOIN واستخدام كل نوع

### 🔹 الدوال والتجميع

* Aggregate Functions:

  * COUNT
  * SUM
  * AVG
  * MIN
  * MAX
* استخدام `GROUP BY` لتجميع البيانات
* استخدام `HAVING` للتصفية بعد التجميع

### 🔹 القيود (Constraints)

* NOT NULL
* UNIQUE
* PRIMARY KEY
* FOREIGN KEY
* CHECK

🔥 بعد المرحلة دي، تقدر تقول إنك فاهم أساس SQL صح، ومؤهل تدخل على مستوى **Advanced SQL** وانت مطمّن، وتبدأ تتعامل مع Queries أعقد وقواعد بيانات حقيقية في مشاريع عملية.



