# 🚀 دليل الـ Pipeline في Scikit-Learn — شرح شامل بالعربي

---

## 📌 جدول المحتويات

1. [ايه هي الـ Pipeline؟](#ايه-هي-الـ-pipeline)
2. [ليه بنعملها؟](#ليه-بنعملها)
3. [ازاي بتشتغل من جوا؟](#ازاي-بتشتغل-من-جوا)
4. [ازاي تعمل Pipeline — Implementation](#ازاي-تعمل-pipeline--implementation)
5. [كل الـ Features بتاعتها](#كل-الـ-features-بتاعتها)
6. [مثال كامل — Breast Cancer Model](#مثال-كامل--breast-cancer-model)
7. [أنواع الـ Pipelines](#أنواع-الـ-pipelines)
8. [Pipeline مع GridSearchCV](#pipeline-مع-gridsearchcv)
9. [الأخطاء الشائعة وازاي تتجنبها](#الأخطاء-الشائعة-وازاي-تتجنبها)
10. [ملخص سريع](#ملخص-سريع)

---

## 🤔 ايه هي الـ Pipeline؟

الـ **Pipeline** هي زي "خط تجميع" — بتحط فيها كل الخطوات اللي بتعملها على الداتا بالترتيب في **حاجة واحدة بس**.

تخيل معايا إنك بتعمل عصير برتقال 🍊:

```
خطوة 1: تقشر البرتقالة
خطوة 2: تعصرها
خطوة 3: تضيف سكر
```

من غير Pipeline: بتعمل كل خطوة لوحدها وبتحفظ كل أداة لوحدها.
مع Pipeline: بتحط التلات خطوات في **ماكينة واحدة** وبتقولها "اشتغلي".

```python
from sklearn.pipeline import Pipeline

# كل الخطوات في سطرين بس ✨
pipeline = Pipeline([
    ('scaler',     StandardScaler()),       # خطوة 1: تطبيع الداتا
    ('classifier', LogisticRegression())    # خطوة 2: تدريب الموديل
])
```

---

## ❓ ليه بنعملها؟

### المشكلة اللي بتحلها 🛠️

من **غير** Pipeline بتعمل كده:

```python
# ❌ الطريقة القديمة — مشكلة!

# خطوة 1: الـ Scaling
sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled  = sc.transform(X_test)       # لازم تفكر تعملها بنفسك!

# خطوة 2: التدريب
clf = LogisticRegression()
clf.fit(X_train_scaled, y_train)

# خطوة 3: التنبؤ
y_pred = clf.predict(X_test_scaled)         # لو نسيت الـ scale هتاخد نتايج غلط!

# خطوة 4: الحفظ — 3 فايلات!
joblib.dump(clf, 'classifier.joblib')
joblib.dump(sc,  'scaler.joblib')           # لو ضيعته الموديل مش هيشتغل!
joblib.dump(le,  'label_encoder.joblib')
```

**المشاكل هنا:**
- 🔴 لو نسيت تعمل `sc.transform()` على الـ test data — نتايجك هتبقى **غلط تماماً**
- 🔴 بتحتاج تحفظ وتحمّل **3 فايلات** منفصلين
- 🔴 الكود كبير ومعقد وسهل تغلط فيه
- 🔴 لو شغّلت على production ونسيت الـ scaler — **كارثة** 💥

---

مع **Pipeline** بيبقى كده:

```python
# ✅ الطريقة الصح — مع Pipeline

pipeline = Pipeline([
    ('scaler',     StandardScaler()),
    ('classifier', LogisticRegression())
])

pipeline.fit(X_train, y_train)              # بيعمل fit للـ scaler والـ classifier مع بعض
y_pred = pipeline.predict(X_test)          # بيعمل scale تلقائياً جوّاه ✨

# حفظ فايل واحد بس!
joblib.dump(pipeline, 'pipeline.joblib')
```

**الفوايد:**
- ✅ مستحيل تنسى الـ scale — بيتعمل تلقائي
- ✅ فايل واحد بس بيحفظ كل حاجة
- ✅ الكود أنظف وأقصر
- ✅ آمن على الـ production

---

## ⚙️ ازاي بتشتغل من جوا؟

الـ Pipeline بتتعامل مع كل step بطريقة مختلفة حسب الموقف:

### 🔵 وقت الـ `fit()`:

```
X_train → [Step 1: fit_transform] → [Step 2: fit_transform] → ... → [آخر Step: fit فقط]
```

يعني:
- كل خطوة **غير الأخيرة** بتعمل `fit_transform()` وبتبعت الناتج للخطوة الجاية
- الخطوة الأخيرة (الـ model) بتعمل `fit()` بس

### 🟢 وقت الـ `predict()`:

```
X_test → [Step 1: transform] → [Step 2: transform] → ... → [آخر Step: predict]
```

يعني:
- كل خطوة **غير الأخيرة** بتعمل `transform()` بس (مش fit — عشان مش هتعلم على test data!)
- الخطوة الأخيرة بتعمل `predict()`

> 💡 **ملحوظة مهمة:** الـ Pipeline بتضمن إن الـ fit بيتعمل على الـ training data بس، والـ transform بيتطبق على أي داتا جديدة. ده بيحميك من **Data Leakage**!

---

## 💻 ازاي تعمل Pipeline — Implementation

### 1️⃣ أبسط pipeline ممكنة

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# الـ Pipeline بتاخد list من tuples: ('اسم', object)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model',  LogisticRegression())
])

# Train
pipeline.fit(X_train, y_train)

# Predict — الـ scaler بيشتغل تلقائياً
y_pred = pipeline.predict(X_test)
```

---

### 2️⃣ Pipeline بخطوات أكتر

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC

pipeline = Pipeline([
    ('scaler', StandardScaler()),    # خطوة 1: تطبيع
    ('pca',    PCA(n_components=10)),# خطوة 2: تقليل الأبعاد
    ('model',  SVC())                # خطوة 3: الموديل
])

pipeline.fit(X_train, y_train)
print(pipeline.score(X_test, y_test))
```

---

### 3️⃣ الوصول لـ Step معين جوا الـ Pipeline

```python
# عن طريق الاسم
scaler = pipeline.named_steps['scaler']

# عن طريق الـ index
scaler = pipeline.steps[0][1]

# شوف parameters الـ scaler
print(scaler.mean_)
print(scaler.scale_)
```

---

### 4️⃣ حفظ وتحميل الـ Pipeline

```python
import joblib

# حفظ
joblib.dump(pipeline, 'my_pipeline.joblib')

# تحميل
pipeline = joblib.load('my_pipeline.joblib')

# استخدام على داتا جديدة — مفيش حاجة تاني محتاجها
prediction = pipeline.predict(new_data)
```

---

## 🌟 كل الـ Features بتاعتها

### 🔹 Feature 1: `fit()` و `predict()`

```python
# بيعمل كل الخطوات مرة واحدة
pipeline.fit(X_train, y_train)

# بيعمل transform لكل خطوة وبعدين predict
y_pred = pipeline.predict(X_test)
```

---

### 🔹 Feature 2: `fit_transform()`

```python
# بيعمل fit وبعدين بيرجع الـ transformed data
# مفيد لو عايز تشوف الداتا بعد الـ preprocessing
X_transformed = pipeline.fit_transform(X_train, y_train)
```

---

### 🔹 Feature 3: `predict_proba()`

```python
# لو الـ classifier بيدعم predict_proba
# الـ Pipeline بتعمل scale تلقائياً وبعدين predict_proba
probabilities = pipeline.predict_proba(X_test)
print(probabilities[:, 1])  # احتمال الـ class الموجب
```

---

### 🔹 Feature 4: `score()`

```python
# بيحسب الـ accuracy مباشرة
accuracy = pipeline.score(X_test, y_test)
print(f"Accuracy: {accuracy:.4f}")
```

---

### 🔹 Feature 5: `set_params()` — تغيير Parameters

```python
# تغيير parameter في step معين
# الصيغة: اسم_الـstep__اسم_الـparameter
pipeline.set_params(model__C=0.5)
pipeline.set_params(scaler__with_mean=False)

# مفيد جداً مع GridSearchCV
```

---

### 🔹 Feature 6: `get_params()`

```python
# شوف كل الـ parameters
params = pipeline.get_params()
print(params)

# Output:
# {
#   'scaler': StandardScaler(),
#   'scaler__copy': True,
#   'scaler__with_mean': True,
#   'model': LogisticRegression(),
#   'model__C': 1.0,
#   ...
# }
```

---

### 🔹 Feature 7: `steps`

```python
# بيرجع list من كل الـ steps
for name, step in pipeline.steps:
    print(f"Step: {name} → {step}")

# Output:
# Step: scaler → StandardScaler()
# Step: model  → LogisticRegression()
```

---

### 🔹 Feature 8: `named_steps`

```python
# وصول لأي step باسمه
my_scaler = pipeline.named_steps['scaler']
my_model  = pipeline.named_steps['model']

# بعد الـ fit تقدر تشوف الـ learned parameters
print("Feature means:", my_scaler.mean_)
print("Model coefficients:", my_model.coef_)
```

---

### 🔹 Feature 9: `make_pipeline()` — طريقة أسرع

```python
from sklearn.pipeline import make_pipeline

# من غير ما تكتب الأسامي بنفسك
pipeline = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

# الـ sklearn بتسمّي كل step تلقائياً بناءً على اسم الـ class
# standardscaler → logisticregression
print(pipeline.named_steps.keys())
# dict_keys(['standardscaler', 'logisticregression'])
```

---

## 📝 مثال كامل — Breast Cancer Model

```python
import pandas as pd
import numpy as np
import joblib

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# ============================================
# 1️⃣  تحميل الداتا
# ============================================
df = pd.read_csv('breast_cancer.csv')

y = df['diagnosis']
X = df.drop(columns=['id', 'Unnamed: 32', 'diagnosis'])

# الـ LabelEncoder لوحده عشان محتاجين inverse_transform بعدين
le = LabelEncoder()
y  = le.fit_transform(y)   # M → 1, B → 0

# ============================================
# 2️⃣  تقسيم الداتا
# ============================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# ============================================
# 3️⃣  بناء الـ Pipeline
# ============================================
pipeline = Pipeline([
    ('scaler',     StandardScaler()),
    ('classifier', LogisticRegression())
])

# ============================================
# 4️⃣  التدريب — سطر واحد بس
# ============================================
pipeline.fit(X_train, y_train)

# ============================================
# 5️⃣  التقييم
# ============================================
y_pred = pipeline.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le.classes_))

# ============================================
# 6️⃣  Threshold Analysis
# ============================================
y_proba = pipeline.predict_proba(X_test)[:, 1]  # بيعمل scale تلقائي ✨

results = []
for thresh in np.arange(0.1, 1.0, 0.05):
    y_t = (y_proba >= thresh).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_test, y_t).ravel()
    results.append({
        'threshold': round(thresh, 2),
        'recall':    tp / (tp + fn),
        'precision': tp / (tp + fp),
        'accuracy':  (tp + tn) / (tp + tn + fp + fn)
    })

print(pd.DataFrame(results))

# ============================================
# 7️⃣  الحفظ — فايلين بس!
# ============================================
joblib.dump(pipeline, 'pipeline.joblib')          # scaler + model في واحد
joblib.dump(le,       'label_encoder.joblib')

# ============================================
# 8️⃣  التحميل والاستخدام على داتا جديدة
# ============================================
pipeline = joblib.load('pipeline.joblib')
le       = joblib.load('label_encoder.joblib')

new_data = pd.DataFrame([[
    17.99, 10.38, 122.8,  1001.0, 0.1184,
    0.2776, 0.3001, 0.1471, 0.2419, 0.0787,
    1.0950, 0.9053,  8.589,  153.4, 0.0064,
    0.0490, 0.0537, 0.0159,  0.030, 0.0062,
    25.38,  17.33,  184.6,  2019.0, 0.1622,
    0.6656, 0.7119, 0.2654,  0.4601, 0.1189
]], columns=X.columns)

# مش محتاج تعمل sc.transform() بنفسك!
prediction  = pipeline.predict(new_data)
probability = pipeline.predict_proba(new_data)

print("Diagnosis  :", le.inverse_transform(prediction))   # ['M'] أو ['B']
print("Probability:", probability)
```

---

## 🗂️ أنواع الـ Pipelines

### 🔸 1. Standard Pipeline

```python
# الأبسط — خطوات بالترتيب
pipeline = Pipeline([
    ('imputer',    SimpleImputer(strategy='mean')),
    ('scaler',     StandardScaler()),
    ('classifier', RandomForestClassifier())
])
```

---

### 🔸 2. ColumnTransformer — لو عندك أعمدة مختلفة

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

numeric_cols     = ['age', 'salary', 'experience']
categorical_cols = ['gender', 'department', 'city']

# preprocessor بيتعامل مع كل نوع عمود بطريقته
preprocessor = ColumnTransformer([
    ('num', StandardScaler(),    numeric_cols),
    ('cat', OneHotEncoder(),     categorical_cols)
])

# Pipeline الكاملة
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model',        LogisticRegression())
])

pipeline.fit(X_train, y_train)
```

---

### 🔸 3. FeatureUnion — دمج features من مصادر مختلفة

```python
from sklearn.pipeline import FeatureUnion

# بتعمل عمليتين مختلفتين على نفس الداتا وبتجمع النتايج
combined_features = FeatureUnion([
    ('pca',  PCA(n_components=5)),
    ('kbest', SelectKBest(k=10))
])

pipeline = Pipeline([
    ('scaler',   StandardScaler()),
    ('features', combined_features),
    ('model',    SVC())
])
```

---

## 🔍 Pipeline مع GridSearchCV

ده من أقوى استخدامات الـ Pipeline — بتعمل Hyperparameter Tuning على كل الخطوات مع بعض:

```python
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model',  LogisticRegression())
])

# الصيغة: اسم_الـstep__اسم_الـparameter
param_grid = {
    'scaler__with_mean':  [True, False],     # parameters الـ scaler
    'model__C':           [0.01, 0.1, 1, 10],# parameters الـ model
    'model__max_iter':    [100, 200, 500]
}

grid_search = GridSearchCV(
    estimator  = pipeline,
    param_grid = param_grid,
    cv         = 5,
    scoring    = 'accuracy',
    n_jobs     = -1
)

grid_search.fit(X_train, y_train)

print("Best params :", grid_search.best_params_)
print("Best score  :", grid_search.best_score_)

# الـ best_estimator_ هو Pipeline كامل بأحسن parameters
best_pipeline = grid_search.best_estimator_
y_pred = best_pipeline.predict(X_test)
```

> 💡 **الميزة الكبيرة:** الـ GridSearchCV بيعمل الـ cross-validation صح — كل fold بيعمل fit للـ scaler على الـ training data بس، ومش بيـ leak الـ test data. لو معملتش Pipeline ده هيبقى غلط!

---

## ⚠️ الأخطاء الشائعة وازاي تتجنبها

### ❌ خطأ 1: بتعمل scale على كل الداتا قبل الـ split

```python
# ❌ غلط — Data Leakage!
X_scaled = StandardScaler().fit_transform(X)        # بيشوف الـ test data!
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)

# ✅ صح — مع Pipeline
pipeline = Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression())])
X_train, X_test, y_train, y_test = train_test_split(X, y)
pipeline.fit(X_train, y_train)  # الـ scaler بيشوف X_train بس ✨
```

---

### ❌ خطأ 2: بتنسى تعمل transform على الداتا الجديدة

```python
# ❌ غلط
new_data_raw    = pd.DataFrame([...])
prediction      = clf.predict(new_data_raw)          # مش متعمل عليها scale!

