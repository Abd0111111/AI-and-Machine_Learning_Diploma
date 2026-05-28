# 🤖 Machine Learning — Session 11
## دليلك الشامل لـ Clustering (التجميع)

> 📌 **ملاحظة:** الشرح ده مصمم يكون سلس ومفيد، فيه رياضيات + كود + أمثلة حقيقية + مقارنات + أسئلة انترفيو 🎯

---

## 📚 فهرس المحتوى

1. [إيه هو Unsupervised Learning؟](#1--إيه-هو-unsupervised-learning)
2. [إيه هو Clustering؟](#2--إيه-هو-clustering)
3. [K-Means Clustering](#3--k-means-clustering)
4. [Hierarchical Clustering](#4--hierarchical-clustering)
5. [DBSCAN Clustering](#5--dbscan-clustering)
6. [مقارنة شاملة بين الخوارزميات](#6--مقارنة-شاملة-بين-الخوارزميات)
7. [أسئلة الانترفيو](#7--أسئلة-انترفيو-مهمة)

---

## 1. 🧠 إيه هو Unsupervised Learning؟

### التعريف

**Unsupervised Learning** هو نوع من التعلم الآلي بيشتغل على بيانات **مش عندها labels أو تصنيفات مسبقة** — الموديل بيكتشف الأنماط لوحده!

```
Supervised Learning:
  Input: صورة قطة   →   Label: "قطة"   →   الموديل بيتعلم

Unsupervised Learning:
  Input: صور قطط وكلاب   →   مفيش Labels   →   الموديل بيقسمهم لوحده!
```

### 🌍 مثال من الحياة الحقيقية

```
📦 تخيل عندك مخزن فيه منتجات مختلطة:
   أحذية + ملابس + إلكترونيات + طعام

🤖 الـ Unsupervised Learning بيشوف أوجه الشبه:
   → يجمع الأحذية مع بعض
   → يجمع الملابس مع بعض
   → يجمع الإلكترونيات مع بعض

⬆️ ده بالظبط زي موظف متاجر بدون تعليمات!
```

### الخوارزميات الرئيسية في Unsupervised Learning

| النوع | الأمثلة | الاستخدام |
|-------|---------|----------|
| **Clustering** | K-Means, Hierarchical, DBSCAN | تقسيم البيانات لمجموعات |
| **Association Rules** | Apriori, FP-Growth | إيجاد العلاقات بين العناصر |
| **Dimensionality Reduction** | PCA, t-SNE | تقليل عدد الـ Features |

---

## 2. 🎯 إيه هو Clustering؟

### التعريف

**Clustering** هو عملية تجميع نقاط البيانات المتشابهة مع بعض في مجموعات (Clusters)، بحيث:

```
✅ النقاط داخل نفس الـ Cluster → متشابهة جداً (High Intra-cluster similarity)
❌ النقاط في Clusters مختلفة → مختلفة عن بعض (Low Inter-cluster similarity)
```

### رسم توضيحي 🎨

```
قبل الـ Clustering:              بعد الـ Clustering:
                                 
  ● ●   ■ ■                       🔴 🔴   🔵 🔵
●   ●  ■   ■                    🔴   🔴  🔵   🔵
  ● ●   ■ ■                       🔴 🔴   🔵 🔵
       ▲ ▲                              🟢 🟢
      ▲   ▲                            🟢   🟢

     كل حاجة مخلطة!              3 Clusters واضحة!
```

### أنواع الـ Clustering

#### Hard Clustering مقابل Soft Clustering

```
Hard Clustering (K-Means):
  كل نقطة تنتمي لـ Cluster واحد بالظبط
  → نقطة A تنتمي لـ Cluster 2 (100%)

Soft Clustering (GMM):
  كل نقطة ليها احتمال انتماء لكل Cluster
  → نقطة A: 70% Cluster 1, 30% Cluster 2
```

### تطبيقات Clustering في الواقع 🌍

```
🛍️  التسويق:    تقسيم العملاء لشرائح متشابهة
🏥  الطب:       تجميع المرضى بناءً على الأعراض
📰  النصوص:     تجميع الأخبار بناءً على الموضوع
🎵  الموسيقى:   Netflix/Spotify لتوصية المحتوى
🔍  أمن المعلومات: كشف التهديدات غير المعتادة
```

---

## 3. 📊 K-Means Clustering

### إيه هو K-Means؟

**K-Means** هو خوارزمية Clustering من نوع **Centroid-based** — بتقسم البيانات لـ K مجموعات بناءً على قرب كل نقطة من مركز (Centroid) المجموعة.

> 💡 **الفكرة:** "كل نقطة تتبع أقرب مركز ليها!"

### الخطوات بالتفصيل ⚙️

```
الخطوة 1️⃣  →  اختار عدد الـ Clusters (K)
الخطوة 2️⃣  →  اختار K نقطة عشوائية كـ Centroids أولية
الخطوة 3️⃣  →  [Assignment] كل نقطة تتبع أقرب Centroid
الخطوة 4️⃣  →  [Update] احسب الـ Centroid الجديد = متوسط كل نقاط الـ Cluster
الخطوة 5️⃣  →  كرر 3 و4 لحد ما الـ Centroids متتغيرش (Convergence)
```

### مثال مرئي خطوة بخطوة 🎨

```
البيانات:  A(1,1), B(1.5,2), C(3,4), D(5,7), E(3.5,5), F(4.5,5)

K=2, Centroids الأولية: C1=(1,1), C2=(5,7)

──────── Iteration 1 ────────
Assignment:
  A(1,1)   → C1 (مسافة=0)
  B(1.5,2) → C1 (أقرب)
  C(3,4)   → C1 (أقرب)
  D(5,7)   → C2 (أقرب)
  E(3.5,5) → C2 (أقرب)
  F(4.5,5) → C2 (أقرب)

Update:
  C1_new = avg[(1,1),(1.5,2),(3,4)] = (1.83, 2.33)
  C2_new = avg[(5,7),(3.5,5),(4.5,5)] = (4.33, 5.67)

──────── Iteration 2 ────────
Assignment تتغير → Update جديد → وهكذا لحد الـ Convergence ✅
```

### إزاي تختار أفضل K؟ — Elbow Method 📈

**المفهوم:** WCSS (Within Cluster Sum of Squares) = مجموع مربعات المسافات داخل كل Cluster

```
WCSS = Σ Σ distance(xᵢ, centroid_j)²
       j  xᵢ∈Cⱼ

↓ WCSS كل ما K كبر (لحد نقطة معينة)
```

```
WCSS
  ↑
  |●
  |  ●
  |    ●            ← Elbow هنا! (K=3)
  |      ●●●●●●●   ← بيثبت
  +──────────────→ K
  1  2  3  4  5  6

الـ Elbow = النقطة اللي بعدها WCSS مش بيتحسن كتير ✅
```

### K-Means++ (الإصدار المحسّن) ⭐

مشكلة K-Means العادي: الـ Centroids الأولية العشوائية ممكن تدي نتائج وحشة!

```
K-Means++ بيختار الـ Centroids بذكاء:
  1. اختار أول Centroid عشوائياً
  2. لكل نقطة، احسب مسافتها من أقرب Centroid موجود
  3. اختار الـ Centroid الجديد باحتمالية تتناسب مع المسافة
     (النقطة الأبعد أكبر فرصة تتاختار)
  4. كرر لحد ما تجمع K Centroids
```

### مزايا وعيوب K-Means ⚖️

```
✅ المزايا:
  1. سريع ومناسب للـ datasets الكبيرة — O(n×k×i×d)
  2. سهل الفهم والتطبيق
  3. بيضمن الـ Convergence دايماً
  4. مناسب للـ Clusters الكروية الشكل

❌ العيوب:
  1. لازم تحدد K مسبقاً
  2. حساس للـ Outliers (ممكن تأثر على الـ Centroid)
  3. بيشتغل بشكل مثالي بس مع Clusters كروية الشكل
  4. نتيجته بتتغير مع كل تشغيل (عشوائي)
  5. حساس لـ Feature Scaling
```

### 💻 Implementation — K-Means

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs

# ==============================
# 1. توليد بيانات تجريبية
# ==============================
X, y_true = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=0.8,
    random_state=42
)

print(f"شكل البيانات: {X.shape}")

# ==============================
# 2. Feature Scaling (مهم جداً!)
# ==============================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==============================
# 3. Elbow Method لإيجاد أفضل K
# ==============================
wcss = []
silhouette_scores = []
k_range = range(2, 11)

for k in k_range:
    kmeans = KMeans(
        n_clusters=k,
        init='k-means++',   # استخدم K-Means++ للتهيئة
        n_init=10,           # جرب 10 مرات وخد الأحسن
        max_iter=300,
        random_state=42
    )
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# رسم Elbow Curve
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(k_range, wcss, 'bo-', linewidth=2, markersize=8)
axes[0].set_xlabel('عدد الـ Clusters (K)', fontsize=12)
axes[0].set_ylabel('WCSS (Inertia)', fontsize=12)
axes[0].set_title('Elbow Method — إيجاد أفضل K', fontsize=13)
axes[0].axvline(x=4, color='red', linestyle='--', label='K الأمثل = 4')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(k_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
axes[1].set_xlabel('عدد الـ Clusters (K)', fontsize=12)
axes[1].set_ylabel('Silhouette Score', fontsize=12)
axes[1].set_title('Silhouette Analysis', fontsize=13)
axes[1].axvline(x=4, color='red', linestyle='--', label='K الأمثل = 4')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('elbow_method.png', dpi=150, bbox_inches='tight')
plt.show()

# ==============================
# 4. تدريب الموديل النهائي
# ==============================
best_k = 4
kmeans_final = KMeans(
    n_clusters=best_k,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=42
)

labels = kmeans_final.fit_predict(X_scaled)
centroids = kmeans_final.cluster_centers_

print(f"\n✅ K-Means النتائج:")
print(f"   عدد الـ Clusters: {best_k}")
print(f"   WCSS (Inertia): {kmeans_final.inertia_:.2f}")
print(f"   Silhouette Score: {silhouette_score(X_scaled, labels):.3f}")

# توزيع النقاط على الـ Clusters
unique, counts = np.unique(labels, return_counts=True)
print(f"\n   توزيع النقاط:")
for cluster, count in zip(unique, counts):
    print(f"   Cluster {cluster}: {count} نقطة")

# ==============================
# 5. رسم النتائج
# ==============================
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']

plt.figure(figsize=(10, 7))

for i in range(best_k):
    mask = labels == i
    plt.scatter(
        X_scaled[mask, 0], X_scaled[mask, 1],
        c=colors[i], s=60, alpha=0.7,
        label=f'Cluster {i+1} ({counts[i]} نقطة)',
        edgecolors='white', linewidth=0.5
    )

# رسم الـ Centroids
plt.scatter(
    centroids[:, 0], centroids[:, 1],
    s=300, c='black', marker='★',
    zorder=5, label='Centroids'
)

plt.title('K-Means Clustering — النتيجة النهائية', fontsize=14)
plt.xlabel('Feature 1 (Scaled)')
plt.ylabel('Feature 2 (Scaled)')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('kmeans_result.png', dpi=150, bbox_inches='tight')
plt.show()

# ==============================
# 6. تطبيق حقيقي: Customer Segmentation
# ==============================
print("\n" + "="*50)
print("📊 تطبيق: Customer Segmentation")
print("="*50)

# بيانات عملاء وهمية
np.random.seed(42)
n_customers = 200

customer_data = pd.DataFrame({
    'Annual_Income': np.random.randint(15, 150, n_customers),
    'Spending_Score': np.random.randint(1, 100, n_customers),
    'Age': np.random.randint(18, 70, n_customers)
})

# Scale البيانات
X_customers = scaler.fit_transform(customer_data)

# K-Means
kmeans_customers = KMeans(n_clusters=5, init='k-means++', random_state=42)
customer_data['Cluster'] = kmeans_customers.fit_predict(X_customers)

# عرض النتائج
print("\n📋 متوسط خصائص كل Cluster:")
print(customer_data.groupby('Cluster').mean().round(2).to_string())

# وصف كل Cluster
cluster_profiles = customer_data.groupby('Cluster').mean()
print("\n🏷️ توصيف الشرائح:")
for cluster_id in range(5):
    income = cluster_profiles.loc[cluster_id, 'Annual_Income']
    spending = cluster_profiles.loc[cluster_id, 'Spending_Score']
    if income > 80 and spending > 60:
        profile = "💎 عملاء VIP — دخل عالي وإنفاق عالي"
    elif income > 80 and spending < 40:
        profile = "💰 مدخرون — دخل عالي لكن إنفاق منخفض"
    elif income < 40 and spending > 60:
        profile = "🛍️ متسوقون متحمسون — دخل منخفض لكن إنفاق عالي"
    elif income < 40 and spending < 40:
        profile = "💤 غير نشطين — دخل وإنفاق منخفضان"
    else:
        profile = "👥 متوسطون — دخل وإنفاق متوسطان"
    print(f"   Cluster {cluster_id}: {profile}")
```

---

## 4. 🌳 Hierarchical Clustering

### إيه هو Hierarchical Clustering؟

**Hierarchical Clustering** هو خوارزمية بتبني **شجرة من الـ Clusters** — بتعمل تسلسل هرمي (Hierarchy) يوضح العلاقة بين كل النقاط.

> 💡 **الميزة الكبرى:** مش محتاج تحدد K مسبقاً! الـ Dendrogram بيساعدك تختار.

### نوعان رئيسيان 🔄

```
1️⃣ Agglomerative (Bottom-Up) — الأشهر:
   يبدأ: كل نقطة = Cluster مستقل
   يدمج: الأقرب مع الأقرب تدريجياً
   ينتهي: كل البيانات في Cluster واحد

   ●  ●  ●  ●  ●       (Start: 5 Clusters)
    ↘↙    ↘↙  ↓
    [●●]  [●●] ●        (Step 1: 3 Clusters)
       ↘↙    ↓
      [●●●●] ●          (Step 2: 2 Clusters)
          ↘↙
         [●●●●●]         (End: 1 Cluster)


2️⃣ Divisive (Top-Down) — الأقل شيوعاً:
   يبدأ: كل البيانات في Cluster واحد
   يقسم: الأبعد تدريجياً
   ينتهي: كل نقطة = Cluster مستقل

   [●●●●●]               (Start: 1 Cluster)
    ↙↘
   [●●●] [●●]            (Step 1: 2 Clusters)
   ↙↘    ↙↘
  [●●][●][●][●]          (Step 2: 4 Clusters)
```

### الـ Dendrogram 🌲

الـ Dendrogram هو الشكل الشجري اللي بيوضح التسلسل الهرمي:

```
Distance
  ↑
16|                     ┌──────────────────┐
14|                     │                  │
12|           ┌──────── │ ────────┐        │
10|    ┌──────┘                   └────────┘
 8|    │
 6|    │         ┌──────┐
 4|    │         │      │
 2| ┌──┘      ┌──┘    ┌─┘
 0| │         │       │
   [1, 2]   [3, 4]   [5]    ← Data Points

كيف تقرأ الـ Dendrogram:
  🔴 اقطع عند ارتفاع معين
  🔵 عدد الـ Branches اللي القطع عبرها = عدد الـ Clusters
  ⭐ القطع المثالي = عند أطول خط رأسي (أكبر مسافة بين الدمجات)
```

### Linkage Methods — طرق ربط الـ Clusters 🔗

طريقة الربط بتحدد إزاي بنحسب المسافة بين Cluster ومجموعة نقاط:

| الطريقة | التعريف | الاستخدام المثالي | العيب |
|--------|---------|-----------------|-------|
| **Single** | أقرب نقطتين بين الـ Clusters | كشف الـ Outliers | "Chaining Effect" |
| **Complete** | أبعد نقطتين بين الـ Clusters | Clusters متوازنة | حساسية للـ Outliers |
| **Average** | متوسط كل المسافات | متوازن وشامل | أبطأ حسابياً |
| **Centroid** | مسافة بين المراكز | بيانات متجانسة | ممكن تعطي نتائج غير منطقية |
| **Ward** | يقلل زيادة الـ Variance | الأكثر استخداماً ✅ | بس مع Euclidean Distance |

```
مثال توضيحي لـ Single vs Complete:

Cluster A: {a1, a2}       Cluster B: {b1, b2}
  a1 ●    ● b1
  a2 ●    ● b2

Single Linkage:   d = min(d(a1,b1), d(a1,b2), d(a2,b1), d(a2,b2))
Complete Linkage: d = max(d(a1,b1), d(a1,b2), d(a2,b1), d(a2,b2))
Average Linkage:  d = mean(d(a1,b1), d(a1,b2), d(a2,b1), d(a2,b2))
```

### مزايا وعيوب Hierarchical Clustering ⚖️

```
✅ المزايا:
  1. مش محتاج تحدد K مسبقاً
  2. الـ Dendrogram مفيد بصرياً وبيدي فهم عميق للبيانات
  3. مش محتاج Centroids عشوائية
  4. بيدي نتيجة واحدة ثابتة (مش عشوائي زي K-Means)
  5. بيشتغل مع أي نوع Distance

❌ العيوب:
  1. بطيء جداً مع البيانات الكبيرة — O(n³) أو O(n² log n)
  2. استهلاك ذاكرة عالي
  3. مش قابل للتعديل (لو دمجت نقطتين مش تقدر تفك الدمج)
  4. حساس للـ Outliers
  5. صعب على البيانات عالية الأبعاد
```

### 💻 Implementation — Hierarchical Clustering

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import pdist

# ==============================
# 1. توليد البيانات
# ==============================
X, y_true = make_blobs(
    n_samples=150,
    centers=3,
    cluster_std=1.0,
    random_state=42
)

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==============================
# 2. رسم الـ Dendrogram
# ==============================
# حساب الـ Linkage Matrix
Z = linkage(X_scaled, method='ward')

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
dendrogram(
    Z,
    truncate_mode='lastp',   # اعرض آخر p دمجة بس
    p=20,
    leaf_rotation=90,
    leaf_font_size=10,
    show_contracted=True,
    color_threshold=6        # لون الـ Clusters المختلفة
)
plt.title('Dendrogram — Ward Linkage', fontsize=13)
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.axhline(y=6, color='red', linestyle='--', label='Cut Line (K=3)')
plt.legend()

# ==============================
# 3. تجربة Linkage Methods المختلفة
# ==============================
linkage_methods = ['ward', 'complete', 'average', 'single']
scores = {}

for method in linkage_methods:
    if method == 'ward':
        model = AgglomerativeClustering(n_clusters=3, linkage=method)
    else:
        model = AgglomerativeClustering(n_clusters=3, linkage=method)

    labels = model.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    scores[method] = score

print("📊 مقارنة Linkage Methods:")
for method, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    bar = "█" * int(score * 20)
    print(f"   {method:10s}: {score:.3f} {bar}")

best_method = max(scores, key=scores.get)
print(f"\n✅ أفضل Linkage Method: {best_method} (Score: {scores[best_method]:.3f})")

# ==============================
# 4. الموديل النهائي
# ==============================
final_model = AgglomerativeClustering(
    n_clusters=3,
    linkage='ward',
    metric='euclidean'
)

labels = final_model.fit_predict(X_scaled)

# عرض النتائج
plt.subplot(1, 2, 2)
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
for i in range(3):
    mask = labels == i
    plt.scatter(
        X_scaled[mask, 0], X_scaled[mask, 1],
        c=colors[i], s=80, alpha=0.7,
        label=f'Cluster {i+1}',
        edgecolors='white', linewidth=0.5
    )

plt.title('Hierarchical Clustering — النتيجة', fontsize=13)
plt.xlabel('Feature 1 (Scaled)')
plt.ylabel('Feature 2 (Scaled)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('hierarchical_result.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"\n✅ Hierarchical Clustering النتائج:")
print(f"   Silhouette Score: {silhouette_score(X_scaled, labels):.3f}")

# ==============================
# 5. تحديد العدد الأمثل من الـ Clusters بالـ Dendrogram
# ==============================
print("\n📏 تحليل الـ Dendrogram لاختيار K:")
print("   أكبر مسافات بين الدمجات:")

# آخر 10 دمجات (الصفوف الأخيرة في Z)
last_10 = Z[-10:]
distances = last_10[:, 2]
n_merges = len(distances)

for i, (dist, n_merges_remaining) in enumerate(zip(reversed(distances), range(n_merges, 0, -1))):
    k = i + 2  # عدد الـ Clusters لو قطعنا هنا
    gap = distances[-(i+1)] - (distances[-(i+2)] if i+2 <= n_merges else 0)
    print(f"   K={k}: المسافة عند الدمج = {dist:.2f}")
```

---

## 5. 🔍 DBSCAN Clustering

### إيه هو DBSCAN؟

**DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** هو خوارزمية بتكتشف الـ Clusters بناءً على **كثافة النقاط** — مش بناءً على المسافة لمركز.

> 💡 **الفكرة:** "الـ Cluster = منطقة كثيفة من النقاط محاطة بمناطق أقل كثافة"

### المفاهيم الأساسية 🧩

```
Parameters:
  ε (epsilon): نصف قطر الـ Neighborhood (ابحث في الدائرة دي)
  minPts: الحد الأدنى لعدد النقاط في الـ Neighborhood

أنواع النقاط:
  🔴 Core Point:    عندها ≥ minPts نقطة في دائرة ε
  🟡 Border Point:  في دائرة Core Point لكن هي نفسها مش Core Point
  ⚫ Noise Point:   مش في دائرة أي Core Point (Outlier)
```

### مثال مرئي 🎨

```
ε = 1.5, minPts = 3

        ●●
       ●●●   ← Core Points (كثيفة)
         ●
    ○              ← Border Point
                         ×   ← Noise (Outlier)
           ●●●
          ●●●●  ← Cluster تاني
           ●●●

الـ DBSCAN بيكتشف:
  Cluster 1: المجموعة فوق يسار
  Cluster 2: المجموعة تحت يمين
  Noise: النقطة المعزولة ×
```

### خطوات الخوارزمية ⚙️

```
1. لكل نقطة غير زُرت:
   a. لو Core Point → ابدأ Cluster جديد
   b. ضيف كل النقاط في دائرة ε للـ Cluster
   c. لكل Core Point في الـ Cluster، كرر الخطوة
   d. لو مش Core Point → Noise (مؤقتاً)

2. النقاط اللي اتزُرت كـ Noise ومفيش Cluster قبلها → Outliers فعلية
```

### مزايا وعيوب DBSCAN ⚖️

```
✅ المزايا:
  1. بيكتشف Clusters بأي شكل (مش بس كروية!)
  2. بيكتشف الـ Outliers تلقائياً ويعاملهم كـ Noise
  3. مش محتاج تحدد K مسبقاً
  4. مناسب للبيانات الكبيرة مع التحسينات

❌ العيوب:
  1. صعب اختيار ε و minPts المناسبين
  2. مش بيشتغل كويس لو الكثافة بتتغير بين الـ Clusters
  3. حساس لـ ε اختيار ε غلط بيخرب كل شيء
  4. مش مناسب للبيانات عالية الأبعاد (Curse of Dimensionality)
```

### 💻 Implementation — DBSCAN

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.neighbors import NearestNeighbors
from sklearn.datasets import make_moons, make_blobs

# ==============================
# 1. DBSCAN على بيانات غير كروية (قوته الحقيقية!)
# ==============================
X_moons, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

scaler = StandardScaler()
X_moons_scaled = scaler.fit_transform(X_moons)

# K-Means (بيفشل هنا!)
from sklearn.cluster import KMeans
kmeans_moons = KMeans(n_clusters=2, random_state=42)
labels_kmeans = kmeans_moons.fit_predict(X_moons_scaled)

# DBSCAN (بينجح!)
dbscan_moons = DBSCAN(eps=0.3, min_samples=5)
labels_dbscan = dbscan_moons.fit_predict(X_moons_scaled)

# مقارنة بصرية
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, labels, title in zip(
    axes,
    [labels_kmeans, labels_dbscan],
    ['K-Means (فشل!)', 'DBSCAN (نجح!)']
):
    unique_labels = set(labels)
    colors_map = {-1: 'black', 0: '#FF6B6B', 1: '#4ECDC4', 2: '#45B7D1'}

    for label in unique_labels:
        mask = labels == label
        color = colors_map.get(label, 'gray')
        marker = 'x' if label == -1 else 'o'
        label_name = 'Noise' if label == -1 else f'Cluster {label+1}'
        ax.scatter(
            X_moons_scaled[mask, 0], X_moons_scaled[mask, 1],
            c=color, s=50, marker=marker,
            alpha=0.7, label=label_name
        )

    ax.set_title(title, fontsize=13)
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.suptitle('مقارنة K-Means vs DBSCAN على بيانات هلال القمر', fontsize=14)
plt.tight_layout()
plt.savefig('dbscan_vs_kmeans.png', dpi=150, bbox_inches='tight')
plt.show()

# ==============================
# 2. إزاي تختار ε المناسب — K-Distance Plot
# ==============================
print("📏 K-Distance Plot لاختيار ε:")

k = 5  # minPts = k + 1 في الغالب
neigh = NearestNeighbors(n_neighbors=k)
neigh.fit(X_moons_scaled)
distances, _ = neigh.kneighbors(X_moons_scaled)

# المسافة من كل نقطة لأقرب K جار
k_distances = np.sort(distances[:, -1])[::-1]

plt.figure(figsize=(10, 5))
plt.plot(k_distances, 'b-', linewidth=2)
plt.xlabel('نقاط البيانات (مرتبة)')
plt.ylabel(f'المسافة لأقرب {k} جار')
plt.title('K-Distance Plot — إيجاد ε المناسب')
plt.axhline(y=0.3, color='red', linestyle='--', label='ε = 0.3 (الأمثل)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('k_distance_plot.png', dpi=150, bbox_inches='tight')
plt.show()

print("   ابحث عن 'الكوع' في الرسم → ده هو ε الأمثل!")

# ==============================
# 3. تجربة قيم مختلفة لـ ε
# ==============================
print("\n📊 تأثير قيمة ε على النتائج:")

eps_values = [0.1, 0.2, 0.3, 0.5, 0.8]

for eps in eps_values:
    dbscan = DBSCAN(eps=eps, min_samples=5)
    labels = dbscan.fit_predict(X_moons_scaled)

    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = list(labels).count(-1)
    noise_pct = n_noise / len(labels) * 100

    print(f"   ε={eps}: {n_clusters} Clusters, {n_noise} Noise points ({noise_pct:.1f}%)")

# ==============================
# 4. DBSCAN على بيانات كشف الشذوذ (Anomaly Detection)
# ==============================
print("\n" + "="*50)
print("🔍 تطبيق: Anomaly Detection في بيانات المبيعات")
print("="*50)

# بيانات مبيعات مع شذوذات
np.random.seed(42)
n_normal = 200

normal_sales = np.random.multivariate_normal(
    mean=[50, 5000],
    cov=[[100, 5000], [5000, 500000]],
    size=n_normal
)

# شذوذات (معاملات مشبوهة)
anomalies = np.array([
    [200, 1000],    # كمية عالية جداً بسعر منخفض جداً (مشبوه!)
    [5, 50000],     # كمية قليلة بسعر خيالي
    [150, 2000],    # كمية عالية بسعر منخفض
])

X_sales = np.vstack([normal_sales, anomalies])
X_sales_scaled = scaler.fit_transform(X_sales)

# DBSCAN للكشف
dbscan_anomaly = DBSCAN(eps=0.5, min_samples=10)
labels_anomaly = dbscan_anomaly.fit_predict(X_sales_scaled)

n_anomalies = list(labels_anomaly).count(-1)
print(f"\n   إجمالي المعاملات: {len(X_sales)}")
print(f"   معاملات طبيعية: {len(X_sales) - n_anomalies}")
print(f"   معاملات مشبوهة (Anomalies): {n_anomalies} 🚨")

# رسم النتائج
plt.figure(figsize=(10, 6))
normal_mask = labels_anomaly != -1
noise_mask = labels_anomaly == -1

plt.scatter(
    X_sales[normal_mask, 0], X_sales[normal_mask, 1],
    c='#4ECDC4', s=50, alpha=0.6, label='معاملات طبيعية'
)
plt.scatter(
    X_sales[noise_mask, 0], X_sales[noise_mask, 1],
    c='#FF6B6B', s=200, marker='★', zorder=5,
    label=f'شذوذات مكتشفة ({n_anomalies})'
)

plt.xlabel('الكمية المباعة')
plt.ylabel('قيمة المبيعات')
plt.title('DBSCAN — كشف الشذوذات في بيانات المبيعات')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('dbscan_anomaly.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 6. ⚖️ مقارنة شاملة بين الخوارزميات

### مقارنة الخصائص الأساسية

| المعيار | K-Means | Hierarchical | DBSCAN |
|--------|---------|-------------|--------|
| **تحديد K مسبقاً** | ✅ مطلوب | ❌ غير مطلوب | ❌ غير مطلوب |
| **شكل الـ Clusters** | كروي فقط | أي شكل | أي شكل |
| **كشف الـ Outliers** | ❌ لا | ❌ محدود | ✅ ممتاز |
| **السرعة** | ✅ سريع | ❌ بطيء | ✅ متوسط |
| **البيانات الكبيرة** | ✅ مناسب | ❌ غير مناسب | ✅ مناسب |
| **الـ Noise** | ❌ حساس | ❌ حساس | ✅ يتعامل معها |
| **Feature Scaling** | ضروري | مهم | ضروري |
| **التكرارية** | عشوائي | ثابت | ثابت |
| **التفسير** | سهل | معقد (Dendrogram) | صعب |
| **الـ Parameters** | K فقط | Linkage method | ε و minPts |

### متى تستخدم إيه؟ 🤔

```
🎯 اختار K-Means لما:
   ✓ تعرف عدد الـ Clusters تقريباً مسبقاً
   ✓ البيانات كبيرة (> 10,000 نقطة)
   ✓ الـ Clusters متوقعة تكون كروية الشكل
   ✓ تحتاج سرعة عالية
   ✓ تريد Baseline سريع

🌳 اختار Hierarchical لما:
   ✓ مش عارف عدد الـ Clusters
   ✓ تريد فهم التسلسل الهرمي للبيانات
   ✓ البيانات صغيرة (< 5,000 نقطة)
   ✓ تريد Visualization مفيدة (Dendrogram)
   ✓ التكرارية في النتائج مهمة ليك

🔍 اختار DBSCAN لما:
   ✓ الـ Clusters بأشكال غير منتظمة
   ✓ عندك Outliers وعايز تكشفها تلقائياً
   ✓ مش عارف عدد الـ Clusters
   ✓ Anomaly Detection
   ✓ بيانات جغرافية (Geographic Clustering)
```

### رسم مقارنة شاملة 🎨

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs, make_moons, make_circles

# ==============================
# مقارنة شاملة على 3 أنواع بيانات
# ==============================

# توليد أنواع مختلفة من البيانات
np.random.seed(42)

datasets = [
    (make_blobs(n_samples=300, centers=3, cluster_std=0.8, random_state=42)[0],
     "Blobs (كروية)"),
    (make_moons(n_samples=300, noise=0.05, random_state=42)[0],
     "Moons (هلالية)"),
    (make_circles(n_samples=300, noise=0.05, factor=0.5, random_state=42)[0],
     "Circles (دائرية متداخلة)"),
]

algorithms = [
    ('K-Means', KMeans(n_clusters=2, random_state=42, n_init=10)),
    ('Hierarchical\n(Ward)', AgglomerativeClustering(n_clusters=2, linkage='ward')),
    ('DBSCAN', DBSCAN(eps=0.3, min_samples=5)),
]

fig, axes = plt.subplots(3, 3, figsize=(15, 12))
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']

for row_idx, (X, dataset_name) in enumerate(datasets):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    for col_idx, (algo_name, algo) in enumerate(algorithms):
        ax = axes[row_idx, col_idx]
        labels = algo.fit_predict(X_scaled)

        unique_labels = set(labels)
        for label in unique_labels:
            mask = labels == label
            if label == -1:
                ax.scatter(X_scaled[mask, 0], X_scaled[mask, 1],
                          c='black', s=30, marker='x', alpha=0.5, label='Noise')
            else:
                ax.scatter(X_scaled[mask, 0], X_scaled[mask, 1],
                          c=colors[label % len(colors)], s=30,
                          alpha=0.7, label=f'C{label+1}')

        n_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)
        n_noise = list(labels).count(-1)

        ax.set_title(f'{algo_name}\n({n_clusters} Clusters, {n_noise} Noise)', fontsize=10)
        if col_idx == 0:
            ax.set_ylabel(dataset_name, fontsize=11, fontweight='bold')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(True, alpha=0.2)

plt.suptitle('مقارنة شاملة: K-Means vs Hierarchical vs DBSCAN\nعلى أشكال بيانات مختلفة',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('algorithms_comparison.png', dpi=150, bbox_inches='tight')
plt.show()

# ==============================
# مقارنة الأداء والسرعة
# ==============================
import time
from sklearn.datasets import make_blobs

print("\n" + "="*60)
print("⏱️ مقارنة السرعة والأداء")
print("="*60)

n_samples_list = [1000, 5000, 10000]

for n in n_samples_list:
    X, _ = make_blobs(n_samples=n, centers=4, random_state=42)
    X_scaled = StandardScaler().fit_transform(X)

    print(f"\n📊 حجم البيانات: {n} نقطة")

    for name, algo in [
        ('K-Means    ', KMeans(n_clusters=4, random_state=42, n_init=10)),
        ('Hierarchical', AgglomerativeClustering(n_clusters=4)),
        ('DBSCAN     ', DBSCAN(eps=0.5, min_samples=5)),
    ]:
        start = time.time()
        algo.fit(X_scaled)
        elapsed = time.time() - start
        print(f"   {name}: {elapsed:.4f} ثانية")
```

### Evaluation Metrics — إزاي نقيم نتائج الـ Clustering؟

```python
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import numpy as np

X, y_true = make_blobs(n_samples=300, centers=4, random_state=42)
X_scaled = StandardScaler().fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

# ==============================
# 1. Silhouette Score
# ==============================
# القيمة: من -1 لـ 1 (كلما أقرب لـ 1 كلما أحسن)
silhouette = silhouette_score(X_scaled, labels)

# ==============================
# 2. Davies-Bouldin Index
# ==============================
# القيمة: أقرب لـ 0 = أحسن (Clusters أكثر انفصالاً)
davies_bouldin = davies_bouldin_score(X_scaled, labels)

# ==============================
# 3. Calinski-Harabasz Score
# ==============================
# القيمة: أكبر = أحسن (Clusters أكثر تماسكاً وانفصالاً)
calinski = calinski_harabasz_score(X_scaled, labels)

print("📊 Evaluation Metrics:")
print(f"""
   ┌────────────────────────────────────────┐
   │ المقياس               │ القيمة        │
   ├────────────────────────────────────────┤
   │ Silhouette Score      │ {silhouette:.3f}         │
   │   (الأقرب لـ 1 أحسن) │               │
   ├────────────────────────────────────────┤
   │ Davies-Bouldin Index  │ {davies_bouldin:.3f}         │
   │   (الأقرب لـ 0 أحسن) │               │
   ├────────────────────────────────────────┤
   │ Calinski-Harabasz     │ {calinski:.1f}     │
   │   (الأكبر أحسن)      │               │
   └────────────────────────────────────────┘
""")

# مقارنة المقاييس عبر K مختلفة
print("📈 مقارنة المقاييس مع قيم K مختلفة:")
print(f"{'K':>5} {'Silhouette':>12} {'Davies-Bouldin':>16} {'Calinski':>12}")
print("-" * 50)

for k in range(2, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    lbl = km.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, lbl)
    dbi = davies_bouldin_score(X_scaled, lbl)
    cal = calinski_harabasz_score(X_scaled, lbl)
    marker = " ← أفضل!" if k == 4 else ""
    print(f"{k:>5} {sil:>12.3f} {dbi:>16.3f} {cal:>12.1f}{marker}")
```

---

## 7. 📝 أسئلة انترفيو مهمة

---

> ### 🎤 سؤال انترفيو #1
> **"إيه الفرق بين Supervised و Unsupervised Learning؟"**
>
> **الإجابة:** في Supervised Learning، البيانات عندها Labels (مثلاً صورة + تصنيف "قطة"). الموديل بيتعلم يتنبأ بالـ Label. في Unsupervised Learning، مفيش Labels — الموديل بيكتشف الأنماط لوحده. Clustering هو أشهر مثال للـ Unsupervised Learning.

---

> ### 🎤 سؤال انترفيو #2
> **"إيه الـ Inertia في K-Means وإزاي بتستخدمها؟"**
>
> **الإجابة:** الـ Inertia (أو WCSS) هي مجموع مربعات المسافات بين كل نقطة والـ Centroid بتاعها عبر كل الـ Clusters. كلما الـ Inertia أقل كلما الـ Clusters أحسن. بنستخدمها في الـ Elbow Method — نرسم Inertia مقابل K، ونختار K عند "الكوع" (النقطة اللي بعدها الـ Inertia مش بتتحسن كتير).

---

> ### 🎤 سؤال انترفيو #3
> **"ليه K-Means بيدي نتائج مختلفة مع كل تشغيل؟ وإزاي نحل ده؟"**
>
> **الإجابة:** لأن الـ Centroids الأولية بتتاختار عشوائياً — نقطة بداية مختلفة = نتيجة مختلفة (Local Optima مختلف). الحل هو K-Means++ اللي بيختار الـ Centroids بذكاء، أو تعيين `n_init=10` عشان الخوارزمية تجرب 10 نقاط بداية مختلفة وتاخد الأحسن.

---

> ### 🎤 سؤال انترفيو #4
> **"إمتى تفضل DBSCAN على K-Means؟"**
>
> **الإجابة:** أفضل DBSCAN في 3 حالات: (1) لو الـ Clusters بأشكال غير كروية (هلالية، دائرية، إلخ) — K-Means بيفشل هنا. (2) لو عندي Outliers وعايز أكشفها تلقائياً — DBSCAN بيعاملها كـ Noise. (3) لو مش عارف عدد الـ Clusters مسبقاً. في المقابل، K-Means أسرع بكتير مع البيانات الكبيرة.

---

> ### 🎤 سؤال انترفيو #5
> **"إيه هو الـ Silhouette Score وإزاي بتفسره؟"**
>
> **الإجابة:** الـ Silhouette Score بيقيس جودة الـ Clustering — بيحسب لكل نقطة:
> - `a` = متوسط المسافة لنقاط نفس الـ Cluster
> - `b` = متوسط المسافة لأقرب Cluster تاني
> - `s = (b - a) / max(a, b)`
>
> القيمة من -1 لـ 1:
> - قريب من 1: النقطة في الـ Cluster الصح تماماً ✅
> - قريب من 0: النقطة على حدود بين Clusters
> - سالب: النقطة في الـ Cluster الغلط ❌

---

> ### 🎤 سؤال انترفيو #6
> **"إيه مشكلة K-Means مع الـ Outliers وإزاي نتعامل معاها؟"**
>
> **الإجابة:** K-Means حساس جداً للـ Outliers لأن الـ Centroid = متوسط النقاط — نقطة شاذة واحدة بعيدة جداً ممكن تشد الـ Centroid بعيد عن المجموعة الحقيقية. الحلول: (1) K-Medoids بدل K-Means (يستخدم وسيط بدل متوسط). (2) إزالة الـ Outliers قبل التطبيق. (3) استخدام DBSCAN بدلاً منه.

---

> ### 🎤 سؤال انترفيو #7
> **"إيه هو الـ Linkage Method في Hierarchical Clustering وإيه الأفضل؟"**
>
> **الإجابة:** الـ Linkage Method بيحدد إزاي نحسب المسافة بين Cluster ومجموعة نقاط: Single (أقرب نقطتين)، Complete (أبعد نقطتين)، Average (المتوسط)، Ward (يقلل الـ Variance). الأفضل في الغالب هو **Ward** لأنه بينتج Clusters متوازنة في الحجم وبيتعامل كويس مع الـ Noise — لكن بيشتغل بس مع Euclidean Distance.

---

> ### 🎤 سؤال انترفيو #8
> **"إزاي تختار ε و minPts في DBSCAN؟"**
>
> **الإجابة:**
> - **minPts:** اختار قيمة ≥ عدد الـ Dimensions + 1 (في الغالب 4-5 للبيانات ثنائية الأبعاد). كلما البيانات أكبر ومعقدة، زود minPts.
> - **ε:** استخدم الـ K-Distance Plot — ارسم مسافة كل نقطة لأقرب K جار (K=minPts-1)، رتبها تنازلياً، وابحث عن "الكوع" في الرسم. النقطة عند الكوع = ε الأمثل.

---

> ### 🎤 سؤال انترفيو #9
> **"إزاي تعمل Clustering على بيانات نصية؟"**
>
> **الإجابة:** البيانات النصية تحتاج تحويل لـ Vectors أولاً:
> 1. استخدم TF-IDF أو Word Embeddings (Word2Vec, BERT) لتحويل النصوص
> 2. استخدم Cosine Distance بدل Euclidean (لأن الاتجاه أهم من الحجم)
> 3. K-Means مع Cosine هو الأكثر استخداماً في تجميع النصوص
> 4. ممكن تستخدم Hierarchical Clustering مع Cosine Distance كمان

---

> ### 🎤 سؤال انترفيو #10
> **"إيه هو Hard Clustering وإيه الفرق مع Soft Clustering؟ مثال؟"**
>
> **الإجابة:**
> - **Hard Clustering (K-Means):** كل نقطة تنتمي لـ Cluster واحد بالظبط. النقطة A = Cluster 2 (100%).
> - **Soft Clustering (GMM):** كل نقطة عندها احتمالات انتماء لكل Cluster. النقطة A: 70% Cluster 1، 30% Cluster 2.
>
> الـ Soft Clustering أفضل للبيانات على الحدود بين Clusters، لكنه أبطأ وأصعب تفسيراً.

---

## 🎓 خلاصة الدرس

```
┌─────────────────────────────────────────────────────────────┐
│                   Clustering Cheat Sheet                    │
├───────────────┬─────────────┬──────────────┬───────────────┤
│               │   K-Means   │ Hierarchical │    DBSCAN     │
├───────────────┼─────────────┼──────────────┼───────────────┤
│ تحديد K       │ ✅ مطلوب    │ ❌ لا        │   ❌ لا        │
│ شكل Clusters  │ كروي فقط     │ أي شك       │  أي شكل       │
│ الـ Outliers  │ ❌ حساس     │ ❌ حس       │  ✅ يكشفها    │
│ السرعة        │ ✅ سريع     │ ❌ بطي      │  ✅ متوسط     │
│ البيانات      │ كبيرة ✅    │ صغيرة فقط   │  كبيرة ✅     │
└───────────────┴─────────────┴──────────────┴───────────────┘

🔑 القاعدة الذهبية:
   K-Means     = سرعة + بساطة + Clusters كروية
   Hierarchical = فهم عميق + Visualization + بيانات صغيرة
   DBSCAN      = أشكال معقدة + كشف Outliers + مرونة

⚠️ لازم دايماً:
   1. Feature Scaling قبل أي Clustering!
   2. جرب أكتر من خوارزمية وقارن
   3. استخدم Silhouette Score للتقييم
   4. Visualize النتائج دايماً
```

---

*📖 المصدر: Machine Learning Session 11 — Clustering Algorithms*
*🎓 AMIT Learning — Machine Learning Diploma*