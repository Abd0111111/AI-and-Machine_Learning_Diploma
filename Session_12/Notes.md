# SQL Fundamentals – Complete Session with Examples

## 1️⃣ Introduction to SQL

### What is SQL?
SQL هي لغة بتستخدم للتعامل مع قواعد البيانات العلائقية (Relational Databases).

نستخدم SQL علشان:
- إنشاء Databases  
- إنشاء Tables  
- إدخال البيانات  
- تعديل البيانات  
- حذف البيانات  
- استرجاع البيانات  

### What does SQL stand for?
SQL = Structured Query Language

- Structured → منظمة  
- Query → استعلام  
- Language → لغة  

---

## 2️⃣ SQL Command Categories

### DDL – Data Definition Language
بتتحكم في هيكل الداتا.

أهم أوامر DDL:
- CREATE  
- ALTER  
- DROP  
- TRUNCATE  

مثال:
```sql
CREATE TABLE test (
    id INT
);
```

### DML – Data Manipulation Language
بتتعامل مع البيانات نفسها.

أهم أوامر DML:
- INSERT  
- UPDATE  
- DELETE  
- SELECT  

مثال:
```sql
INSERT INTO test VALUES (1);
```

### Difference between DDL & DML

| DDL | DML |
|---|---|
| بتتعامل مع الهيكل | بتتعامل مع البيانات |
| CREATE, DROP | INSERT, UPDATE |
| أقل استخدامًا | استخدام يومي |

---

## 3️⃣ SQL Server & SSMS Overview

### What is SQL Server?
Database Management System (DBMS) من Microsoft.

مسؤول عن:
- تخزين البيانات  
- إدارة البيانات  
- الأمان  
- الأداء  

### What is SSMS?
SQL Server Management Studio

أداة رسومية نستخدمها:
- نكتب SQL Queries  
- ننشئ Databases  
- نشوف Tables و Data  

---

## 4️⃣ Creating a Database in SSMS

### Using GUI
- فتح SSMS  
- Connect على السيرفر  
- Right Click على Databases  
- New Database  
- Database Name: `company`  
- OK  

### Database Files
- Data File (ROWS)  
- Log File (LOG)  

Default Size:
- 8 MB Data  
- 8 MB Log  

Create Database using SQL:
```sql
CREATE DATABASE company;
```

---

## 5️⃣ Database Structure Basics

| Concept | Meaning |
|---|---|
| Database | حاوية البيانات |
| Table | جدول |
| Column | عمود |
| Row | صف |

---

## 6️⃣ Creating Tables (DDL)

### Customers
```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY NOT NULL,
    customer_name VARCHAR(50) NOT NULL,
    customer_age INT NOT NULL,
    cutomer_gender VARCHAR(6) NULL,
    customer_regiend VARCHAR(100) NULL
);
```

### Products
```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price INT NOT NULL
);
```

### Orders
```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY NOT NULL,
    customer_id INT NOT NULL,
    order_date DATE,
    total_amonant INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

### Order Details
```sql
CREATE TABLE order_details (
    order_details_id INT PRIMARY KEY NOT NULL,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

---

## 7️⃣ Keys & Relationships

### Primary Key
- Unique  
- NOT NULL  
- يميز كل Row  

### Foreign Key
- بيربط جدول بجدول  
- يمنع إدخال بيانات غلط  

---

## 8️⃣ Constraints in SQL

قوانين لضمان صحة البيانات:
- PRIMARY KEY  
- FOREIGN KEY  
- UNIQUE  
- NOT NULL  

### UNIQUE Constraint
- يمنع التكرار  
- ممكن يقبل NULL  

```sql
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);
```

---

## 9️⃣ Indexes

طريقة لتسريع البحث.

```sql
CREATE INDEX idx_customer_name
ON customers(customer_name);
```

- SELECT أسرع  
- INSERT و UPDATE أبطأ  

---

## 1️⃣0️⃣ Big O Notation

| Type | Meaning |
|---|---|
| O(1) | ثابت |
| O(log n) | سريع |
| O(n) | خطي |
| O(n²) | بطيء |

Index → O(log n)

---

## 1️⃣1️⃣ Pointer Concept

- Reference لمكان في الذاكرة  
- مستخدمة داخليًا في DBMS  
- بتحسن الأداء  

---

## 1️⃣2️⃣ Data Manipulation Language

### INSERT
```sql
INSERT INTO customers
(customer_id, customer_name, customer_age, cutomer_gender, customer_regiend)
VALUES
(2227253, 'ABDELRAHMAN', 21, 'MALE', 'CAIRO');
```

### INSERT Multiple Rows
```sql
INSERT INTO products VALUES
(1,'Laptop','Electronics',15000),
(2,'Mouse','Electronics',300);
```

### UPDATE
```sql
UPDATE customers
SET customer_regiend = 'GIZA'
WHERE customer_id = 2227253;
```

### DELETE
```sql
DELETE FROM customers
WHERE customer_id = 2227253;
```

بدون WHERE يعني حذف كل الجدول.

---

## 1️⃣3️⃣ Learning Resource
W3Schools

---

## Final Takeaway
- SQL أساس أي Backend أو Data Career  
- فهم Structure و Commands ضروري  
- ده أساس لأي مستوى متقدم
- by Manzzzy