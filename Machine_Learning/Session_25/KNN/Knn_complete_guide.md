# 🤖 Machine Learning — Session 5
## دليلك الشامل لـ K-Nearest Neighbors (KNN)

> 📌 **ملاحظة:** الشرح ده مصمم يكون سلس ومفيد، فيه رياضيات + كود + أمثلة حقيقية + أسئلة انترفيو 🎯

---

## 📚 فهرس المحتوى

1. [إيه هو KNN؟](#1--إيه-هو-knn)
2. [إزاي KNN بيشتغل؟ (الخطوات)](#2--إزاي-knn-بيشتغل)
3. [مقاييس المسافة](#3--مقاييس-المسافة)
4. [إزاي تختار أفضل قيمة لـ K؟](#4--إزاي-تختار-أفضل-قيمة-لـ-k)
5. [مزايا وعيوب KNN](#5--مزايا-وعيوب-knn)
6. [Implementation بالكود](#6--implementation-بالكود)
7. [أسئلة الانترفيو](#7--أسئلة-انترفيو-مهمة)

---

## 1. 🧠 إيه هو KNN؟

### التعريف

**K-Nearest Neighbors (KNN)** هو خوارزمية تعلم آلي من النوع **Supervised Learning**، بتستخدم في مشكلتين:
- 🔵 **Classification** — تصنيف (مثلاً: هو مريض ولا لأ؟)
- 📈 **Regression** — تنبؤ برقم (مثلاً: سعر الشقة كام؟)

### الفكرة الأساسية

> 💡 "قولي مين جيرانك وأقولك إنت مين"

الخوارزمية بتقول: لو عايز تعرف نوع نقطة جديدة، شوف أقرب K نقاط ليها في البيانات، وخد "التصويت الأغلبي" بينهم!

### 🏷️ خصائص مهمة

| الخاصية | التفاصيل |
|---------|----------|
| **Non-Parametric** | مش بيفترض شكل معين للبيانات (زي Gaussian مثلاً) |
| **Lazy Learning** | مش بيتدرب فعلاً! بيحتفظ بكل البيانات ويستخدمها وقت التنبؤ |
| **Instance-based** | كل قرار بيتاخد بناءً على البيانات الموجودة مباشرة |

### 🌍 أمثلة من الحياة الحقيقية

```
🏥 طب:         تشخيص مريض بناءً على أعراض مشابهة لحالات سابقة
🎬 Netflix:     "الناس اللي بتحب اللي أنت بتحبه، بتحب كمان..."
🏠 عقارات:     تسعير شقة بناءً على شقق مشابهة في نفس الحي
📧 إيميل:      فلتر الـ Spam بناءً على رسائل مشابهة
💳 بنوك:       كشف التزوير بناءً على معاملات مشابهة
```

---

> ### 🎤 سؤال انترفيو #1
> **"إيه الفرق بين Lazy Learning و Eager Learning؟"**
>
> **الإجابة:** الـ Lazy Learning (زي KNN) مش بيبني موديل أثناء التدريب — بيحتفظ بالبيانات كلها وبيستخدمها وقت التنبؤ. الـ Eager Learning (زي Decision Trees) بيبني موديل كامل من البيانات ويرميها. النتيجة: KNN بطيء وقت التنبؤ، سريع وقت "التدريب".

---

## 2. ⚙️ إزاي KNN بيشتغل؟

### الخطوات بالتفصيل

```
الخطوة 1️⃣  →  اختار قيمة K
الخطوة 2️⃣  →  احسب المسافة بين النقطة الجديدة وكل النقاط في التدريب
الخطوة 3️⃣  →  رتب النقاط من الأقرب للأبعد
الخطوة 4️⃣  →  خد أقرب K نقطة
الخطوة 5️⃣  →  صوّت! الأغلبية تكسب (Classification) أو خد المتوسط (Regression)
```

### مثال مرئي 🎨

```
البيانات الموجودة:
  🔴 R1 = (1,1)   🔴 R2 = (2,2)   🔴 R3 = (1,3)
  🔵 B1 = (5,5)   🔵 B2 = (6,4)   🔵 B3 = (5,7)

النقطة الجديدة: 🟢 G = (3,3) ← إيه نوعها؟

مع K=3، أقرب 3 نقاط هي:
  → R2=(2,2)  المسافة ≈ 1.41
  → R1=(1,1)  المسافة ≈ 2.83
  → R3=(1,3)  المسافة ≈ 2.00

النتيجة: 3 نقاط حمراء، 0 زرقاء → 🟢 G = 🔴 RED!
```

### رسم توضيحي (ASCII)

```
7 |         🔵B3
6 |
5 |     🔵B1
4 |       🔵B2
3 |  🔴R3   🟢G←?
2 |   🔴R2
1 |  🔴R1
  +------------------
     1  2  3  4  5  6
```

---

> ### 🎤 سؤال انترفيو #2
> **"إيه معنى إن KNN هو Lazy Learner؟ وإيه التأثير على الـ Performance؟"**
>
> **الإجابة:** معناها إنه مش بيعمل حاجة وقت التدريب — بس يحفظ البيانات. لكن وقت التنبؤ بياخد وقت طويل لأنه لازم يحسب المسافة مع كل نقطة في الـ Training Set. فـ Training Time = O(1) لكن Prediction Time = O(n × d) حيث n هو عدد النقاط و d هو عدد الـ Features.

---

## 3. 📐 مقاييس المسافة

مقياس المسافة هو قلب KNN — بيحدد "مين الجار الأقرب". اختيار المقياس الغلط ممكن يخرب كل حاجة! 😬

---

### 3.1 🏙️ Manhattan Distance (L1)

#### التعريف
سميت Manhattan لأنها زي المشي في شوارع المدينة — ممكن تمشي يمين وشمال بس مش قطري!

```
                B
                |
           ─────┘   ← Manhattan (المسار الأزرق): فقط أفقي وعمودي
          /
         /            ← Euclidean (المسار الأحمر): خط مستقيم
        A
```

#### الصيغة الرياضية

```
                  n
d(A, B) = Σ |Aᵢ - Bᵢ|
                 i=1
```

بالعربي: جمع القيمة المطلقة لكل الفروقات في كل بُعد

#### مثال محلول 🔢

```
النقطة A = (4, 4)
النقطة B = (1, 1)

d = |4-1| + |4-1|
d = 3 + 3
d = 6 ✅
```

#### متى نستخدمها؟
- 🏙️ حساب مسافات في شبكات طرق (Grid-based)
- 📊 بيانات فيها Outliers (أقل حساسية ليهم)
- 🧬 بيانات عالية الأبعاد (High-dimensional data)

---

### 3.2 📏 Euclidean Distance (L2)

#### التعريف
المسافة المباشرة "كما يطير الغراب" — الخط المستقيم بين نقطتين. الأكثر استخداماً في KNN.

#### الصيغة الرياضية

```
                  n
d(A, B) = √ Σ (Aᵢ - Bᵢ)²
                 i=1
```

بالعربي: جذر مجموع مربعات الفروقات

#### مثال محلول 🔢

```
النقطة A = (4, 4)
النقطة B = (1, 1)

d = √[(4-1)² + (4-1)²]
d = √[9 + 9]
d = √18
d ≈ 4.24 ✅
```

#### متى نستخدمها؟
- 📐 البيانات المستمرة الطبيعية
- 🌡️ بيانات زي الطول والوزن
- 🗺️ المسافات الجغرافية الحقيقية

---

### 3.3 🔧 Minkowski Distance (الأم!)

#### التعريف
Minkowski هي الصيغة العامة اللي بتشمل Manhattan و Euclidean كحالات خاصة منها!

#### الصيغة الرياضية

```
                    n           1/p
d(A, B) = [ Σ |Aᵢ - Bᵢ|ᵖ ]
                   i=1

عند p=1  →  Manhattan Distance
عند p=2  →  Euclidean Distance
عند p=∞  →  Chebyshev Distance (أقصى فرق في بُعد واحد)
```

#### مثال توضيحي

```
نفس النقاط A=(4,4), B=(1,1):

p=1:  d = 3+3 = 6           (Manhattan)
p=2:  d = √(9+9) ≈ 4.24    (Euclidean)
p=3:  d = ∛(27+27) ≈ 3.78  (Minkowski مخصص)
```

---

### 3.4 📝 Cosine Similarity & Distance

#### التعريف
بتقيس الزاوية بين متجهين، مش المسافة بينهم! بتسأل: "هل بيشيروا لنفس الاتجاه؟"

#### الصيغة الرياضية

```
                  A · B
cos(θ) = ─────────────────
              ||A|| × ||B||

حيث:
A · B = Σ(Aᵢ × Bᵢ)          (الضرب الداخلي)
||A|| = √(Σ Aᵢ²)             (طول المتجه)

Cosine Distance = 1 - cos(θ)
```

#### النتائج الممكنة

```
cos(θ) = 1   →  نفس الاتجاه تماماً  ✅ (أكثر تشابه)
cos(θ) = 0   →  متعامدان (مش متشابهين)
cos(θ) = -1  →  عكس بعض تماماً  ❌
```

#### مثال حقيقي 📧

```
تحليل النصوص:
  Document 1: "النهارده الجو جميل وحلو"  → Vector: [3, 1, 0, ...]
  Document 2: "النهارده الجو حار ومش كويس" → Vector: [3, 1, 1, ...]

Cosine similarity بتحكيلك إن المستندين بيتكلموا في نفس المجال (الجو)
حتى لو طولهم مختلف!
```

#### متى نستخدمها؟
- 📄 تحليل النصوص (NLP)
- 🔍 محركات البحث
- 🎵 توصيات الموسيقى

---

### 3.5 🔤 Hamming Distance

#### التعريف
بتحسب عدد المواضع اللي فيها اختلاف بين سلسلتين من نفس الطول.

#### الصيغة الرياضية

```
d(A, B) = عدد المواضع اللي فيها Aᵢ ≠ Bᵢ
```

#### مثال 🔢

```
String A: "ABCDE"
String B: "AGDDF"
            ↑ ↑↑
Positions: 2, 4, 5 مختلفة

Hamming Distance = 3 ✅
```

#### مثال بيانات ثنائية

```
Binary A: 1 0 1 1 0 1
Binary B: 1 1 1 0 0 1
               ↑ ↑
           موضع 2 وموضع 4 مختلفين

Hamming Distance = 2 ✅
```

#### متى نستخدمها؟
- 💻 كشف أخطاء الإرسال في الاتصالات
- 🧬 مقارنة تسلسلات DNA
- 🔤 بيانات Categorical (Binary Encoded)

---

### جدول مقارنة المسافات 📊

| المقياس | نوع البيانات | الاستخدام المثالي | الحساسية للـ Outliers |
|---------|------------|-----------------|---------------------|
| Manhattan | مستمرة | البيانات الشبكية | منخفضة ✅ |
| Euclidean | مستمرة | البيانات العامة | متوسطة |
| Minkowski | مستمرة | عام ومرن | متغيرة |
| Cosine | متجهات | النصوص | منخفضة جداً ✅ |
| Hamming | فئوية/ثنائية | النصوص والـ DNA | — |

---

> ### 🎤 سؤال انترفيو #3
> **"إيه الفرق بين Euclidean و Cosine Distance؟ وإمتى تختار كل واحدة؟"**
>
> **الإجابة:**
> - **Euclidean** بتقيس المسافة الفعلية في الفراغ — مهم فيها الحجم والقيم.
> - **Cosine** بتقيس الزاوية بين المتجهين — مهم فيها الاتجاه مش الحجم.
>
> **مثال:** لو Document A فيها كلمة "AI" مرة، و Document B فيها "AI" عشر مرات — Euclidean هتقول مختلفين جداً، Cosine هتقول متشابهين (نفس الموضوع).
> 
> **القاعدة:** NLP/Text → Cosine | البيانات الرقمية العادية → Euclidean

---

> ### 🎤 سؤال انترفيو #4
> **"ليه لازم نعمل Feature Scaling قبل KNN؟"**
>
> **الإجابة:** KNN بيعتمد على حساب المسافات. لو Feature واحدة بقيم كبيرة (مثلاً الراتب: 5000-50000) وفيه Feature تانية بقيم صغيرة (مثلاً العمر: 20-60)، الـ Feature الأول هيسيطر على حساب المسافة وكأن الـ Feature الثانية مش موجودة! الحل: نستخدم **Min-Max Scaling** أو **Standard Scaling** لنخلي كل الـ Features على نفس المقياس.

---

## 4. 🎯 إزاي تختار أفضل قيمة لـ K؟

اختيار K من أهم القرارات في KNN — صغير أوي أو كبير أوي والنتائج بتبوظ! 😅

### تأثير قيمة K على الموديل

```
K صغير جداً (K=1):               K كبير جداً (K=100):
────────────────────             ──────────────────────
✗ Overfitting                    ✗ Underfitting
✗ حساس جداً للـ Noise            ✗ بيتجاهل التفاصيل المهمة
✗ Variance عالية                 ✗ Bias عالي
✓ Training Accuracy عالية        ✓ Smooth boundaries

الحل الأمثل: K في النص! ⭐
```

### رسم توضيحي للـ Decision Boundaries

```
K=1 (Overfitting):     K=5 (مناسب):        K=50 (Underfitting):
┌──────────────┐       ┌──────────────┐      ┌──────────────┐
│ 🔴.🔵.🔴.🔵 │       │  🔴🔴 | 🔵🔵│      │              │
│  حدود معقدة  │       │   حد واضح   │      │  حد مسطح    │
│   جداً 🌀   │       │     ✅      │      │    جداً 😐  │
└──────────────┘       └──────────────┘      └──────────────┘
```

---

### طريقة 1: Grid Search 🔍

بتجرب كل قيم K ممكنة وتشوف أيها أعلى Accuracy

```python
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

# جرب k من 1 لـ 20
param_grid = {'n_neighbors': range(1, 21)}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print(f"أحسن K = {grid_search.best_params_['n_neighbors']}")
print(f"أحسن Accuracy = {grid_search.best_score_:.2f}")
```

---

### طريقة 2: Elbow Method 📈

بترسم منحنى الـ Accuracy مقابل قيم K، وتختار النقطة "المرفق" (Elbow) — النقطة اللي بعدها الـ Accuracy مش بتتحسن كتير.

```
Accuracy
  ↑
  |              🟢 ← Elbow هنا! (K=5)
  |           🟢    🟢🟢🟢🟢🟢  ← بيثبت
  |        🟢
  |     🟢
  |  🟢
  |🟢
  +──────────────────→ K
  1  2  3  4  5  6  7

اختار K = 5 (عند المرفق) — بعديه الـ Accuracy بتثبت أو بتنزل
```

```python
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

accuracy_list = []
k_values = range(1, 31)

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy_list.append(acc)

best_k = k_values[accuracy_list.index(max(accuracy_list))]

plt.plot(k_values, accuracy_list, marker='o', color='green')
plt.xlabel('K Value')
plt.ylabel('Accuracy')
plt.title('Elbow Method - Finding Optimal K')
plt.axvline(x=best_k, color='blue', linestyle='--', label=f'Optimal K={best_k}')
plt.legend()
plt.show()

print(f"✅ أحسن K = {best_k} بـ Accuracy = {max(accuracy_list):.2%}")
```

### 💡 نصائح عملية لاختيار K

```
1️⃣  ابدأ بـ K = √n حيث n هو عدد نقاط التدريب
2️⃣  جرب فقط القيم الفردية (1, 3, 5, 7...) لتجنب التعادل في التصويت
3️⃣  استخدم Cross-Validation للتقييم الموثوق
4️⃣  K الكبير → Smoother Boundaries لكن أبطأ
5️⃣  مع بيانات بها Noise → K أكبر أحسن
```

---

> ### 🎤 سؤال انترفيو #5
> **"إمتى ممكن يحصل Overfitting في KNN؟ وإزاي تحله؟"**
>
> **الإجابة:** يحصل Overfitting في KNN لما K صغير جداً (خصوصاً K=1). في الحالة دي، الموديل بيحفظ كل نقطة بيانات بدل ما يتعلم النمط العام. بيشتغل ممتاز على Training Data لكن بيفشل مع البيانات الجديدة.
>
> **الحل:**
> - زود قيمة K
> - استخدم Cross-Validation
> - اعمل Feature Selection لإزالة الـ Features الغير مفيدة
> - نظّف الـ Outliers من البيانات

---

> ### 🎤 سؤال انترفيو #6
> **"إزاي تختار بين K فردي وزوجي؟"**
>
> **الإجابة:** دايماً فضّل K فردي في مشاكل Binary Classification عشان تتجنب التعادل في التصويت (50%-50%). مثلاً مع K=4، ممكن يطلع 2 حمر و2 زرق — مش عارف يختار! مع K=5، لازم فيه أغلبية.

---

## 5. ⚖️ مزايا وعيوب KNN

### ✅ المزايا

```
1. 🎯 سهل الفهم والتطبيق
   └─ مفيش رياضيات معقدة — فكرة "الجيران" واضحة وبديهية

2. ⚡ لا يحتاج تدريب (Lazy Learning)
   └─ تقدر تضيف بيانات جديدة في أي وقت بدون إعادة التدريب

3. 🔄 يشتغل مع Classification و Regression
   └─ مرن ومتعدد الاستخدامات

4. 📊 Non-parametric
   └─ مش بيفترض شكل معين للبيانات (مش لازم Normal Distribution)

5. 🏆 قوي مع بيانات صغيرة
   └─ بيدي نتايج كويسة مع datasets صغيرة ومعقدة الشكل
```

### ❌ العيوب

```
1. 🐌 بطيء وقت التنبؤ
   └─ O(n × d) لكل تنبؤ — مع ملايين النقاط ده مشكلة كبيرة!

2. 💾 استهلاك ذاكرة عالي
   └─ لازم يحتفظ بكل البيانات في الذاكرة — مفيش "ضغط" للموديل

3. ⚠️ حساس لـ Feature Scaling
   └─ Features بقيم كبيرة تسيطر على حساب المسافة

4. 🎯 حساس لـ Irrelevant Features
   └─ كل feature بتأثر على المسافة — حتى لو مش مهمة

5. 👻 مش بيتعامل مع Missing Values
   └─ لازم تعالج البيانات الناقصة قبل استخدامه

6. 🔴 حساس لـ Outliers
   └─ نقطة واحدة شاذة ممكن تغير التصنيف
```

### متى تستخدم KNN ومتى لا؟ 🤔

```
✅ استخدم KNN لما:              ❌ اجتنب KNN لما:
────────────────────           ─────────────────────
البيانات صغيرة (< 10K)         البيانات ضخمة جداً
التنبؤ مش Real-time            تحتاج سرعة عالية
البيانات منخفضة الأبعاد        Features كتير جداً (> 50)
تريد Baseline سريع             المحمول / البيئات المحدودة
```

---

> ### 🎤 سؤال انترفيو #7
> **"إيه مشكلة الـ Curse of Dimensionality في KNN؟"**
>
> **الإجابة:** لما عدد الـ Features (الأبعاد) بيزيد، المسافات بين كل النقاط بتبقى متقاربة جداً من بعض — فبيبقى صعب تحدد مين "الجار الحقيقي". مثلاً في 1000 بُعد، نقطة قريبة ونقطة بعيدة مسافتهم مش بتختلف كتير! الحل: استخدم **PCA** أو **Feature Selection** لتقليل الأبعاد قبل KNN.

---

## 6. 💻 Implementation بالكود

### Dataset المشكلة: تشخيص مرض السكري 🏥

هنستخدم **Pima Indians Diabetes Dataset** — بيانات حقيقية لتشخيص السكري بناءً على 8 قياسات طبية.

```
Features:
  1. Pregnancies       - عدد مرات الحمل
  2. Glucose           - مستوى السكر في الدم
  3. BloodPressure     - ضغط الدم
  4. SkinThickness     - سماكة الجلد
  5. Insulin           - مستوى الأنسولين
  6. BMI               - مؤشر كتلة الجسم
  7. DiabetesPedigree  - تاريخ عائلي للمرض
  8. Age               - العمر

Target: 0 = مش مريض، 1 = مريض
```

---

### الخطوة 1: استيراد المكتبات

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.datasets import load_iris  # للتجربة السريعة
```

---

### الخطوة 2: تحميل ومعاينة البيانات

```python
# تحميل Dataset السكري
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
           'Insulin', 'BMI', 'DiabetesPedigree', 'Age', 'Outcome']

df = pd.read_csv(url, names=columns)

# معاينة أولية
print("شكل البيانات:", df.shape)
print("\nأول 5 صفوف:")
print(df.head())

print("\nإحصائيات عامة:")
print(df.describe())

print("\nنسبة الفئات:")
print(df['Outcome'].value_counts(normalize=True))
```

**Output متوقع:**
```
شكل البيانات: (768, 9)

نسبة الفئات:
0    0.651  ← 65% مش مرضى
1    0.349  ← 35% مرضى
```

---

### الخطوة 3: تجهيز البيانات (Preprocessing) ⚠️ مهم جداً!

```python
# فصل Features عن Target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y  # ← مهم: يحافظ على نسبة الفئات في كل قسم
)

print(f"Training set: {X_train.shape[0]} sample")
print(f"Test set:     {X_test.shape[0]} sample")

# ⚠️ Feature Scaling - لازم مع KNN!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit هنا بس
X_test_scaled  = scaler.transform(X_test)        # transform بس، مش fit

# ليه؟ عشان نمنع Data Leakage من الـ Test Set للـ Training
```

---

### الخطوة 4: إيجاد أفضل K بـ Elbow Method

```python
error_rates = []
accuracy_list = []
k_range = range(1, 31)

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_pred = knn.predict(X_test_scaled)

    error_rates.append(1 - accuracy_score(y_test, y_pred))
    accuracy_list.append(accuracy_score(y_test, y_pred))

# رسم Elbow Curve
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(k_range, error_rates, color='red', marker='o', markerfacecolor='blue')
axes[0].set_title('Elbow Method - Error Rate vs K')
axes[0].set_xlabel('K Value')
axes[0].set_ylabel('Error Rate')
axes[0].axvline(x=11, color='green', linestyle='--', label='Optimal K=11')
axes[0].legend()

axes[1].plot(k_range, accuracy_list, color='blue', marker='s', markerfacecolor='red')
axes[1].set_title('Accuracy vs K')
axes[1].set_xlabel('K Value')
axes[1].set_ylabel('Accuracy')

plt.tight_layout()
plt.show()

best_k = k_range[error_rates.index(min(error_rates))]
print(f"✅ أحسن K = {best_k}")
```

---

### الخطوة 5: تدريب الموديل النهائي

```python
# تدريب بأحسن K
best_knn = KNeighborsClassifier(
    n_neighbors=11,
    metric='euclidean',    # مقياس المسافة
    weights='distance'     # النقاط الأقرب ليها وزن أكبر
)

best_knn.fit(X_train_scaled, y_train)
y_pred = best_knn.predict(X_test_scaled)

# تقييم الموديل
print("=" * 50)
print("📊 تقرير الأداء:")
print("=" * 50)
print(classification_report(y_test, y_pred, target_names=['لا سكري', 'سكري']))
print(f"\n✅ Accuracy الكلية: {accuracy_score(y_test, y_pred):.2%}")
```

---

### الخطوة 6: Confusion Matrix مرئية

```python
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['لا سكري', 'سكري'],
    yticklabels=['لا سكري', 'سكري']
)
plt.title('Confusion Matrix - KNN Diabetes Detection', fontsize=14)
plt.ylabel('القيمة الحقيقية')
plt.xlabel('القيمة المتوقعة')
plt.tight_layout()
plt.show()

# تفسير الـ Confusion Matrix
tn, fp, fn, tp = cm.ravel()
print(f"""
📊 تفسير النتائج:
  ✅ True Negative  (صح لا سكري): {tn}
  ✅ True Positive  (صح سكري):    {tp}
  ❌ False Positive (خطأ: قال سكري وهو مش):  {fp}
  ❌ False Negative (خطأ: قال مش سكري وهو):  {fn}

⚠️ الـ False Negative خطير هنا (مريض لم يُشخَّص)!
""")
```

---

### الخطوة 7: Grid Search لأفضل Parameters

```python
param_grid = {
    'n_neighbors': [3, 5, 7, 9, 11, 15],
    'metric': ['euclidean', 'manhattan', 'minkowski'],
    'weights': ['uniform', 'distance']
}

grid_search = GridSearchCV(
    KNeighborsClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,  # استخدم كل الـ CPU cores
    verbose=1
)

grid_search.fit(X_train_scaled, y_train)

print(f"🏆 أحسن Parameters: {grid_search.best_params_}")
print(f"🏆 أحسن CV Accuracy: {grid_search.best_score_:.2%}")
```

---

### الخطوة 8: Cross-Validation للتقييم الموثوق

```python
final_model = grid_search.best_estimator_

cv_scores = cross_val_score(
    final_model,
    np.vstack([X_train_scaled, X_test_scaled]),
    pd.concat([y_train, y_test]),
    cv=10,          # 10-Fold Cross Validation
    scoring='accuracy'
)

print(f"""
📊 Cross-Validation Results (10-Fold):
   Mean Accuracy:  {cv_scores.mean():.2%}
   Std Deviation:  {cv_scores.std():.2%}
   Min:            {cv_scores.min():.2%}
   Max:            {cv_scores.max():.2%}
""")
```

---

### الخطوة 9: تجربة عملية — تنبؤ بحالة جديدة 👤

```python
# بيانات مريض جديد
new_patient = pd.DataFrame({
    'Pregnancies': [3],
    'Glucose': [148],
    'BloodPressure': [72],
    'SkinThickness': [35],
    'Insulin': [0],
    'BMI': [33.6],
    'DiabetesPedigree': [0.627],
    'Age': [50]
})

# تطبيق نفس الـ Scaling
new_patient_scaled = scaler.transform(new_patient)

# التنبؤ
prediction = final_model.predict(new_patient_scaled)
probability = final_model.predict_proba(new_patient_scaled)

result = "🔴 مريض بالسكري" if prediction[0] == 1 else "🟢 غير مريض"
print(f"التشخيص: {result}")
print(f"نسبة احتمال الإصابة: {probability[0][1]:.1%}")
```

---

### الكود الكامل في مكان واحد 📋

```python
"""
KNN Complete Implementation - Diabetes Detection
================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. تحميل البيانات
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
           'Insulin', 'BMI', 'DiabetesPedigree', 'Age', 'Outcome']
df = pd.read_csv(url, names=columns)

# 2. تجهيز البيانات
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# 3. إيجاد أفضل K
errors = [1 - accuracy_score(y_test,
          KNeighborsClassifier(n_neighbors=k).fit(X_train_s, y_train).predict(X_test_s))
          for k in range(1, 31)]
best_k = errors.index(min(errors)) + 1
print(f"✅ أحسن K = {best_k}")

# 4. تدريب وتقييم
model = KNeighborsClassifier(n_neighbors=best_k, weights='distance')
model.fit(X_train_s, y_train)
y_pred = model.predict(X_test_s)
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
```

---

> ### 🎤 سؤال انترفيو #8
> **"إيه هو Data Leakage وإزاي KNN ممكن يكون عرضة له؟"**
>
> **الإجابة:** Data Leakage بيحصل لما معلومات من الـ Test Set تتسرب للـ Training. في KNN، اللو عملت `scaler.fit_transform()` على كل البيانات قبل التقسيم، الـ Scaler هيكون شاف إحصائيات الـ Test Set وده غش! الصح: `fit` على Training فقط، `transform` على الاتنين.

---

> ### 🎤 سؤال انترفيو #9
> **"إيه الفرق بين weights='uniform' و weights='distance' في KNN؟"**
>
> **الإجابة:**
> - **uniform:** كل الجيران ليهم نفس الوزن في التصويت (1 صوت لكل واحد)
> - **distance:** الجيران الأقرب ليهم وزن أكبر (وزن = 1/distance)
>
> `weights='distance'` بيدي نتائج أحسن في الغالب لأنه بيقول: "رأي الجار الأقرب أهم من الجار البعيد".

---

> ### 🎤 سؤال انترفيو #10
> **"إزاي تعمل KNN بشكل أسرع مع datasets كبيرة؟"**
>
> **الإجابة:** الـ sklearn بيدعم خوارزميات بيانية أسرع:
> - **KD-Tree:** بيقسم الفضاء لأشجار — سريع جداً في البيانات المنخفضة الأبعاد (< 20 feature)
> - **Ball-Tree:** أحسن مع الأبعاد العالية والمسافات غير-Euclidean
> - **Brute Force:** بيحسب كل المسافات — الأبطأ لكن الأدق
>
> ```python
> knn = KNeighborsClassifier(algorithm='kd_tree')  # أو 'ball_tree'
> ```

---

## 7. 📝 ملخص أسئلة الانترفيو

| # | السؤال | الكلمة المفتاحية |
|---|--------|-----------------|
| 1 | الفرق بين Lazy و Eager Learning | Training Time vs Prediction Time |
| 2 | تأثير Lazy Learning على الـ Performance | O(n×d) prediction |
| 3 | Euclidean vs Cosine Distance | Magnitude vs Direction |
| 4 | ليه Feature Scaling ضروري | Dominating Features |
| 5 | Overfitting في KNN | K صغير جداً |
| 6 | K فردي ولا زوجي | Tie-breaking |
| 7 | Curse of Dimensionality | PCA / Feature Selection |
| 8 | Data Leakage | fit على Training فقط |
| 9 | uniform vs distance weights | Weighted Voting |
| 10 | تسريع KNN | KD-Tree / Ball-Tree |

---

## 🎓 خلاصة الدرس

```
KNN = "قولي مين جيرانك وأقولك إنت مين"

✅ بسيط، بديهي، بدون تدريب
✅ مناسب للبيانات الصغيرة والمعقدة

⚠️ لازم Feature Scaling
⚠️ اختار K بالـ Elbow Method
⚠️ حساس للـ Outliers والـ Noise

🔑 الـ Trade-off الأساسي:
   K صغير = Overfitting (Variance عالية)
   K كبير = Underfitting (Bias عالي)
   K مناسب = التوازن ✨
```

---

> 💡 **نصيحة أخيرة:** KNN ممتاز كـ **Baseline Model** — استخدمه أول حاجة لتقييم البيانات، وبعدين قارن بيه موديلات أعقد زي Random Forest أو SVM.

---

*📖 المصدر: Machine Learning Session 5 — K-Nearest Neighbors*
