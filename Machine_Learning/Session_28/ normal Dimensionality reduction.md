# 🤖 Machine Learning — Session 6
## دليلك الشامل لـ Dimensionality Reduction (تقليل الأبعاد)

> 📌 **ملاحظة:** الشرح ده مصمم يكون سلس ومفيد، فيه نظرية + رياضيات + كود + مقارنات + أسئلة انترفيو 🎯

---

## 📚 فهرس المحتوى

1. [The Curse of Dimensionality](#1--the-curse-of-dimensionality)
2. [إزاي Dimensionality Reduction بيساعد؟](#2--إزاي-dimensionality-reduction-بيساعد)
3. [Feature Selection](#3--feature-selection)
4. [Feature Extraction (Dimension Reduction)](#4--feature-extraction-dimension-reduction)
5. [PCA — Principal Component Analysis](#5--pca--principal-component-analysis)
6. [t-SNE](#6--t-sne)
7. [ملاحظات مهمة جداً (Notes)](#7--ملاحظات-مهمة-جداً)
8. [Implementation بالكود](#8--implementation-بالكود)
9. [أسئلة الانترفيو](#9--أسئلة-انترفيو-مهمة)

---

## 1. 😱 The Curse of Dimensionality

### التعريف

**Curse of Dimensionality** هي مجموعة من المشاكل اللي بتحصل لما بتشتغل مع داتا فيها عدد كبير من الـ features — كلما زاد عدد الأبعاد، كلما الأمور بدأت تتعقد بشكل مش خطي!

> 💡 "كلما زادت الـ Features، بزيادة الأبعاد، كلما احتجت داتا أكبر بكتير عشان تغطي الـ feature space وتتعلم صح."

### المشاكل الناتجة عن High Dimensionality

#### 1. زيادة الحسابات (Increased Computational Requirements)
```
مع كل feature جديدة بتضيفها:
  الحسابات بتزيد بشكل Exponential مش Linear!

مثال:
  10 features  → حسابات معقولة ✅
  100 features → حسابات كتير جداً 😓
  1000 features → ممكن يستغرق ساعات أو أيام 😱
```

#### 2. تفرق البيانات (Sparsity of Data)
```
في الـ Low Dimensions:               في الـ High Dimensions:
─────────────────────                ──────────────────────
● ● ●                                ●         ●
● ● ●   ← نقاط قريبة                 
● ● ●                                    ●           ●
                                     ← نقاط متباعدة جداً
النقاط قريبة من بعض               الداتا بتتفرق والمسافات
→ خوارزميات زي KNN بتشتغل كويس    بين النقاط بتكبر
                                   → KNN بتفشل
```

#### 3. Overfitting
```
High Dimensions → الموديل بيحفظ الـ Noise بدل ما يتعلم النمط

Training Accuracy:  98%  ✅ (عالية جداً)
Testing Accuracy:   55%  ❌ (منخفضة جداً)
→ Overfitting كبير
```

#### 4. Features مكررة وغير مفيدة (Redundant & Irrelevant Features)
```
Redundant Features:    Height_cm و Height_m → نفس المعلومة مرتين!
Irrelevant Features:   رقم الـ ID في مشكلة تنبؤ المرض → مفيش معنى

الأثر:
  → الموديل بيتشتت ويدي نتايج أسوأ
  → وقت التدريب بيطول من غير فايدة
```

#### 5. صعوبة التصور (Difficult Visualization)
```
1D → خط         ✅ سهل
2D → مستوي       ✅ سهل
3D → فضاء ثلاثي  ✅ صعب شوية لكن ممكن
4D+ → مستحيل!    ❌ الدماغ البشري مش قادر يتخيل
```

#### 6. مشاكل المسافات (Distance Issues)
```
في الـ High Dimensions، المسافات بين كل النقاط بتتقارب من بعض!

مثال:
  في 2D:  قريب = 1 unit، بعيد = 10 units  → فرق كبير ✅
  في 1000D: قريب ≈ 31.6 units، بعيد ≈ 31.7 units → فرق ضئيل جداً! ❌

الأثر على KNN و SVM:
  مش قادرين يفرقوا بين "الجار القريب" و"الجار البعيد"
```

#### 7. مشاكل التخزين (Storage Concerns)
```
feature واحدة إضافية × ملايين الصفوف = جيجابايتات إضافية!
→ مش كل الأنظمة عندها الـ RAM الكافية
```

### ملخص المشاكل السبعة

| # | المشكلة | التأثير |
|---|---------|---------|
| 1 | Increased Computation | وقت أطول + موارد أكبر |
| 2 | Sparsity of Data | KNN و distance-based algorithms بتفشل |
| 3 | Overfitting | الموديل بيحفظ مش بيتعلم |
| 4 | Redundant Features | تشتيت الموديل |
| 5 | Visualization Issues | مش ممكن تشوف الداتا |
| 6 | Distance Convergence | المسافات بتتقارب |
| 7 | Storage Issues | ذاكرة أكبر |

---

> ### 🎤 سؤال انترفيو #1
> **"إيه هي Curse of Dimensionality وإزاي بتأثر على خوارزميات الـ ML؟"**
>
> **الإجابة:** هي مجموعة من المشاكل اللي بتحصل لما عدد الـ features بيزيد بشكل كبير. أهم تأثيراتها: (1) الداتا بتتفرق (Sparsity) فبتبقى محتاج داتا أضخم عشان تغطي الـ feature space. (2) خوارزميات المسافة زي KNN بتفشل لأن المسافات بين النقاط بتتقارب. (3) الموديلات بتـ Overfit لأن عدد الـ features أكبر من اللازم. الحل الأساسي هو Dimensionality Reduction.

---

## 2. 💊 إزاي Dimensionality Reduction بيساعد؟

**Dimensionality Reduction** بتقلل عدد الـ features مع الاحتفاظ بأكبر قدر ممكن من المعلومات المهمة.

```
الفوائد:
  ✅ تبسيط الموديلات وتسريعها
  ✅ تحسين الـ Generalization وتقليل الـ Overfitting
  ✅ تقليل متطلبات التخزين
  ✅ تمكين الـ Visualization
  ✅ تحسين دقة الخوارزميات المعتمدة على المسافات
```

### نوعين رئيسيين

```
Dimensionality Reduction
         │
         ├── 1. Feature Selection
         │       → نختار features موجودة ونرمي الباقي
         │       → الـ features الناتجة هي نفس الأصلية
         │
         └── 2. Feature Extraction
                 → نحوّل الـ features لحاجة جديدة وأقل
                 → الـ features الناتجة مختلفة عن الأصلية
                 → مثال: PCA
```

---

## 3. 🔍 Feature Selection

### التعريف

**Feature Selection** هي اختيار أهم الـ features من الأصلية وحذف الباقي — من **غير** ما نحوّل أي حاجة. النتيجة subset من الـ features الأصلية.

> 💡 **الفرق الجوهري:** في Feature Selection، الـ features الناتجة هي **نفس** الـ features الأصلية. في Feature Extraction، الـ features الناتجة **مختلفة** (محوّلة).

### الأنواع الثلاثة

```
Feature Selection
      │
      ├── 1. Filter Methods    → إحصاء بحت، مش محتاج موديل
      ├── 2. Wrapper Methods   → بيجرب combinations مختلفة
      └── 3. Embedded Methods  → الاختيار جوه التدريب نفسه
```

---

### 3.1 Filter Methods 🔵

#### التعريف
بتختار الـ features بناءً على علاقتها الإحصائية بالـ target **من غير** ما تستخدم أي موديل ML. هي **preprocessing step** خالص.

```
Filter Methods = إحصاء فقط، بدون training
```

#### التقنيات الشائعة

| التقنية | الاستخدام | نوع البيانات |
|---------|-----------|-------------|
| **Pearson's Correlation** | العلاقة الخطية بين متغيرين مستمرين | Continuous |
| **Chi-Square Test (χ²)** | الاستقلالية بين متغيرين فئويين | Categorical |
| **ANOVA** | الفرق في المتوسطات بين مجموعات | Mixed |
| **Spearman's Correlation** | العلاقة الرتبية (غير خطية) | Ordinal |
| **Kendall's Correlation** | العلاقة الرتبية (أكثر دقة) | Ordinal |

---

#### 📐 Pearson's Correlation

**التعريف:** بتقيس قوة واتجاه العلاقة **الخطية** بين متغيرين مستمرين.

**الصيغة الرياضية:**
```
         Σ (Xᵢ - X̄)(Yᵢ - Ȳ)
r = ─────────────────────────────────
     √[Σ(Xᵢ - X̄)²] × √[Σ(Yᵢ - Ȳ)²]

حيث:
  X̄ = متوسط X
  Ȳ = متوسط Y
```

**تفسير القيم:**
```
r = +1   →  علاقة طردية كاملة  (↑X → ↑Y)
r = 0    →  لا علاقة خطية
r = -1   →  علاقة عكسية كاملة  (↑X → ↓Y)

القاعدة العملية:
  |r| > 0.5  → علاقة قوية مع الـ Target → احتفظ بالـ feature ✅
  |r| < 0.5  → علاقة ضعيفة → ممكن تحذفها ❌
```

**مثال:**
```
feature: الوزن       target: ضغط الدم
r = 0.78 → علاقة قوية → احتفظ بالـ feature ✅

feature: اسم الشارع  target: ضغط الدم
r = 0.02 → علاقة ضعيفة جداً → احذف الـ feature ❌
```

---

#### 📊 Chi-Square Test (χ²)

**التعريف:** بيتحقق إذا كان متغيرين **فئويين (Categorical)** مستقلين عن بعض أم لا.

**الصيغة الرياضية:**
```
       Σ (Oᵢ - Eᵢ)²
χ² =  ─────────────
            Eᵢ

حيث:
  Oᵢ = القيمة الملاحظة (Observed)
  Eᵢ = القيمة المتوقعة (Expected) لو الاستقلالية صح
```

**الخطوات:**
```
1️⃣  تحديد الفرضيات:
    H₀: المتغيرين مستقلين (لا علاقة)
    H₁: المتغيرين مرتبطين (في علاقة)

2️⃣  بناء Contingency Table:
    جدول بيحسب تكرارات كل combination

3️⃣  حساب Expected Values:
    E = (Row Total × Column Total) / Grand Total

4️⃣  حساب χ²

5️⃣  المقارنة بـ Critical Value:
    χ² > Critical Value → ارفض H₀ → في علاقة → احتفظ بالـ feature
    χ² < Critical Value → اقبل H₀  → مفيش علاقة → احذف الـ feature
```

**مثال بسيط:**
```
هل الـ Gender مرتبط بشراء منتج معين؟

         Buy    Not Buy   Total
Male      45      55       100
Female    30      70       100
Total     75     125       200

E(Male, Buy) = (100 × 75) / 200 = 37.5

χ² = (45-37.5)²/37.5 + ... = محسوب

لو χ² > Critical Value → Gender مرتبط بالشراء → احتفظ بيه ✅
```

> ⚠️ **تحذير مهم:** Chi-Square **لا تشتغل مع القيم السالبة!** لازم تعمل transformation للداتا الأول.

---

### 3.2 Wrapper Methods 🟡

#### التعريف
بيعامل الـ Feature Selection كـ **search problem** — بيجرب combinations مختلفة من الـ features ويقيّمها بناءً على أداء موديل ML معين.

```
الفكرة:
  لازم تدرّب موديل على كل combination!
  → أبطأ من Filter ❌
  → لكن نتايج أدق ✅
```

#### التقنيات الشائعة

**1. Recursive Feature Elimination (RFE)**
```
1. درّب الموديل على كل الـ features
2. احسب أهمية كل feature
3. احذف الـ feature الأقل أهمية
4. أعد التدريب على الـ features المتبقية
5. كرر لحد ما توصل للعدد المطلوب من الـ features
```

**2. Forward Selection**
```
1. ابدأ من غير features
2. أضف feature واحدة كل مرة (الأكثر تحسيناً للأداء)
3. كرر لحد ما الأداء مش بيتحسن أكتر
```

**3. Backward Elimination**
```
1. ابدأ بكل الـ features
2. احذف feature واحدة كل مرة (الأقل تأثيراً على الأداء)
3. كرر لحد ما الأداء يبدأ ينزل
```

---

### 3.3 Embedded Methods 🟢

#### التعريف
**الاختيار بيحصل جوه عملية التدريب نفسها** — الموديل بيقرر تلقائياً أي الـ features مهمة وأيها مش مهمة.

```
المميزات:
  ✅ أكفأ من Wrapper (مش محتاج runs متعددة)
  ✅ أكثر دقة من Filter (بيستخدم الموديل)
  ✅ الأفضل في الممارسة العملية
```

#### التقنيات الشائعة

**1. Lasso Regression (L1 Regularization)**
```
بيضيف عقوبة = λ × Σ|weights|

الأثر:
  الـ weights بتاعة الـ features الأقل أهمية بتتحول لـ ZERO تماماً
  → الـ features دي بتتحذف أوتوماتيك!

مثال:
  feature 1: weight = 0.85  → مهمة ✅
  feature 2: weight = 0.00  → اتحذفت تلقائياً ❌
  feature 3: weight = 0.62  → مهمة ✅
```

**2. Ridge Regression (L2 Regularization)**
```
بيضيف عقوبة = λ × Σ(weights²)

الأثر:
  بيقلل الـ weights بس مش بيوصلها لـ ZERO
  → بيقلل تأثير الـ features الأقل أهمية بدل ما يحذفها
```

**3. Random Forest Feature Importance**
```
Random Forest بيحسب أهمية كل feature بناءً على:
  كام مرة الـ feature دي بتقلل الـ Impurity (Gini Index) في الـ Trees

الأعلى أهمية → الأكثر تأثيراً على الـ predictions
```

### مقارنة الطرق الثلاثة

| المعيار | Filter | Wrapper | Embedded |
|---------|:------:|:-------:|:--------:|
| سرعة التنفيذ | 🟢 سريع جداً | 🔴 بطيء | 🟡 متوسط |
| دقة النتيجة | 🟡 متوسطة | 🟢 عالية | 🟢 عالية |
| بيستخدم موديل ML | ❌ لا | ✅ نعم | ✅ نعم (داخلياً) |
| مخاطر الـ Overfitting | 🟢 منخفضة | 🔴 عالية | 🟡 متوسطة |
| الاستخدام العملي | Baseline سريع | بيانات صغيرة | الأفضل عموماً |

---

> ### 🎤 سؤال انترفيو #2
> **"إيه الفرق بين Filter و Wrapper و Embedded Methods في الـ Feature Selection؟"**
>
> **الإجابة:**
> - **Filter:** بيستخدم إحصاء بحت (Correlation, Chi-Square) من غير موديل — سريع بس أقل دقة.
> - **Wrapper:** بيجرب combinations مختلفة من الـ features ويقيّمها بموديل ML — أدق بس أبطأ وأغلى حسابياً.
> - **Embedded:** الاختيار بيحصل جوه التدريب نفسه (Lasso, Random Forest) — توازن ممتاز بين السرعة والدقة.
>
> **القاعدة:** في الواقع العملي، ابدأ بـ Filter كـ quick scan، وبعدين استخدم Embedded للنتيجة النهائية.

---

## 4. 🔄 Feature Extraction (Dimension Reduction)

### التعريف

**Feature Extraction** بتحوّل الـ features الأصلية لـ features جديدة أقل عدداً وأكثر تعبيراً — الـ features الجديدة **مختلفة** عن الأصلية ومش ممكن نفسّرها مباشرة.

```
Feature Selection:    X1, X2, X3, X4 → X1, X3      (نفس الـ features)
Feature Extraction:   X1, X2, X3, X4 → PC1, PC2    (features جديدة)
```

### الأنواع

#### Linear Methods (Factor-based)
```
PCA (Principal Component Analysis)
  → أشهر خوارزمية linear dimensionality reduction
  → بتدور على directions ذات أعلى variance
  
Factor Analysis (FA)
  → مشابه لـ PCA لكن بيركز على الـ latent factors
  
Independent Component Analysis (ICA)
  → بيدور على components مستقلة إحصائياً
  → مفيد جداً في معالجة الإشارات (Signal Processing)
```

#### Non-Linear Methods (Manifold Learning)
```
t-SNE
  → للـ Visualization بس (مش للـ Training)
  → ممتاز في إظهار الـ clusters في 2D/3D
  
UMAP
  → أسرع وأحسن من t-SNE
  → محافظ على الـ Global Structure أحسن
  
Kernel PCA
  → PCA لكن بيتعامل مع العلاقات غير الخطية
  
MDS (Multidimensional Scaling)
  → بيحافظ على المسافات بين النقاط
```

---

## 5. 🏆 PCA — Principal Component Analysis

### التعريف

**PCA** هي أشهر وأكثر خوارزمية Dimensionality Reduction استخداماً. بتحوّل الـ features لمحاور جديدة **متعامدة (orthogonal)** تسمى **Principal Components** — كل محور بيمثل اتجاه ذو variance عالية.

> 💡 "PCA بتدور على الاتجاهات في البيانات اللي فيها أكبر تشتت (spread) — لأن الاتجاهات دي بتحمل أكبر قدر من المعلومات."

### مفاهيم أساسية لازم تفهمها الأول

#### Variance و Standard Deviation

```
Standard Deviation (σ):
  → بيقيس متوسط بُعد النقاط عن المتوسط
  σ = √[ Σ(Xᵢ - X̄)² / N ]

Variance (σ²):
  → مربع الـ Standard Deviation
  σ² = Σ(Xᵢ - X̄)² / N

الـ Variance أكثر حساسية للـ Outliers بسبب التربيع.
```

**ليه Variance مهمة في PCA؟**
```
PCA بتدور على الاتجاهات ذات أعلى Variance لأن:
  Variance عالية = الداتا متشتتة في الاتجاه ده = معلومات أكتر
  Variance منخفضة = الداتا متقاربة = معلومات أقل (ممكن تكون noise)
```

#### Linear Transformation

```
Linear Transformation = تحويل هندسي للبيانات يحافظ على:
  ✅ الخطوط المستقيمة تفضل مستقيمة
  ✅ نسب المسافات
  ✅ نقطة الأصل

أمثلة:
  → Rotation   (تدوير)
  → Scaling    (تمديد/تقليص)
  → Reflection (انعكاس)
  → Shearing   (قص)

PCA بتستخدم Linear Transformation عشان تحول الداتا لـ feature space جديدة.
```

#### Eigenvalues و Eigenvectors

```
معادلة الـ Eigenvector:
  A × v = λ × v

حيث:
  A = المصفوفة (في PCA = Covariance Matrix)
  v = الـ Eigenvector (الاتجاه)
  λ = الـ Eigenvalue (مقدار الـ Variance في الاتجاه ده)

المعنى:
  الـ Eigenvector = اتجاه Principal Component
  الـ Eigenvalue  = كمية الـ Variance في الاتجاه ده
                  = مدى أهمية هذا الـ Component

مثال:
  A = [[3, 1], [1, 3]]
  Eigenvector 1: v₁ = [1, 1],  λ₁ = 4   ← أهم component (أعلى variance)
  Eigenvector 2: v₂ = [1, -1], λ₂ = 2   ← تاني component
```

### شروط تطبيق PCA قبل البدء

```
1️⃣  Feature Scaling ضروري:
    لو features بـ scales مختلفة، الـ feature ذات القيم الكبيرة
    هتسيطر على الـ Variance وتشوّه النتيجة.
    الحل: StandardScaler() قبل PCA.

2️⃣  Numerical Data فقط:
    PCA مش بتشتغل مع الـ Categorical Data.
    الحل: حوّل الـ Categorical features أولاً (Encoding).
```

### خطوات PCA بالتفصيل

#### الخطوة 1: Standardize the Data
```
هدف: كل feature يبقى عنده Mean = 0 و Std = 1

X_standardized = (X - mean) / std

قبل:  [5000, 1.7, 25]   ← scales مختلفة تماماً
بعد:  [0.8, -0.3, 1.2]  ← كل الـ features على نفس الـ scale ✅
```

#### الخطوة 2: Calculate Covariance Matrix (Σ)
```
الـ Covariance Matrix بتوضح العلاقة بين كل feature وكل feature تانية.

Cov(X, Y) = Σ(Xᵢ - X̄)(Yᵢ - Ȳ) / (n-1)

مثال مع 3 features (f1, f2, f3):
      f1     f2     f3
f1 [ 1.00   0.85  -0.20 ]   ← f1 و f2 مترابطين قوي (0.85)
f2 [ 0.85   1.00   0.10 ]
f3 [-0.20   0.10   1.00 ]

القيم على الـ diagonal = variance كل feature مع نفسها = 1 (بعد الـ Standardization)
```

#### الخطوة 3: Calculate Eigenvectors & Eigenvalues
```
من الـ Covariance Matrix، بنطلع:
  Eigenvectors → اتجاهات الـ Principal Components
  Eigenvalues  → أهمية كل component (= variance في اتجاهه)

بنرتبهم من أكبر Eigenvalue لأصغر:
  PC1: λ₁ = 2.8   ← الأهم (أعلى variance)
  PC2: λ₂ = 0.9   ← تاني
  PC3: λ₃ = 0.3   ← الأقل أهمية
```

#### الخطوة 4: Select Top K Eigenvectors
```
إزاي تختار K؟ (راجع قسم 5.4 لأساليب الاختيار)

Explained Variance Ratio = λᵢ / Σλ
  PC1: 2.8 / 4.0 = 70%  ← بيشرح 70% من التباين
  PC2: 0.9 / 4.0 = 22.5%
  PC3: 0.3 / 4.0 = 7.5%

Cumulative:
  K=1: 70%
  K=2: 92.5% ← لو عاوز 95% مش كافي
  K=3: 100%

لو عاوز 95%: خد K=3
لو عاوز تصور (Visualization): خد K=2
```

#### الخطوة 5: Project Data onto New Space
```
X_new = X_standardized × W

حيث W = مصفوفة الـ K Eigenvectors المختارين (n_features × K)

النتيجة:
  قبل: 150 صف × 4 features
  بعد: 150 صف × 2 components
  → نفس عدد الصفوف، لكن features أقل ✅
```

### إزاي تختار K (عدد الـ Components)?

#### الطريقة 1: Explained Variance (95% Rule)
```
اختار أقل K بيشرح ≥ 95% من الـ Variance.

Cumulative Explained Variance:
  K=1:  70%
  K=2:  92%
  K=3:  97% ← أول K بيتعدى 95% → اختار K=3
  K=4: 100%
```

#### الطريقة 2: Visualization (K=2 أو K=3)
```
لو هدفك رسم الداتا:
  K = 2  → scatter plot (2D)
  K = 3  → 3D plot
```

#### الطريقة 3: Elbow Method
```
ارسم الـ Explained Variance لكل K:

Variance
  ↑
  |●
  | ●
  |  ●
  |   ●
  |    ●──────── ← Elbow هنا!
  |         ●●●●
  +──────────────→ K

اختار K عند نقطة "الكوع" — بعديها الـ Variance مش بتتحسن كتير.
```

### تفسير الـ Principal Components

```
⚠️ ملاحظة مهمة:
الـ Principal Components مش ليها تفسير مباشر زي الـ features الأصلية!

مثال:
  الأصلي:  [Height, Weight, Age, Income]
  بعد PCA: [PC1, PC2]

PC1 ممكن يكون = 0.6×Height + 0.5×Weight + 0.3×Age + 0.2×Income
→ مزيج من كل الـ features الأصلية

الـ PCA بنستخدمها للأداء مش للتفسير!
```

---

> ### 🎤 سؤال انترفيو #3
> **"إيه هي الـ Principal Components وإيه علاقتها بالـ Eigenvectors؟"**
>
> **الإجابة:** الـ Principal Components هي محاور جديدة في الـ feature space بيتم اشتقاقها من الداتا الأصلية. كل Principal Component هو Eigenvector للـ Covariance Matrix، والـ Eigenvalue المقابل بيمثل كمية الـ Variance في اتجاه الـ Component ده. الـ Component الأول (PC1) بيكون في اتجاه أعلى Variance، والثاني (PC2) في اتجاه ثاني أعلى Variance وعمودي على الأول، وهكذا. نختار أول K components اللي بتشرح معظم الـ Variance (مثلاً 95%).

---

> ### 🎤 سؤال انترفيو #4
> **"ليه Standardization ضرورية قبل PCA؟"**
>
> **الإجابة:** لأن PCA بتعتمد على الـ Variance، ولو features بـ scales مختلفة (مثلاً الراتب: 5000-50000 والعمر: 20-60)، الـ feature ذات القيم الكبيرة هيكون عندها Variance أعلى بكتير — مش لأنها أهم، لكن لأن أرقامها أكبر. الـ PCA هتعتقد إنها أهم وتركز عليها. الـ Standardization بيخلي كل feature عندها Mean=0 و Std=1، فالمقارنة بين الـ Variances تبقى عادلة.

---

## 6. 📊 t-SNE

### التعريف

**t-SNE (t-Distributed Stochastic Neighbor Embedding)** هي خوارزمية Non-Linear لتقليل الأبعاد — بس هي **للـ Visualization فقط** مش للـ Training.

```
PCA vs t-SNE:
  PCA:   Linear  | للـ Training والـ Visualization
  t-SNE: Non-Linear | للـ Visualization فقط
```

### إزاي t-SNE بتشتغل؟

```
1. في الـ High-Dimensional Space:
   بتحسب احتمالية إن كل نقطتين "جيران"
   بناءً على المسافة بينهم

2. في الـ Low-Dimensional Space:
   Attraction:  النقاط القريبة في الـ High-D تتقرب في الـ Low-D
   Repulsion:   النقاط البعيدة في الـ High-D تتباعد في الـ Low-D

3. النتيجة:
   تشكيل clusters واضحة تعكس التجمعات في الداتا الأصلية
```

### متى تستخدم t-SNE؟

```
✅ استخدم t-SNE لو:
  → عاوز تشوف الـ clusters في الداتا بصرياً
  → عاوز تتأكد إن الـ Clustering بتاعك منطقي
  → Exploratory Data Analysis (EDA)

❌ متستخدمش t-SNE لو:
  → عاوز تدرب موديل عليها
  → عاوز تحتفظ بالـ Global Structure
  → الداتا كبيرة جداً (بطيئة مع Datasets كبيرة)
```

---

## 7. ⚠️ ملاحظات مهمة جداً

### الترتيب الصحيح لعمليات الـ Preprocessing

```
الترتيب الصح:

1. Feature Selection / Engineering
        ↓
2. Encoding (Categorical → Numerical)
        ↓
3. Train-Test Split
        ↓
4. Feature Scaling (StandardScaler)
        ↓
5. PCA (لو هتستخدمها)
        ↓
6. تدريب الموديل
```

> ⚠️ **لماذا Feature Selection قبل Encoding؟**
> لو عندك features نصية (text)، بعد الـ Encoding هتبقى numerical فبتقدر تطبق filter methods زي Pearson. لكن على الـ original categorical features، استخدم Chi-Square **قبل** الـ Encoding.

### Chi-Square والقيم السالبة

```
❌ Chi-Square مش بتشتغل مع القيم السالبة!

لو عندك feature بقيم سالبة وعاوز تطبق Chi-Square:
  1. استخدم MinMaxScaler بدل StandardScaler (بيعمل shift للقيم لـ [0,1])
  2. أو أضف constant عشان كل القيم تبقى موجبة
  3. أو استخدم Pearson بدلاً منها (لو الداتا continuous)
```

### PCA بعد الـ Scaling

```
الترتيب الإلزامي مع PCA:
  1. Feature Selection
  2. Train-Test Split
  3. StandardScaler → fit على Train فقط!
  4. PCA → fit على Train فقط!

⚠️ لو عملت fit_transform على كل الداتا قبل التقسيم
   → Data Leakage → نتائج متحيزة وغير حقيقية!
```

### Data Leakage في الـ Scaling والـ PCA

```python
# ❌ غلط — Data Leakage!
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # شايف الـ test data!
X_train, X_test = train_test_split(X_scaled)

# ✅ صح
X_train, X_test = train_test_split(X)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit هنا بس
X_test_scaled  = scaler.transform(X_test)        # transform بس
```

---

> ### 🎤 سؤال انترفيو #5
> **"إيه الفرق بين Feature Selection و Feature Extraction؟"**
>
> **الإجابة:** الفرق الجوهري في الـ features الناتجة: Feature Selection بتختار subset من الـ features الأصلية من غير ما تغيّر فيها — النتيجة هي features بتقدر تفسرها مباشرة (مثلاً: "Height", "Age"). Feature Extraction بتحوّل الـ features لـ features جديدة مختلفة تماماً عن الأصلية — النتيجة features مش ليها تفسير مباشر (مثلاً: "PC1", "PC2"). PCA هي أشهر مثال على الـ Feature Extraction.

---

> ### 🎤 سؤال انترفيو #6
> **"إيه هو الـ Explained Variance في PCA وإزاي بنستخدمه؟"**
>
> **الإجابة:** الـ Explained Variance لكل Principal Component هو نسبة الـ Variance اللي بيشرحها من إجمالي الـ Variance في الداتا. بنحسبه بقسمة الـ Eigenvalue على مجموع كل الـ Eigenvalues. بنستخدمه لتحديد K الأمثل — الـ Rule of Thumb هو اختيار أقل عدد من الـ Components يشرح ≥ 95% من الـ Variance. برسم الـ Cumulative Explained Variance Curve ونشوف عند أي K بتتعدى 95%.

---

## 8. 💻 Implementation بالكود

### Dataset المشكلة: Iris Dataset 🌸

```
Features: 4 (sepal length, sepal width, petal length, petal width)
Samples: 150
Target: 3 أنواع زهور (مش هنستخدمه في PCA)
```

---

### الخطوة 1: Import المكتبات

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import (
    SelectKBest,
    f_classif,           # ANOVA F-test
    chi2,                # Chi-Square
    RFE
)
from sklearn.linear_model import Lasso, LassoCV, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

---

### الخطوة 2: تحميل ومعاينة الداتا

```python
# تحميل الداتا
iris = load_iris()
X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y

print("شكل الداتا:", df.shape)
print("\nأول 5 صفوف:")
print(df.head())

print("\nإحصائيات عامة:")
print(df.describe().round(2))
```

**Output متوقع:**
```
شكل الداتا: (150, 5)

إحصائيات عامة:
       sepal length  sepal width  petal length  petal width
count        150.00       150.00        150.00       150.00
mean           5.84         3.06          3.76         1.20
std            0.83         0.44          1.77         0.76
```

---

### الخطوة 3: تقسيم الداتا والـ Scaling

```python
# تقسيم الداتا
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Standardization — ضروري قبل PCA وبعد الـ Feature Selection
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit هنا بس
X_test_scaled  = scaler.transform(X_test)        # transform بس

print(f"Training set: {X_train.shape[0]} samples")
print(f"Test set:     {X_test.shape[0]} samples")
print(f"\nبعد الـ Scaling:")
print(f"  Mean (train): {X_train_scaled.mean(axis=0).round(3)}")
print(f"  Std  (train): {X_train_scaled.std(axis=0).round(3)}")
```

---

### الخطوة 4: Feature Selection — Filter Method (Pearson Correlation)

```python
# رسم Correlation Heatmap
plt.figure(figsize=(8, 6))
corr_matrix = df.drop('target', axis=1).corr()
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    square=True
)
plt.title('Pearson Correlation Heatmap', fontsize=14)
plt.tight_layout()
plt.show()

# Correlation مع الـ target
print("Correlation مع الـ Target:")
for col in iris.feature_names:
    corr = df[col].corr(df['target'])
    status = "✅ احتفظ" if abs(corr) > 0.3 else "❌ ممكن تحذف"
    print(f"  {col:<25}: {corr:+.3f}  {status}")
```

**Output متوقع:**
```
Correlation مع الـ Target:
  sepal length (cm)        : +0.782  ✅ احتفظ
  sepal width (cm)         : -0.420  ✅ احتفظ
  petal length (cm)        : +0.949  ✅ احتفظ
  petal width (cm)         : +0.957  ✅ احتفظ
```

---

### الخطوة 5: Feature Selection — Filter Method (ANOVA F-test)

```python
# ANOVA F-test مع SelectKBest
selector_anova = SelectKBest(score_func=f_classif, k=3)
selector_anova.fit(X_train_scaled, y_train)

# نتائج
feature_scores = pd.DataFrame({
    'Feature': iris.feature_names,
    'F-Score': selector_anova.scores_,
    'P-Value': selector_anova.pvalues_
}).sort_values('F-Score', ascending=False)

print("ANOVA F-test Results:")
print(feature_scores.to_string(index=False))

# أهم 3 features
selected_features = [iris.feature_names[i]
                     for i in selector_anova.get_support(indices=True)]
print(f"\nأهم 3 Features: {selected_features}")

# تطبيق الاختيار
X_train_anova = selector_anova.transform(X_train_scaled)
X_test_anova  = selector_anova.transform(X_test_scaled)
print(f"Shape بعد الاختيار: {X_train_anova.shape}")
```

---

### الخطوة 6: Feature Selection — Wrapper Method (RFE)

```python
from sklearn.feature_selection import RFE

# RFE مع Logistic Regression
estimator = LogisticRegression(max_iter=200, random_state=42)
rfe = RFE(estimator=estimator, n_features_to_select=2)
rfe.fit(X_train_scaled, y_train)

print("RFE Feature Ranking:")
for i, (feature, rank, selected) in enumerate(zip(
    iris.feature_names, rfe.ranking_, rfe.support_
)):
    status = "✅ Selected" if selected else f"❌ Rank {rank}"
    print(f"  {feature:<25}: {status}")

# تطبيق الاختيار
X_train_rfe = rfe.transform(X_train_scaled)
X_test_rfe  = rfe.transform(X_test_scaled)
```

---

### الخطوة 7: Feature Selection — Embedded Method (Random Forest)

```python
# Random Forest Feature Importance
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_scaled, y_train)

# رسم Feature Importance
importance_df = pd.DataFrame({
    'Feature': iris.feature_names,
    'Importance': rf.feature_importances_
}).sort_values('Importance', ascending=True)

plt.figure(figsize=(8, 4))
plt.barh(importance_df['Feature'], importance_df['Importance'],
         color=['#e74c3c' if x > 0.1 else '#95a5a6'
                for x in importance_df['Importance']])
plt.xlabel('Feature Importance')
plt.title('Random Forest Feature Importance', fontsize=13)
plt.axvline(x=0.1, color='red', linestyle='--',
            alpha=0.7, label='Threshold = 0.1')
plt.legend()
plt.tight_layout()
plt.show()

print("\nFeature Importance:")
for _, row in importance_df.sort_values('Importance', ascending=False).iterrows():
    bar = '█' * int(row['Importance'] * 30)
    print(f"  {row['Feature']:<25}: {row['Importance']:.3f}  {bar}")
```

---

### الخطوة 8: PCA — تطبيق كامل

```python
# تطبيق PCA
pca_full = PCA()   # بدون تحديد n_components عشان نشوف كل الـ Variance
pca_full.fit(X_train_scaled)

# Explained Variance
explained_var = pca_full.explained_variance_ratio_
cumulative_var = np.cumsum(explained_var)

print("Explained Variance per Component:")
for i, (ev, cv) in enumerate(zip(explained_var, cumulative_var)):
    bar = '█' * int(ev * 40)
    print(f"  PC{i+1}: {ev:.3f} ({ev*100:.1f}%)  Cumulative: {cv*100:.1f}%  {bar}")

# رسم Explained Variance
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Individual Variance
axes[0].bar(range(1, len(explained_var)+1), explained_var,
            color=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'],
            edgecolor='white', linewidth=0.5)
axes[0].set_title('Explained Variance per Component', fontsize=13)
axes[0].set_xlabel('Principal Component')
axes[0].set_ylabel('Explained Variance Ratio')
axes[0].set_xticks(range(1, len(explained_var)+1))

# Cumulative Variance (Elbow Method)
axes[1].plot(range(1, len(cumulative_var)+1), cumulative_var*100,
             'bo-', linewidth=2, markersize=8)
axes[1].axhline(y=95, color='red', linestyle='--', label='95% threshold')
axes[1].fill_between(range(1, len(cumulative_var)+1), cumulative_var*100,
                     alpha=0.2, color='blue')
axes[1].set_title('Cumulative Explained Variance (Elbow Method)', fontsize=13)
axes[1].set_xlabel('Number of Components (K)')
axes[1].set_ylabel('Cumulative Explained Variance (%)')
axes[1].set_xticks(range(1, len(cumulative_var)+1))
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# تحديد K الأمثل
k_95 = np.argmax(cumulative_var >= 0.95) + 1
print(f"\n✅ K عشان تشرح 95% من الـ Variance = {k_95}")
```

**Output متوقع:**
```
Explained Variance per Component:
  PC1: 0.725 (72.5%)  Cumulative: 72.5%  ████████████████████████████
  PC2: 0.230 (23.0%)  Cumulative: 95.5%  █████████
  PC3: 0.037  (3.7%)  Cumulative: 99.2%  █
  PC4: 0.008  (0.8%)  Cumulative: 100%

✅ K عشان تشرح 95% من الـ Variance = 2
```

---

### الخطوة 9: PCA — التطبيق بـ K المختار

```python
# PCA بـ K=2 (للـ Visualization)
pca_2d = PCA(n_components=2)
X_train_pca = pca_2d.fit_transform(X_train_scaled)  # fit هنا بس
X_test_pca  = pca_2d.transform(X_test_scaled)        # transform بس

print(f"Shape قبل PCA: {X_train_scaled.shape}")
print(f"Shape بعد PCA: {X_train_pca.shape}")
print(f"Variance محفوظة: {pca_2d.explained_variance_ratio_.sum()*100:.1f}%")

# Visualization
plt.figure(figsize=(10, 7))
colors = ['#e74c3c', '#3498db', '#2ecc71']
markers = ['o', 's', '^']

for i, (color, marker, name) in enumerate(zip(
    colors, markers, iris.target_names
)):
    mask = y_train == i
    plt.scatter(
        X_train_pca[mask, 0], X_train_pca[mask, 1],
        c=color, marker=marker, s=80, alpha=0.8,
        label=name, edgecolors='white', linewidth=0.5
    )

plt.xlabel(f'PC1 ({pca_2d.explained_variance_ratio_[0]*100:.1f}% Variance)',
           fontsize=12)
plt.ylabel(f'PC2 ({pca_2d.explained_variance_ratio_[1]*100:.1f}% Variance)',
           fontsize=12)
plt.title('PCA — Iris Dataset (2D Projection)', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

### الخطوة 10: PCA — Loadings (تفسير الـ Components)

```python
# Loadings = مساهمة كل feature في كل component
loadings = pd.DataFrame(
    pca_2d.components_.T,
    columns=['PC1', 'PC2'],
    index=iris.feature_names
)

print("PCA Loadings (مساهمة كل feature في كل component):")
print(loadings.round(3).to_string())

# رسم Loadings
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, component, pc_name in zip(axes, pca_2d.components_, ['PC1', 'PC2']):
    colors_bar = ['#e74c3c' if x > 0 else '#3498db' for x in component]
    ax.barh(iris.feature_names, component, color=colors_bar, edgecolor='white')
    ax.set_title(f'{pc_name} Loadings', fontsize=13)
    ax.set_xlabel('Loading Value')
    ax.axvline(x=0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

### الخطوة 11: مقارنة قبل وبعد PCA (تأثير على الـ Model)

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

results = {}

# بدون PCA (كل الـ features)
model_full = LogisticRegression(max_iter=200, random_state=42)
model_full.fit(X_train_scaled, y_train)
results['All Features (4)'] = accuracy_score(y_test, model_full.predict(X_test_scaled))

# مع PCA (2 components)
model_pca2 = LogisticRegression(max_iter=200, random_state=42)
model_pca2.fit(X_train_pca, y_train)
results['PCA (2 components)'] = accuracy_score(y_test, model_pca2.predict(X_test_pca))

# مع PCA (3 components)
pca_3d = PCA(n_components=3)
X_train_pca3 = pca_3d.fit_transform(X_train_scaled)
X_test_pca3  = pca_3d.transform(X_test_scaled)
model_pca3 = LogisticRegression(max_iter=200, random_state=42)
model_pca3.fit(X_train_pca3, y_train)
results['PCA (3 components)'] = accuracy_score(y_test, model_pca3.predict(X_test_pca3))

print("\n📊 مقارنة النتائج:")
print("=" * 50)
print(f"{'Method':<25} {'Accuracy':>10} {'Features':>10}")
print("-" * 50)
for method, acc in results.items():
    n_features = int(method.split('(')[1].split(')')[0].split()[0])
    reduction = f"(-{4-n_features})" if n_features < 4 else ""
    print(f"{method:<25} {acc*100:>9.1f}% {str(n_features)+reduction:>10}")
print("=" * 50)
```

**Output متوقع:**
```
📊 مقارنة النتائج:
==================================================
Method                   Accuracy   Features
--------------------------------------------------
All Features (4)            100.0%          4
PCA (2 components)           96.7%       2(-2)
PCA (3 components)          100.0%       3(-1)
==================================================
```

---

### الكود الكامل في مكان واحد 📋

```python
"""
Dimensionality Reduction Complete Implementation
================================================
Feature Selection + PCA on Iris Dataset
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ─────────────────────────────────────────
# 1. تحميل الداتا
# ─────────────────────────────────────────
iris = load_iris()
X, y = iris.data, iris.target

# ─────────────────────────────────────────
# 2. تقسيم الداتا
# ─────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ─────────────────────────────────────────
# 3. Feature Scaling
# ─────────────────────────────────────────
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# ─────────────────────────────────────────
# 4. Feature Selection — Filter (ANOVA)
# ─────────────────────────────────────────
selector = SelectKBest(score_func=f_classif, k=3)
X_train_sel = selector.fit_transform(X_train_s, y_train)
X_test_sel  = selector.transform(X_test_s)
selected = [iris.feature_names[i] for i in selector.get_support(indices=True)]
print(f"Selected Features (ANOVA): {selected}")

# ─────────────────────────────────────────
# 5. Feature Importance — Random Forest
# ─────────────────────────────────────────
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_s, y_train)
for f, imp in sorted(zip(iris.feature_names, rf.feature_importances_),
                     key=lambda x: x[1], reverse=True):
    print(f"  {f:<25}: {imp:.3f}")

# ─────────────────────────────────────────
# 6. PCA — تحديد K
# ─────────────────────────────────────────
pca_full = PCA().fit(X_train_s)
cum_var = np.cumsum(pca_full.explained_variance_ratio_)
k_95 = np.argmax(cum_var >= 0.95) + 1
print(f"\nK لـ 95% Variance = {k_95}")

# ─────────────────────────────────────────
# 7. PCA — التطبيق
# ─────────────────────────────────────────
pca = PCA(n_components=k_95)
X_train_pca = pca.fit_transform(X_train_s)
X_test_pca  = pca.transform(X_test_s)
print(f"Variance محفوظة: {pca.explained_variance_ratio_.sum()*100:.1f}%")

# ─────────────────────────────────────────
# 8. مقارنة الأداء
# ─────────────────────────────────────────
lr = LogisticRegression(max_iter=300, random_state=42)

lr.fit(X_train_s, y_train)
acc_full = accuracy_score(y_test, lr.predict(X_test_s))

lr.fit(X_train_pca, y_train)
acc_pca = accuracy_score(y_test, lr.predict(X_test_pca))

print(f"\n📊 النتائج النهائية:")
print(f"  كل الـ features ({X_train_s.shape[1]}): {acc_full*100:.1f}%")
print(f"  PCA ({k_95} components):          {acc_pca*100:.1f}%")
print(f"  تقليل الأبعاد: {X_train_s.shape[1]} → {k_95} features")
```

---

## 9. 📝 ملخص أسئلة الانترفيو

| # | السؤال | الكلمة المفتاحية |
|---|--------|-----------------|
| 1 | إيه هي Curse of Dimensionality | Sparsity + Distance Convergence + Overfitting |
| 2 | الفرق بين Filter و Wrapper و Embedded | Stats vs Model-based vs Training-integrated |
| 3 | إيه هي الـ Principal Components | Eigenvectors + Maximum Variance Directions |
| 4 | ليه Standardization ضرورية قبل PCA | Scale-dependent Variance |
| 5 | الفرق بين Feature Selection و Extraction | Subset vs Transformation |
| 6 | إيه هو الـ Explained Variance | Eigenvalue / Sum(Eigenvalues) |
| 7 | إزاي تختار K في PCA | 95% Rule / Elbow / 2D-3D |
| 8 | Chi-Square مع القيم السالبة | MinMaxScaler أولاً |
| 9 | الترتيب الصح للـ Preprocessing | Selection → Split → Scale → PCA |
| 10 | متى t-SNE ومتى PCA | Visualization فقط vs Training |

---

## 🎓 خلاصة الدرس

```
Dimensionality Reduction = "قلل الـ Features وحافظ على المعلومات"

The Curse of Dimensionality:
  ⚠️  Sparsity → خوارزميات المسافة بتفشل
  ⚠️  Overfitting → الموديل بيحفظ مش بيتعلم
  ⚠️  Computation → وقت وموارد أكبر

Feature Selection (نختار من الأصلي):
  ✅ Filter   → سريع، بسيط، إحصاء بحت
  ✅ Wrapper  → دقيق، بطيء، بيجرب combinations
  ✅ Embedded → أفضل، Lasso + Random Forest

PCA (بنحوّل لـ features جديدة):
  ✅ Standardize الداتا أولاً (ضروري!)
  ✅ Covariance Matrix → Eigenvectors → Sort
  ✅ اختار K بـ 95% Rule أو Elbow Method
  ✅ Project الداتا على الـ K components

🔑 القواعد الأساسية:
  Feature Selection قبل Encoding
  Chi-Square مع القيم الموجبة فقط
  Scaling بعد Feature Selection وقبل PCA
  fit على Training فقط (منع Data Leakage)
  t-SNE للـ Visualization فقط، PCA للـ Training
```

---

> 💡 **نصيحة أخيرة:** في الواقع العملي، مش دايماً تحتاج PCA! جرّب الموديل على الـ features الأصلية الأول. لو عندك مشكلة في الوقت أو الـ Overfitting، ساعتها طبّق PCA. أحياناً 4 features بتدي نتيجة أحسن من 2 components.

---

*📖 المصدر: Machine Learning Diploma — Level 3, Session 6*
*🏫 AMIT Learning*