# 🌳 دليل الـ Decision Tree — شرح شامل بالعربي

---

## 📌 جدول المحتويات

1. [ايه هي الـ Decision Tree؟](#ايه-هي-الـ-decision-tree)
2. [مكونات الشجرة](#مكونات-الشجرة)
3. [ليه بنستخدمها؟](#ليه-بنستخدمها)
4. [ازاي الشجرة بتتعلم — الـ Splitting](#ازاي-الشجرة-بتتعلم--الـ-splitting)
5. [الـ Entropy — قياس الفوضى](#الـ-entropy--قياس-الفوضى)
6. [الـ Information Gain — ازاي نختار أحسن سؤال](#الـ-information-gain--ازاي-نختار-أحسن-سؤال)
7. [مثال كامل بالحساب خطوة خطوة](#مثال-كامل-بالحساب-خطوة-خطوة)
8. [الـ Gini Impurity](#الـ-gini-impurity)
9. [Gini vs Entropy — المقارنة الكاملة](#gini-vs-entropy--المقارنة-الكاملة)
10. [الـ Overfitting وازاي تتجنبه](#الـ-overfitting-وازاي-تتجنبه)
11. [الـ Parameters في sklearn](#الـ-parameters-في-sklearn)
12. [Implementation كامل](#implementation-كامل)
13. [ملخص سريع](#ملخص-سريع)

---

## 🤔 ايه هي الـ Decision Tree؟

الـ **Decision Tree** هي خوارزمية Supervised Machine Learning بتشتغل زي ما بتاخد قرار في الحياة الحقيقية — بتسأل أسئلة وعلى حسب الإجابة بتروح لسؤال تاني، لحد ما توصل للقرار النهائي.

### 🧠 مثال من الحياة — هتطلع ولا لا؟

```
                    ☁️ الجو حر؟
                   /           \
                أيوه            لا
                /                 \
        🌂 معاك مية؟           اخرج ✅
           /       \
        أيوه        لا
        /              \
    اخرج ✅         استنى ❌
```

ده بالظبط شكل الـ Decision Tree! كل سؤال = **Node**، كل إجابة = **Branch**، والنتيجة النهائية = **Leaf**.

---

## 🏗️ مكونات الشجرة

```
                    ┌─────────────────┐
                    │   Root Node 🌱   │  ← أول سؤال بيتسأل (أهم feature)
                    └────────┬────────┘
                    /                  \
           ┌──────────┐          ┌──────────┐
           │  Decision │          │  Decision│  ← أسئلة تانية
           │   Node 🔵 │          │   Node 🔵│
           └─────┬─────┘          └─────┬────┘
                / \                      / \
          ┌───┐   ┌───┐           ┌───┐   ┌───┐
          │🍃 │   │🍃 │           │🍃 │   │🍃 │  ← Leaf Nodes (النتائج)
          └───┘   └───┘           └───┘   └───┘
```

| المصطلح | المعنى |
|---------|--------|
| **Root Node** | أول node في الشجرة — بيحتوي على أهم feature |
| **Decision Node** | node بيسأل سؤال ويتفرع |
| **Leaf Node** | آخر node — مفيش تفريع تاني، بيعطي النتيجة |
| **Branch** | الخط اللي بيربط بين nodes |
| **Sub-Tree** | فرع كامل من الشجرة |
| **Depth** | عمق الشجرة — عدد الأسئلة من الـ root للـ leaf |

---

## ❓ ليه بنستخدمها؟

### المشكلة اللي بتحلها 🔧

تخيل عندنا داتا مش **Linearly Separable** — يعني مينفعش تفصل بين الـ classes بخط مستقيم واحد:

```
  🔴 🟢 🔴         مينفعش خط واحد يفصل الأحمر عن الأخضر هنا!
🟢       🔴
  🟢 🔴 🟢
```

الـ Decision Tree بتحل المشكلة دي عن طريق **تقسيم المساحة** لمناطق صغيرة — كل منطقة بتاخد class معينة ✅

### متى تستخدم الـ Decision Tree؟ 🎯

- ✅ الداتا مش خطية (Non-linear)
- ✅ عندك features مختلطة (أرقام وكاتيجوري)
- ✅ عايز نتيجة سهل تفسيرها
- ✅ مش عايز تعمل preprocessing كتير (مش محتاج Scaling!)
- ✅ Classification أو Regression

---

## ⚙️ ازاي الشجرة بتتعلم — الـ Splitting

الشجرة بتتعلم عن طريق خطوة اسمها **Recursive Binary Splitting**:

```
الداتا الكاملة
      ↓
[سؤال 1: X₀ ≤ -12؟]
   /          \
أيوه           لا
(Leaf ✅)    [سؤال 2: X₀ ≤ 9؟]
               /           \
            أيوه             لا
    [سؤال 3: X₁ ≤ 9؟]    (Leaf ✅)
         /        \
      أيوه          لا
    (Leaf ✅)    (Leaf ✅)
```

> 💡 **السؤال الأساسي:** كل مرة بتسأل — **أحسن سؤال أسأله إيه؟** ده اللي الـ Entropy و Information Gain بيجاوبوه!

---

## 📊 الـ Entropy — قياس الفوضى

### الفكرة 🧠

الـ **Entropy** بتقيس **مقدار الفوضى** في مجموعة. كل ما زادت الفوضى = أصعب تعرف الـ class = أعلى Entropy.

**مثالين:**
- 🟢🟢🟢🟢🟢 → **Entropy = 0** (كلهم نفس الـ class — نقاء كامل ✅)
- 🟢🟢🟢🔴🔴 → **Entropy > 0** (فيه فوضى)
- 🟢🟢🟢🟢🔴🔴🔴🔴 → **Entropy = 1** (أقصى فوضى لـ binary)

### المعادلة 🔢

$$H = -\sum_{i} p_i \cdot \log_2(p_i)$$

حيث:
- $p_i$ = نسبة الـ class $i$ في الـ node
- $\log_2$ = اللوغاريتم الثنائي (الأساس 2)
- القيمة بين **0** (نقاء كامل) و **1** (أقصى فوضى لـ binary)

---

### 📝 أمثلة على حساب الـ Entropy

#### مثال 1: نقاء كامل 🟢
```
Node فيها: 🟢🟢🟢🟢🟢 (5 أخضر، 0 أحمر)

p_أخضر = 5/5 = 1.0
p_أحمر = 0/5 = 0.0

H = -(1.0 × log₂(1.0)) - (0.0 × log₂(0.0))
H = -(1.0 × 0) - 0
H = 0  ✅ نقاء كامل
```

#### مثال 2: فوضى متوسطة
```
Node فيها: 🟢🟢🟢🟢🟢🟢🟢 (8 أخضر) + 🔴🔴🔴🔴🔴 (6 أحمر)
         ← زي ما موضح في الـ PDF: الـ Root Node

p_أخضر = 10/20 = 0.5
p_أحمر  = 10/20 = 0.5

H = -(0.5 × log₂(0.5)) - (0.5 × log₂(0.5))
H = -0.5 × (-1) - 0.5 × (-1)
H = 0.5 + 0.5
H = 1.0  ← أقصى فوضى!
```

> 💡 **ملحوظة:** `log₂(0.5) = -1` عشان `2^(-1) = 0.5`

#### مثال 3: فوضى جزئية — Left Child 🔵
```
← من الـ PDF: Left Child بعد Split الأول
فيها: 🟢🟢🟢🟢🟢🟢🟢🟢🟢 (9 أخضر) + 🔴🔴🔴🔴🔴🔴 (6 أحمر)

p_أخضر = 9/15 ≈ 0.57 (تقريباً من الـ PDF: 0.57)
p_أحمر  = 6/15 ≈ 0.43

H = -(0.57 × log₂(0.57)) - (0.43 × log₂(0.43))
  = -(0.57 × (-0.81)) - (0.43 × (-1.22))
  = 0.46 + 0.52
H ≈ 0.99  ← فوضى عالية جداً
```

#### مثال 4: نقاء كامل — Pure Leaf ✅
```
← من الـ PDF: leaf node فيها 4 أحمر بس
فيها: 🔴🔴🔴🔴 (4 أحمر، 0 أخضر)

p_أحمر  = 4/4 = 1.0
p_أخضر = 0/4 = 0.0

H = -(1.0 × log₂(1.0)) - (0 × log₂(0))
  = -(0) - 0
H = 0  ✅ Pure Node!
```

---

## 🎯 الـ Information Gain — ازاي نختار أحسن سؤال

### الفكرة 💡

الـ **Information Gain** بيقيس **قد ايه السؤال ده بيقلل الفوضى** — الشجرة دايماً بتختار السؤال اللي عنده **أعلى IG**.

### المعادلة 🔢

$$IG = H(\text{parent}) - \sum_{i} \frac{n_i}{n} \cdot H(\text{child}_i)$$

حيث:
- $H(\text{parent})$ = Entropy الـ node الأب
- $n_i$ = عدد الـ samples في الـ child $i$
- $n$ = عدد الـ samples الكلي في الأب
- $H(\text{child}_i)$ = Entropy كل child

---

### 📝 مثال كامل من الـ PDF — مقارنة Split 1 vs Split 2

عندنا **20 sample** في الـ Root Node: **10 أخضر 🟢** و **10 أحمر 🔴**

```
H(parent) = -(0.5 × log₂(0.5)) - (0.5 × log₂(0.5)) = 1.0
```

#### 🔸 Split 1 — بالسؤال X₁ ≤ 4

```
Root (20 samples: 10🟢 10🔴, H=1.0)
              |
    ┌─────────┴──────────┐
    ↓                    ↓
Left Child           Right Child
(14 samples)         (6 samples)
9🟢 + 6🔴            2🟢 + 4🔴
H = 0.99             H = 0.91
```

**حساب IG₁:**
```
IG₁ = H(parent) - [w_left × H(left) + w_right × H(right)]

w_left  = 14/20 = 0.7
w_right = 6/20  = 0.3

IG₁ = 1.0 - [(14/20 × 0.99) + (6/20 × 0.91)]
    = 1.0 - [0.7 × 0.99 + 0.3 × 0.91]
    = 1.0 - [0.693 + 0.273]
    = 1.0 - 0.966
IG₁ = 0.034  ← كمية صغيرة من المعلومات!
```

#### 🔸 Split 2 — بالسؤال X₀ ≤ -12

```
Root (20 samples: 10🟢 10🔴, H=1.0)
              |
    ┌─────────┴──────────┐
    ↓                    ↓
Left Child           Right Child
(4 samples)          (16 samples)
0🟢 + 4🔴            10🟢 + 6🔴
H = 0  (Pure! ✅)     H = 0.95
```

**حساب IG₂:**
```
IG₂ = H(parent) - [w_left × H(left) + w_right × H(right)]

w_left  = 4/20  = 0.2
w_right = 16/20 = 0.8

IG₂ = 1.0 - [(4/20 × 0) + (16/20 × 0.95)]
    = 1.0 - [0.2 × 0 + 0.8 × 0.95]
    = 1.0 - [0 + 0.76]
    = 1.0 - 0.76
IG₂ = 0.24  ← معلومات أكتر بكتير!
```

#### 🏆 النتيجة

```
IG₂ (0.24) > IG₁ (0.034)

∴ الشجرة بتختار Split 2 (X₀ ≤ -12) ✅
```

> 💡 **السبب:** Split 2 خلّى Left Child **Pure تماماً** (Entropy = 0)، ده بيقلل الفوضى الكلية أكتر بكتير!

---

## 🔵 الـ Gini Impurity

### الفكرة 🧠

الـ **Gini** بيسأل: *"لو اخترت sample عشوائي وصنّفتها بناءً على توزيع الـ classes، ما احتمال إنك تغلط؟"*

### المعادلة 🔢

$$Gini = 1 - \sum_{i} p_i^2$$

- القيمة بين **0** (نقاء كامل) و **0.5** (أقصى فوضى لـ binary)
- **مفيش log** — عشان كده أسرع في الحساب!

### 📝 مثال على حساب الـ Gini

```
Node فيها: 3 setosa 🌸 و 1 versicolor 🌺

p_setosa     = 3/4 = 0.75
p_versicolor = 1/4 = 0.25

Gini = 1 - (0.75² + 0.25²)
     = 1 - (0.5625 + 0.0625)
     = 1 - 0.625
Gini = 0.375
```

---

## ⚖️ Gini vs Entropy — المقارنة الكاملة

### مقارنة القيم لنفس الـ Node

| الـ Node | Entropy | Gini |
|---------|---------|------|
| 🟢🟢🟢🟢🟢 (Pure) | **0.0** | **0.0** |
| 🟢🟢🟢🔴 (75/25) | **0.81** | **0.375** |
| 🟢🟢🔴🔴 (50/50) | **1.0** | **0.5** |

### جدول المقارنة الشاملة

| المعيار | 🔵 Gini | 🔴 Entropy |
|---------|---------|----------|
| **المعادلة** | $1 - \sum p_i^2$ | $-\sum p_i \log_2(p_i)$ |
| **نطاق القيمة** | 0 → 0.5 | 0 → 1 |
| **السرعة** | ⚡ أسرع (مفيش عملية log) | 🐢 أبطأ شوية |
| **الحساسية للفوضى** | أقل حساسية | أكثر حساسية |
| **النتايج عملياً** | متشابهين في الغالب | متشابهين في الغالب |
| **الـ default في sklearn** | ✅ أيوه | ❌ لا |
| **امتى تستخدم** | داتا كبيرة، أداء مهم | دقة أعلى، datasets صغيرة |

### 🎯 الخلاصة

```python
# في 90% من الحالات النتيجة متشابهة — جرّب الاتنين!
from sklearn.model_selection import GridSearchCV

param_grid = {'criterion': ['gini', 'entropy']}
grid = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)
grid.fit(X_train, y_train)
print("Best:", grid.best_params_)
```

---

## 🚨 الـ Overfitting وازاي تتجنبه

### المشكلة 😱

لو سبت الشجرة تكبر بدون حدود:

```
❌ شجرة بدون max_depth:
الشجرة بتحفظ كل sample في الـ training
→ accuracy على training = 100%
→ accuracy على test      = 60% فقط!
```

ده بيتسمى **Overfitting** — الموديل حفظ الداتا بدل ما يتعلم.

### الحلول 🛠️

#### 1️⃣ `max_depth` — أهم solution

```python
# بتحدد أقصى عمق للشجرة
dt = DecisionTreeClassifier(max_depth=3)
# depth=3 يعني 3 أسئلة بس من الـ root للـ leaf
```

```
max_depth=None:          max_depth=3:
Root                     Root
├── Node                 ├── Node
│   ├── Node             │   ├── Leaf ✅
│   │   ├── Node         │   └── Leaf ✅
│   │   │   ├── Node     └── Node
│   │   │   └── Leaf         ├── Leaf ✅
...                          └── Leaf ✅
← Overfitting!            ← Balanced ✅
```

#### 2️⃣ `min_samples_split` — أقل عدد لتقسيم Node

```python
# Node مش هتتقسم لو فيها أقل من 20 sample
dt = DecisionTreeClassifier(min_samples_split=20)
```

#### 3️⃣ `min_samples_leaf` — أقل عدد في الـ Leaf

```python
# Leaf لازم يكون فيها على الأقل 5 samples
dt = DecisionTreeClassifier(min_samples_leaf=5)
```

#### 4️⃣ `max_features` — عدد الـ features اللي بيشوفها كل split

```python
# بيشوف بس 50% من الـ features كل مرة
dt = DecisionTreeClassifier(max_features=0.5)
```

---

## 🔧 الـ Parameters في sklearn

```python
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(
    # ========================================
    # criterion: معيار اختيار الـ Split
    # ========================================
    criterion='gini',        # 'gini' أو 'entropy'
    # الفرق موضح بالتفصيل في الجزء السابق

    # ========================================
    # max_depth: أقصى عمق للشجرة
    # ========================================
    max_depth=3,             # None = بدون حد (Overfitting!)
    # كل ما قلّ max_depth → شجرة أبسط → أقل Overfitting

    # ========================================
    # min_samples_split: أقل عدد sample لتقسيم Node
    # ========================================
    min_samples_split=2,     # default=2
    # لو Node فيها 1 sample → مش هتتقسم

    # ========================================
    # min_samples_leaf: أقل عدد sample في الـ Leaf
    # ========================================
    min_samples_leaf=1,      # default=1
    # بيمنع إنشاء Leaf nodes صغيرة جداً

    # ========================================
    # max_features: عدد الـ features لكل split
    # ========================================
    max_features=None,       # None=كل الـ features
    # 'sqrt' = √n_features (شائع في Random Forest)
    # 'log2' = log₂(n_features)
    # int/float = عدد أو نسبة مئوية

    # ========================================
    # max_leaf_nodes: أقصى عدد Leaf Nodes
    # ========================================
    max_leaf_nodes=None,     # None = بدون حد

    # ========================================
    # random_state: لتثبيت النتايج
    # ========================================
    random_state=42
)
```

---

## 💻 Implementation كامل

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix

# ============================================================
# 1️⃣  تحميل الداتا
# ============================================================
iris = load_iris()
X, y = iris.data, iris.target

print("Feature names:", iris.feature_names)
print("Class names  :", iris.target_names)
print("Data shape   :", X.shape)   # (150, 4)

# ============================================================
# 2️⃣  تقسيم الداتا
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y          # بيضمن نفس نسبة كل class في train و test
)

print("Train size:", X_train.shape)  # (112, 4)
print("Test size :", X_test.shape)   # (38,  4)

# ============================================================
# 3️⃣  بناء الـ Model
# ============================================================
dt = DecisionTreeClassifier(
    criterion='entropy',   # بنستخدم Information Gain
    max_depth=3,           # نمنع الـ Overfitting
    random_state=42
)

dt.fit(X_train, y_train)

# ============================================================
# 4️⃣  التقييم
# ============================================================
y_pred = dt.predict(X_test)

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("🎯 Accuracy:", dt.score(X_test, y_test))

# ============================================================
# 5️⃣  رسم الشجرة
# ============================================================
plt.figure(figsize=(18, 10))
texts = plot_tree(
    dt,
    feature_names=iris.feature_names,  # أسامي الـ features
    class_names=iris.target_names,     # أسامي الـ classes
    filled=True,                       # لون كل node بلون الـ class
    rounded=True,                      # زوايا دايرية
    fontsize=12
)
for text in texts:
    text.set_color("black")

plt.title("🌳 Decision Tree — Iris Dataset", fontsize=16)
plt.tight_layout()
plt.show()

# ============================================================
# 6️⃣  Feature Importance — أهم الـ features
# ============================================================
importance = dt.feature_importances_
feature_names = iris.feature_names

print("\n🔍 Feature Importance:")
for name, score in sorted(zip(feature_names, importance), key=lambda x: -x[1]):
    bar = "█" * int(score * 40)
    print(f"  {name:35} {score:.4f}  {bar}")

# ============================================================
# 7️⃣  حساب الـ Entropy يدوياً — للفهم
# ============================================================
def entropy(y):
    """حساب الـ Entropy لمجموعة من الـ labels"""
    classes, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    # تجنب log(0) عن طريق استبعاد الـ probs = 0
    probs = probs[probs > 0]
    return -np.sum(probs * np.log2(probs))

def information_gain(parent, left_child, right_child):
    """حساب الـ Information Gain لـ split معين"""
    n = len(parent)
    n_left  = len(left_child)
    n_right = len(right_child)

    H_parent = entropy(parent)
    H_left   = entropy(left_child)
    H_right  = entropy(right_child)

    weighted = (n_left/n) * H_left + (n_right/n) * H_right
    return H_parent - weighted

# مثال من الـ PDF
print("\n📐 مثال حساب IG يدوياً:")

# نفترض عندنا 10 أخضر و 10 أحمر
parent = [0]*10 + [1]*10

# Split 1: 9 أخضر + 6 أحمر | 1 أخضر + 4 أحمر (تقريبي)
left1  = [0]*9 + [1]*6
right1 = [0]*1 + [1]*4

# Split 2: 0 أخضر + 4 أحمر | 10 أخضر + 6 أحمر (تقريبي)
left2  = [1]*4
right2 = [0]*10 + [1]*6

ig1 = information_gain(parent, left1, right1)
ig2 = information_gain(parent, left2, right2)

print(f"  IG₁ (Split 1) = {ig1:.4f}")
print(f"  IG₂ (Split 2) = {ig2:.4f}")
print(f"  الأفضل: {'Split 2 ✅' if ig2 > ig1 else 'Split 1 ✅'}")

# ============================================================
# 8️⃣  مقارنة Gini vs Entropy
# ============================================================
print("\n📊 مقارنة Gini vs Entropy:")
results = {}
for criterion in ['gini', 'entropy']:
    model = DecisionTreeClassifier(
        criterion=criterion,
        max_depth=3,
        random_state=42
    )
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    results[criterion] = acc
    print(f"  criterion={criterion:>8} → Accuracy: {acc:.4f}")

# ============================================================
# 9️⃣  GridSearchCV لأحسن Parameters
# ============================================================
param_grid = {
    'criterion' : ['gini', 'entropy'],
    'max_depth' : [2, 3, 4, 5, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf' : [1, 2, 4]
}

grid = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid.fit(X_train, y_train)

print("\n🏆 Best Parameters:", grid.best_params_)
print("🎯 Best CV Score  :", f"{grid.best_score_:.4f}")
print("📊 Test Accuracy  :", f"{grid.best_estimator_.score(X_test, y_test):.4f}")
```

---

## 📌 ازاي تقرأ الشجرة بعد ما ترسمها؟

كل node في الرسمة بتحتوي على:

```
┌─────────────────────────────────┐
│  petal length (cm) <= 2.45      │  ← السؤال اللي بيتسأل
│  entropy = 1.585                │  ← الفوضى في الـ node دي
│  samples = 112                  │  ← عدد الـ samples اللي وصلت
│  value = [37, 38, 37]           │  ← توزيع الـ samples على الـ classes
│  class = versicolor             │  ← الـ class الأغلب
└─────────────────────────────────┘
```

**قراءة الـ value:**
```
value = [37, 38, 37]
         ↑    ↑    ↑
      setosa  versicolor  virginica
```

**اللون:** كل ما كان اللون أغمى → الـ Node أكثر نقاءً (أغلبية class واحدة)

---

## 🌟 ملخص سريع

```
Decision Tree
│
├── 📐 أساسها:
│   ├── Entropy   = -Σ p·log₂(p)  → قياس الفوضى
│   ├── Info Gain = H(parent) - Σ w·H(child)  → اختيار أحسن split
│   └── Gini      = 1 - Σ p²     → بديل أسرع للـ Entropy
│
├── 🔧 Parameters مهمة:
│   ├── criterion     → gini أو entropy
│   ├── max_depth     → أهم parameter لمنع Overfitting
│   ├── min_samples_split → أقل عدد لتقسيم node
│   └── min_samples_leaf  → أقل عدد في الـ leaf
│
├── ✅ مميزاتها:
│   ├── سهلة الفهم والتفسير (Interpretable)
│   ├── مش محتاجة Feature Scaling
│   ├── بتتعامل مع Numerical و Categorical
│   └── بتشتغل مع Non-linear data
│
└── ❌ عيوبها:
    ├── Overfitting لو مش محكومة بـ max_depth
    ├── Unstable (تغيير صغير في الداتا → شجرة مختلفة)
    └── Biased مع الـ features اللي ليها قيم كتير
```

---

### 🎯 الخلاصة بجملتين

> **الـ Decision Tree بتسأل أسئلة على الداتا بالترتيب من الأهم للأقل أهمية — بتختار كل سؤال عن طريق الـ Information Gain أو الـ Gini.**
>
> **أهم حاجة دايماً تحط `max_depth` عشان متعملش Overfitting!**

---

*Made with ❤️ — Decision Tree Complete Guide*