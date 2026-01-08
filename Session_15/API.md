# Session 15 -- API Basics

## What is an API?

API = Application Programming Interface\
الـ API هو طريقة تخلي برنامج يكلم برنامج تاني.\
زي دالة (function) بتاخد input وترجع output بس بين أنظمة مختلفة.

------------------------------------------------------------------------

## Function Analogy

الفنكشن:

``` python
def add(a, b):
    return a + b
```

Calling:

``` python
print(add(2,3))
```

الـ API نفس الفكرة بس عبر الإنترنت بدل نفس البرنامج.

------------------------------------------------------------------------

## Frontend & Backend

Frontend: الجزء اللي المستخدم بيشوفه\
Backend: السيرفر + الداتا + اللوجيك\
التواصل بينهم عن طريق API باستخدام HTTP.

------------------------------------------------------------------------

## Why Data Scientist Needs API?

-   جلب بيانات من أنظمة تانية
-   إرسال نتائج موديل
-   ربط موديل بتطبيق

------------------------------------------------------------------------

## XML vs JSON

زمان: XML\
دلوقتي: JSON

مثال JSON:

``` json
{"name":"Ali","age":25}
```

------------------------------------------------------------------------

## Serialization & Deserialization

Serialization: تحويل object إلى JSON\
Deserialization: تحويل JSON إلى object

------------------------------------------------------------------------

## Threading

تشغيل أكتر من مهمة في نفس الوقت.

------------------------------------------------------------------------

## Imports Explanation

``` python
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, request, jsonify
import threading
import time
```

------------------------------------------------------------------------

## Build API

``` python
app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client['CustomersDB']
customers_col = db['Customers']
```

------------------------------------------------------------------------

## GET Endpoint

``` python
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = []
    for doc in customers_col.find():
        doc['_id'] = str(doc['_id'])
        customers.append(doc)
    return jsonify(customers)
```

------------------------------------------------------------------------

## Run API

``` python
def run_flask():
    app.run(port=5000, debug=False, use_reloader=False)

threading.Thread(target=run_flask).start()
time.sleep(1)
```

------------------------------------------------------------------------

## Consuming API

``` python
import requests
response = requests.get('http://127.0.0.1:5000/customers')
print(response.json())
```

------------------------------------------------------------------------

## Port

الـ Port رقم بيميز الخدمة جوه الجهاز. مثال: 5000.

------------------------------------------------------------------------

## DNS

DNS بيحول اسم الموقع لعنوان IP.

------------------------------------------------------------------------

## Final Summary

-   API = طريقة تخلي البرامج تكلم بعض
-   مبني على فكرة الفنكشن
-   Frontend يكلم Backend عبر API
-   JSON هو الشكل الحديث
-   Flask لبناء API
-   MongoDB لتخزين الداتا
-   Threading للتوازي
-   Port لتحديد الخدمة
-   DNS لتحويل الاسم لعنوان

## 🔍 Code Explanation -- شرح الأكواد بالتفصيل

### 1. Imports -- استيراد المكتبات

``` python
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
```

-   `pymongo`: مكتبة للتعامل مع MongoDB من بايثون.
-   `MongoClient`: لعمل اتصال بسيرفر MongoDB.
-   `ObjectId`: نوع خاص تستخدمه MongoDB كـ ID لكل Document.

``` python
from flask import Flask, request, jsonify
```

-   `Flask`: إطار عمل لبناء API.
-   `request`: لاستقبال البيانات من العميل.
-   `jsonify`: لتحويل البيانات إلى JSON.

``` python
import threading
import time
```

-   `threading`: لتشغيل الـ API في Thread منفصل.
-   `time`: للتحكم في التوقيت والانتظار.

------------------------------------------------------------------------

### 2. إنشاء تطبيق Flask

``` python
app = Flask(__name__)
```

-   إنشاء سيرفر API.
-   `__name__` بيحدد اسم الملف الحالي للتطبيق.

------------------------------------------------------------------------

### 3. الاتصال بـ MongoDB

``` python
client = MongoClient("mongodb://localhost:27017")
```

-   اتصال بسيرفر MongoDB المحلي.

``` python
db = client['CustomersDB']
customers_col = db['Customers']
```

-   اختيار Database اسمها CustomersDB.
-   اختيار Collection اسمها Customers.

------------------------------------------------------------------------

### 4. إنشاء Endpoint لعرض العملاء

``` python
@app.route('/customers', methods=['GET'])
def get_customers():
```

-   إنشاء مسار API اسمه `/customers`.
-   يقبل طلبات GET فقط.

``` python
customers = []
for doc in customers_col.find():
    doc['_id'] = str(doc['_id'])
    customers.append(doc)
return jsonify(customers)
```

-   قراءة كل البيانات من MongoDB.
-   تحويل `_id` إلى String عشان ينفع يرجع في JSON.
-   رجوع البيانات في شكل JSON.

------------------------------------------------------------------------

### 5. تشغيل Flask في Thread

``` python
def run_flask():
    app.run(port=5000, debug=False, use_reloader=False)

threading.Thread(target=run_flask).start()
time.sleep(1)
```

-   تشغيل السيرفر على بورت 5000.
-   تشغيله في Thread منفصل.
-   `sleep` علشان ندي وقت للسيرفر يشتغل.

------------------------------------------------------------------------

### 6. استهلاك الـ API باستخدام requests

``` python
import requests
response = requests.get('http://127.0.0.1:5000/customers')
print(response.json())
```

-   إرسال طلب GET للـ API.
-   استلام البيانات في شكل JSON.
-   طباعتها.

------------------------------------------------------------------------

## 🔁 Flow كامل للبرنامج

1.  تشغيل Flask.
2.  الاتصال بـ MongoDB.
3.  إنشاء Endpoint.
4.  العميل يطلب البيانات.
5.  السيرفر يرجع JSON.
6.  العميل يعرض النتيجة.

------------------------------------------------------------------------

## 🎯 ليه ده مهم لـ Data Scientist؟

-   تقدر تجيب بيانات من أي System.
-   تقدر تبني API لنتايج الموديلات.
-   تشتغل مع Frontend بسهولة.
-   تدخل في مشاريع Production حقيقية.