# ✅ صح — الـ Pipeline بتعملها تلقائي
prediction = pipeline.predict(new_data_raw)          # ✨
```

---

### ❌ خطأ 3: الـ آخر Step مش estimator

```python
# ❌ غلط — الـ Pipeline محتاجة الـ آخر step يبقى estimator (يعمل predict)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca',    PCA())              # ده transformer مش estimator!
])
pipeline.predict(X_test)  # هيطلع Error!

# ✅ صح
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca',    PCA()),
    ('model',  LogisticRegression())   # الـ آخر دايماً model
])
```

---

### ❌ خطأ 4: غلط في كتابة اسم الـ parameter مع GridSearchCV

```python
# ❌ غلط
param_grid = {'C': [0.1, 1, 10]}          # هيدور عن C في الـ Pipeline مش في الـ model

# ✅ صح
param_grid = {'model__C': [0.1, 1, 10]}   # اسم_الـstep__اسم_الـparam
```

---

## 📊 ملخص سريع

| الموضوع | من غير Pipeline | مع Pipeline |
|---------|----------------|-------------|
| **عدد الفايلات المحفوظة** | 3 فايلات منفصلين | فايل واحد |
| **الـ Scaling على داتا جديدة** | لازم تعملها بنفسك | تلقائي ✅ |
| **Data Leakage** | خطر كبير ⚠️ | محمي تلقائي ✅ |
| **GridSearchCV** | معقد وممكن يبقى غلط | سهل وصح ✅ |
| **الكود** | طويل ومعقد | قصير ونظيف ✅ |
| **Production Safety** | خطر تنسى خطوة | آمن 100% ✅ |

---

### 🎯 الخلاصة بجملة واحدة

> **الـ Pipeline = بتلف كل خطوات الـ preprocessing والموديل في حاجة واحدة، عشان الكود ينظف وآمن ومش هتنسى خطوة تاني.**

---

*Made with ❤️ — Scikit-Learn Pipeline Guide*
