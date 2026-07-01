# 🧠 Session 3 — من أساسيات الـ Neural Networks لحد الـ CNN Architectures

## 📌 مقدمة السيشن

السيشن دي نقلة نوعية مهمة في رحلتك مع الـ Deep Learning. بدأنا بمراجعة الأساسيات اللي أي شبكة عصبية بسيطة (Feedforward Neural Network) بتقوم عليها — إزاي بتقرر شكل الـ output layer بتاعتها حسب نوع المشكلة، وإزاي بتختار الـ activation function المناسب في كل جزء منها. بعد كده طبقنا الكلام ده عمليًا على داتا حقيقية (car_purchasing) وبنينا أول موديل Regression باستخدام Keras.

لكن أهم جزء في السيشن كان النقلة من الشبكات العصبية العادية (اللي بتشتغل مع بيانات جدولية أو نصية) لعالم تاني تمامًا: **الـ Convolutional Neural Networks (CNNs)** — الشبكات المتخصصة في فهم الصور. هنا هتفهم إزاي الكمبيوتر "بيشوف" الصورة، وإزاي المعمار ده اتطور من سنة 1998 (LeNet-5) لحد أحدث المعماريات (EfficientNet)، وإزاي تستخدم موديلات جاهزة ومتدربة بالفعل (Transfer Learning) بدل ما تبدأ من الصفر.

الملف ده هيكون مرجعك الكامل للسيشن، منظم في 3 أجزاء رئيسية، وكل جزء فيه أسئلة انترفيو ممكن تتسأل فيها.

---

## 📚 جدول المحتويات

1. [الجزء الأول: مراجعة Neural Networks الأساسية](#part1)
2. [الجزء الثاني: أول تطبيق عملي — Regression Model](#part2)
3. [الجزء الثالث: مقدمة إلى CNNs](#part3)
4. [الجزء الرابع: هيكل الـ CNN بالتفصيل](#part4)
5. [الجزء الخامس: معماريات الـ CNN الشهيرة](#part5)
6. [الجزء السادس: Transfer Learning](#part6)
7. [خلاصة السيشن](#summary)

---

<a name="part1"></a>
## 1️⃣ الجزء الأول: مراجعة Neural Networks الأساسية

### 🔹 التلاتة Layers الأساسية

أي Feedforward Neural Network بسيطة بتتكون من:

```
Input Layer  →  Hidden Layer(s)  →  Output Layer
   (بيانات)        (تعلّم الأنماط)      (القرار النهائي)
```

| Layer | وظيفته | ملاحظة |
|---|---|---|
| **Input** | استقبال الـ features | عدد الـ neurons = عدد الأعمدة (features) في الداتا |
| **Hidden** | تعلّم الأنماط غير الخطية | ممكن يكون فيه أكتر من طبقة (Deep) |
| **Output** | إعطاء القرار/التنبؤ النهائي | شكلها بيتغير حسب نوع المشكلة |

### 🔹 التغيرات في الـ Output Layer حسب نوع المشكلة

ده أهم جزء لازم يبقى محفوظ عندك 100%:

| نوع المشكلة | عدد neurons في output | Activation Function |
|---|---|---|
| **Regression** | 1 (أو أكتر لو multi-output) | من غير activation (Linear) |
| **Binary Classification** | 1 | Sigmoid |
| **Multi-class Classification** | = عدد الـ classes | Softmax |

> 💡 **ليه الـ Regression من غير activation؟**
> لأن الـ output المطلوب رقم حر (ممكن يكون أي قيمة)، فمش منطقي نحصره بين 0 و1 زي الـ Sigmoid أو نخليه موجب بس زي الـ ReLU.

### 🔹 الـ Non-linearity Functions (Activation Functions)

#### أ) Sigmoid
$$\sigma(z) = \frac{1}{1+e^{-z}}$$

- بتحول أي رقم لقيمة بين **0 و 1**
- **العيب**: مشكلة الـ **Vanishing Gradient** — كل ما z تكبر أو تصغر جدًا، الـ gradient بيقرب من صفر فالتعلم بيبطأ أو يقف
- دلوقتي بتُستخدم غالبًا في الـ **output layer** بس (للـ binary classification)، مش في الـ hidden layers

#### ب) Tanh
$$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$$

- بتحول القيمة لرقم بين **-1 و 1**
- أفضل من Sigmoid لأنها **zero-centered** (متوسطها صفر) → تعلّم أسرع شوية
- برضو بتعاني من Vanishing Gradient بس بدرجة أقل

#### ج) ReLU (Rectified Linear Unit)
$$ReLU(z) = \max(0, z)$$

- لو z موجبة ترجعها زي ما هي، لو سالبة ترجع 0
- **الميزة**: بسيطة وسريعة حسابيًا + بتحل مشكلة الـ Vanishing Gradient
- **العيب**: مشكلة **Dying ReLU** — الـ neuron ممكن "تموت" لو دخلت منطقة سالبة (gradient = 0 دايمًا)
- هي المعيار الحالي (default) في الـ hidden layers

**الترتيب التاريخي/العملي**: Sigmoid → Tanh → ReLU (المستخدمة حاليًا في أغلب الشبكات)

### 🔹 Softmax Function (لـ Multi-class Classification)

**الفكرة الأساسية**: لما يكون عندك أكتر من class (مثلاً 3 أو 10 كلاسات)، عايز الشبكة تديك **احتمال لكل class**، وبحيث **مجموع كل الاحتمالات = 1**.

**الصيغة الرياضية**:

$$\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}$$

يعني: الأس (exponential) بتاع القيمة الحالية، مقسوم على مجموع الأسس بتاعة كل القيم التانية.

**ليه بنستخدم الصيغة دي بالذات؟**
1. الـ exponential (e^z) بتضمن إن كل القيم تبقى **موجبة** (مش زي القيم الخام اللي ممكن تكون سالبة)
2. القسمة على المجموع بتضمن إن الناتج يبقى **نسبة** (بين 0 و1) وإن **مجموع كل الاحتمالات = 1**
3. بتكبّر الفروق بين القيم (بسبب الـ exponential) → القيمة الأكبر بتاخد نصيب أكبر بوضوح من الاحتمال، وده بيسهّل على الموديل يميّز بين الـ classes

**مثال بسيط**: لو عندك 3 classes وطلعتلك القيم الخام (logits): `[2.0, 1.0, 0.1]`

```
e^2.0 = 7.39
e^1.0 = 2.72
e^0.1 = 1.11
المجموع = 11.22

softmax = [7.39/11.22, 2.72/11.22, 1.11/11.22]
        = [0.66, 0.24, 0.10]   ← المجموع = 1.0 ✅
```

يبقى الموديل "واثق" بنسبة 66% إن الإجابة هي الـ class الأول.

### ❓ أسئلة انترفيو محتملة — الجزء الأول

1. ليه مبنحطش activation function على الـ output layer في الـ Regression؟
2. ما الفرق بين Sigmoid و Softmax، ومتى تستخدم كل واحدة؟
3. اشرح مشكلة الـ Vanishing Gradient وإزاي ReLU بتحلها.
4. ما هي مشكلة الـ Dying ReLU وإزاي ممكن تتجنبها؟ (تلميح: Leaky ReLU)
5. ليه بنستخدم exponential في الـ Softmax بدل ما نقسم القيم الخام على مجموعها مباشرة؟

---

<a name="part2"></a>
## 2️⃣ الجزء الثاني: أول تطبيق عملي — Regression Model

استخدمنا داتا **car_purchasing** للتنبؤ بمبلغ شراء السيارة (car purchase amount) بناءً على بيانات العميل.

### 🔹 استيراد الداتا

```python
import pandas as pd
df = pd.read_csv(r'car_purchasing.csv.xls', encoding='ISO-8859-1')
df.info()
```

> ⚠️ ملاحظة: الملف امتداده `.xls` لكنه فعليًا CSV نص عادي، والـ encoding بتاعه `ISO-8859-1` مش UTF-8 العادي — لو ما حددتهاش هيديك error.

### 🔹 تجهيز البيانات (Preprocessing)

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# شيل الأعمدة النصية غير المفيدة (اسم، إيميل، دولة)
X = df.iloc[:, 3:-1]
y = df.iloc[:, -1]

# Scaling - مهم جدًا عشان استقرار الـ gradient descent
scaler = MinMaxScaler()
X = scaler.fit_transform(X)
y = scaler.fit_transform(y.values.reshape(-1, 1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### 🔹 بناء الموديل

```python
model = Sequential()
model.add(Dense(10, activation='relu', input_dim=5))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='linear'))   # Regression → Linear, من غير activation فعليًا
model.compile(loss='mean_squared_error', optimizer='adam')
model.summary()
```

**تحليل المعمار**:
- Input: 5 features
- Hidden Layer 1: 10 neurons + ReLU
- Hidden Layer 2: 10 neurons + ReLU
- Output: 1 neuron + Linear (زي ما اتفقنا في الجزء النظري)
- Loss Function: **MSE** (Mean Squared Error) — المناسب للـ regression

### 🔹 تدريب الموديل ومتابعة الأداء

```python
history = model.fit(X_train, y_train, validation_split=0.2, epochs=1000)
```

بعدها بنرسم الـ Training vs Validation Loss عشان نشوف هل الموديل بيعمل **overfitting** ولا لأ، ونحدد الـ **best epoch** (أقل validation loss).

### 🔹 تقييم الموديل

```python
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

y_pred = model.predict(X_test)
MSE = mean_squared_error(y_test, y_pred)
MAE = mean_absolute_error(y_test, y_pred)
R2 = r2_score(y_test, y_pred)
```

| Metric | المعنى |
|---|---|
| **MSE** | متوسط مربع الخطأ — بيعاقب الأخطاء الكبيرة بشدة |
| **MAE** | متوسط الخطأ المطلق — أسهل في التفسير (بنفس وحدة الـ target) |
| **R² Score** | نسبة التباين اللي الموديل عرف يفسّرها (0 → 1، وكل ما اقترب من 1 كان أفضل) |

### ❓ أسئلة انترفيو محتملة — الجزء الثاني

1. ليه لازم تعمل Scaling للـ features والـ target قبل التدريب؟
2. ما الفرق بين MSE و MAE، ومتى تفضّل واحد عن التاني؟
3. إزاي تعرف إن الموديل بتاعك بيعمل Overfitting من الـ Loss curve؟
4. ليه استخدمنا `validation_split` بدل ما نعتمد على الـ test set بس أثناء التدريب؟

---

<a name="part3"></a>
## 3️⃣ الجزء الثالث: مقدمة إلى Convolutional Neural Networks (CNNs)

### 🔹 تعريف الـ CNN

الـ **CNN** هي فئة من الـ Deep Learning models متخصصة أساسًا في **معالجة الصور والـ Computer Vision**. الفكرة إنها بتحاول تقلّد طريقة **الجهاز البصري البشري** في التعرف على الأنماط مباشرة من الصور، من غير ما حد يقولها يدويًا "دور على الحواف هنا" أو "دور على الألوان هناك".

### 🔹 ليه الـ CNNs مهمة؟

الفرق الجوهري بينها وبين الـ Machine Learning التقليدي:

```
Traditional ML:  صورة → [مهندس بيستخرج features يدويًا] → موديل → تصنيف
CNN:             صورة → [الشبكة نفسها بتتعلم تستخرج الـ features] → تصنيف
```

يعني CNN بتستخرج الـ features (حواف، textures، أشكال) **تلقائيًا** من غير Feature Engineering يدوي، وده اللي خلاها تحدث ثورة في:
- **Medical Imaging** (تحليل صور الأشعة)
- **Self-driving cars** (التعرف على المشاة والإشارات)
- **Facial Recognition** (فتح الموبايل بالوجه)

### 🔹 تطبيقات الـ CNNs

| التطبيق | مثال |
|---|---|
| Image Classification | التفرقة بين صور القطط والكلاب |
| Object Detection | السيارة ذاتية القيادة بتكتشف المشاة |
| Medical Imaging | اكتشاف الأورام من صور الـ MRI |
| Facial Recognition | فتح الموبايل بـ Face ID |
| Autonomous Systems | الروبوتات وكاميرات المراقبة الأمنية |

### ❓ أسئلة انترفيو محتملة — الجزء الثالث

1. ما الفرق الأساسي بين CNN و Fully Connected Neural Network عادية في التعامل مع الصور؟
2. ليه لو استخدمت Dense layers بس (من غير Conv layers) مع صورة كبيرة هيكون فيه مشكلة؟ (تلميح: عدد الـ parameters)
3. اذكر 3 تطبيقات حقيقية للـ CNN في الصناعة.

---

<a name="part4"></a>
## 4️⃣ الجزء الرابع: هيكل الـ CNN بالتفصيل

الـ CNN بتتكون من سلسلة layers بتشتغل مع بعض:

```
الصورة → [Convolution + ReLU] → [Pooling] → ... (تتكرر) ... → [Flatten] → [Fully Connected] → Output
```

### 🔹 أ) Convolutional Layer

هي **الوحدة الأساسية** اللي بتبني عليها الـ CNN كلها.

- بتطبّق **filters (kernels)** — مصفوفات صغيرة (زي 3×3 أو 5×5) — بتتحرك (تعمل "sliding window") فوق الصورة
- كل filter بيستخرج نوع معين من الـ features (حواف، زوايا، textures)
- الناتج اسمه **Feature Map**، وهو بيوضح مكان وجود الـ feature ده في الصورة

```
مثال بسيط لـ Convolution:

Image patch:        Filter (edge detector):      Result:
1  2  3              -1   0   1                  
4  5  6      *        -1   0   1        =        قيمة واحدة تمثل
7  8  9               -1   0   1                  "قوة" الحافة في المكان ده
```

### 🔹 ب) Activation Function (ReLU)

بعد كل Convolution، بنطبّق **ReLU** مباشرة:

- بتحوّل أي قيمة سالبة (pixel value) لصفر
- بتدخل **non-linearity** للموديل — من غيرها الشبكة كلها هتبقى مجرد عمليات خطية مهما زاد عدد الـ layers
- بتساعد الـ CNN تتعلم أنماط معقدة مش بس علاقات خطية

### 🔹 ج) Pooling Layer

وظيفتها **تقليل أبعاد** الـ feature maps مع الحفاظ على المعلومة المهمة.

| نوع Pooling | الطريقة |
|---|---|
| **Max Pooling** | بياخد أعلى قيمة في كل منطقة (الأكثر استخدامًا) |
| **Average Pooling** | بياخد متوسط القيم في كل منطقة |

**فوائدها**:
- تقليل الحسابات (Computational Efficiency)
- تقليل الـ Overfitting
- الحفاظ على أهم المعلومات مع تصغير حجم البيانات

```
مثال Max Pooling (2×2):

1  3  |  2  4          
5  6  |  7  8    →      6   8
------+------           9   4
2  1  |  9  4
0  3  |  1  2
```

### 🔹 د) Flatten Layer

- بتحوّل الـ tensor متعدد الأبعاد (ناتج الـ Conv/Pooling) إلى **متجه (vector) بعد واحد فقط (1D)**
- الطبقة دي **مفيهاش أي تعلّم** — هي بس بتعيد ترتيب البيانات (reshape) عشان تقدر تدخل الـ Dense layer

```
Feature maps (مثلاً 5×5×16) → Flatten → متجه من 400 قيمة
```

### 🔹 هـ) Fully Connected (Dense) Layer

- كل neuron فيها متصل بكل الـ neurons في الطبقة اللي قبلها
- دورها إنها **تجمّع** الـ features المستخرجة من الـ Conv layers وتاخد **القرار النهائي**
- بتعمل weighted sum للمدخلات، متبوعة بـ activation function (ReLU في الطبقات الوسطى، Softmax في الـ output)

### ❓ أسئلة انترفيو محتملة — الجزء الرابع

1. ما الفرق بين Convolution Layer و Fully Connected Layer من ناحية عدد الـ parameters؟
2. ليه بنحتاج Pooling Layer، وإيه الفرق بين Max و Average Pooling؟
3. ما وظيفة الـ Flatten Layer بالظبط، وهل بتتعلم حاجة؟
4. اشرح إزاي الـ filter (kernel) بيستخرج feature معين من الصورة.
5. ليه بنحط ReLU بعد كل Convolution مباشرة؟

---

<a name="part5"></a>
## 5️⃣ الجزء الخامس: معماريات الـ CNN الشهيرة (CNN Architectures)

### 🔹 ليه فيه معماريات مختلفة؟

مع تطور الأبحاث، الباحثين صمموا معماريات جديدة عشان:
- يحسّنوا الـ Accuracy
- يقللوا الـ Computation
- يحلّوا مشاكل زي الـ Vanishing Gradient

بعض المعماريات مُحسّنة للسرعة، وبعضها للعمق والدقة.

---

### 🅰️ LeNet-5 (1998)

طوّرها **Yann LeCun**، من أقدم معماريات الـ CNN، صُممت للتعرف على الأرقام المكتوبة بخط اليد (MNIST dataset).

**7 طبقات** (بدون الـ input):

| Layer | التفاصيل | الناتج |
|---|---|---|
| Input | 32×32 (أكبر من 28×28 عشان التشوهات المحتملة) | 32×32×1 |
| C1 - Conv | 6 filters, 5×5, stride=1 | 28×28×6 |
| S2 - Avg Pooling | 2×2, stride=2 | 14×14×6 |
| C3 - Conv | 16 filters, 5×5 | 10×10×16 |
| S4 - Avg Pooling | 2×2, stride=2 | 5×5×16 |
| F5 - Dense | 120 neuron | Sigmoid/ReLU |
| F6 - Dense | 84 neuron | Sigmoid/ReLU |
| Output | 10 neuron (أرقام 0-9) | Softmax |

**أهم مميزاته**: Parameter Sharing (تقليل عدد الـ parameters)، وFeature Hierarchy (features بسيطة في البداية → معقدة في العمق).

---

### 🅱️ AlexNet (2012)

طوره **Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton**، وفاز بمسابقة **ImageNet (ILSVRC-2012)** — دي اللحظة اللي فجّرت ثورة الـ Deep Learning الحديثة.

**8 layers**: 5 Convolutional + 3 Fully Connected

| Layer | التفاصيل |
|---|---|
| Input | 227×227×3 |
| Conv1 | 96 filters, 11×11, stride=4 → ReLU → MaxPool → 27×27×96 |
| Conv2 | 256 filters, 5×5 → ReLU + LRN → MaxPool → 13×13×256 |
| Conv3 | 384 filters, 3×3 → ReLU |
| Conv4 | 384 filters, 3×3 → ReLU |
| Conv5 | 256 filters, 3×3 → ReLU → MaxPool → 6×6×256 |
| FC6 | 4096 neuron + ReLU + Dropout 50% |
| FC7 | 4096 neuron + ReLU + Dropout 50% |
| FC8 (Output) | 1000 neuron (ImageNet classes) + Softmax |

**أهم مميزاته**:
- استخدام ReLU بدل Sigmoid/Tanh → تدريب أسرع بكتير
- **Dropout** لمنع الـ Overfitting
- تدريب على **2 GPU** بالتوازي (GTX 580)
- **Local Response Normalization (LRN)** — اتستبدلت لاحقًا بـ Batch Normalization

---

### 🆚 VGGNet (2014)

طوّرته **Simonyan & Zisserman** في جامعة Oxford، وحصلت على المركز الثاني في ILSVRC-2014.

**الفكرة المميزة**: معمار **عميق ومنتظم (uniform)** باستخدام فلاتر صغيرة **3×3 فقط** بدل الفلاتر الكبيرة زي AlexNet.

**نسخ متعددة**: VGG-11, VGG-13, VGG-16, VGG-19 (حسب العمق)

**VGG16 بالتفصيل**:

```
Input (227×227×3)
   ↓
Block 1: 2×Conv(64, 3×3) → MaxPool
Block 2: 2×Conv(128, 3×3) → MaxPool
Block 3: 3×Conv(256, 3×3) → MaxPool
Block 4: 3×Conv(512, 3×3) → MaxPool
Block 5: 3×Conv(512, 3×3) → MaxPool
   ↓
Dense(4096, ReLU) → Dense(4096, ReLU) → Dense(1000, Softmax)
```

**أهم مميزاته**: فلاتر صغيرة موحدة (3×3) بتقلل الـ parameters وتحافظ على دقة عالية، لكن المعمار تقيل جدًا في عدد الـ parameters.

---

### 🔴 ResNet (2015)

طوّره **Kaiming He**، وفاز بـ ILSVRC-2015 بدقة تفوق الأداء البشري في التصنيف. النسخ: ResNet-18, 34, 50, 101, 152.

**الابتكار الأهم**: **Residual Learning (Skip Connections)** — بدل ما كل طبقة تتعلم من الصفر، بتتعلم "الفرق" (residual) بين المدخل والمخرج، وده بيسمح ببناء شبكات عميقة جدًا (لحد 1000 layer) من غير ما الأداء يتدهور.

```
Input ──┬──────────────────────┐
        │                      │
        ↓                      │ (Skip Connection)
   [Conv → BN → ReLU]          │
        ↓                      │
   [Conv → BN]                 │
        ↓                      │
        + ←────────────────────┘
        ↓
      ReLU
```

**ResNet50 بالتفصيل**:
- Input: 227×227×3
- Initial Conv: 7×7, 64 filters, stride=2 → BatchNorm → ReLU → MaxPool
- Residual Blocks: Conv2_x (256) → Conv3_x (512) → Conv4_x (1024) → Conv5_x (2048)
- Global Average Pooling
- FC (1000 classes, Softmax)

**أهم مميزاته**: حل مشكلة Vanishing Gradient، شبكات عميقة جدًا من غير تدهور في الأداء، ودقة أعلى بكتير من VGG/AlexNet.

---

### ⚡ EfficientNet (2019)

طوّره **Mingxing Tan & Quoc Le** في Google AI. الفكرة المختلفة عن كل المعماريات السابقة: **Compound Scaling**.

**المشكلة اللي بتحلها**: المعماريات التقليدية بتكبّر بُعد واحد بس (أعمق أو أعرض)، لكن EfficientNet بتكبّر **3 أبعاد مع بعض بنسب محسوبة**:

| البُعد | المعنى |
|---|---|
| **Depth (D)** | عدد الطبقات — feature extraction أفضل |
| **Width (W)** | عدد القنوات في كل طبقة — feature maps أغنى |
| **Resolution (R)** | حجم الصورة المدخلة — تفاصيل أدق |

**النسخ**: B0 (الأصغر) → B7 (الأكبر، أعلى دقة لكن أثقل حسابيًا)

**EfficientNetB0**: بتستخدم **MBConv** (زي MobileNetV2)، **Squeeze-and-Excitation blocks**، و**Swish activation** (أفضل من ReLU في تدفق الـ gradient).

---

### 📊 مقارنة سريعة بين المعماريات

| المعمار | السنة | العمق | أهم ابتكار |
|---|---|---|---|
| LeNet-5 | 1998 | 7 layers | أول CNN عملي |
| AlexNet | 2012 | 8 layers | ReLU + Dropout + GPU |
| VGGNet | 2014 | 16-19 layers | فلاتر 3×3 موحدة |
| ResNet | 2015 | حتى 152+ layer | Skip Connections |
| EfficientNet | 2019 | B0-B7 | Compound Scaling |

### ❓ أسئلة انترفيو محتملة — الجزء الخامس

1. إيه المشكلة اللي حلّها ResNet باستخدام Skip Connections بالظبط؟
2. ليه VGGNet استخدمت فلاتر 3×3 بس بدل الفلاتر الكبيرة اللي كانت مستخدمة في AlexNet؟
3. اشرح فكرة الـ Compound Scaling في EfficientNet وليه أفضل من تكبير بُعد واحد بس.
4. ليه AlexNet كانت نقطة تحول في تاريخ الـ Deep Learning؟
5. رتّب المعماريات اللي اتكلمنا عنها من الأقدم للأحدث واذكر أهم فرق في كل واحدة.

---

<a name="part6"></a>
## 6️⃣ الجزء السادس: Transfer Learning في الـ CNNs

### 🔹 ما هو الـ Transfer Learning؟

هي تقنية بناخد فيها موديل **متدرب بالفعل** على داتا ضخمة (زي ImageNet)، ونعمله **Fine-tune** على الداتا الجديدة بتاعتنا، بدل ما ندرب CNN من الصفر.

### 🔹 ليه نستخدمه؟

- **توفير وقت وموارد**: مش محتاج تدرب شبكة عميقة من الصفر (ده ممكن ياخد أيام على GPU قوية)
- **مفيد جدًا مع الداتا الصغيرة**: لو عندك آلاف الصور بس مش ملايين
- **الاستفادة من الـ features المتعلّمة**: الطبقات الأولى بتتعلم أنماط عامة (حواف، textures)، والطبقات العميقة بتتعلم تفاصيل خاصة بالمهمة

### 🔹 إزاي بيشتغل؟

**1) Feature Extraction**
- تستخدم الـ CNN المتدرب كـ **مستخرج features ثابت**
- تشيل الـ Fully Connected layers الأصلية وتضيف طبقات جديدة خاصة بمهمتك
- مثال: استخدام Convolutional layers بتاعة VGG16 مع داتا طبية جديدة

**2) Fine-Tuning**
- تعمل "فك تجميد" (unfreeze) لبعض الطبقات العميقة وتعيد تدريبها على الداتا الجديدة
- مثال: Fine-tuning آخر طبقات ResNet50 لمهمة تصنيف سيارات

### 🔹 امتى تعمل Freeze وامتى تعمل Unfreeze؟

| الحالة | الاستراتيجية |
|---|---|
| **داتا صغيرة (آلاف الصور)** | جمّد الطبقات المبكرة (بتاخد features عامة)، درّب الـ FC layers بس |
| **مجالات متشابهة** (كلاب → قطط) | جمّد معظم الطبقات إلا آخر كام Conv layer |
| **داتا كبيرة (مئات الآلاف)** | فك تجميد أكتر طبقات (mid + high level) تدريجيًا |
| **مجالات مختلفة تمامًا** (أشعة طبية → صور عادية) | فك تجميد الشبكة كاملة، لكن بـ learning rate منخفض عشان تتجنب الـ "catastrophic forgetting" |

### 🔹 اختيار المعمار المناسب حسب الحالة

| الحالة | أفضل اختيار | تجنّب |
|---|---|---|
| داتا صغيرة، أنماط بسيطة | LeNet-5، CNN بسيطة (2-3 conv layers)، Pretrained (Feature Extraction) | شبكات عميقة (ResNet, EfficientNet-B7) |
| داتا متوسطة | VGG-16/19، ResNet-34/50، EfficientNet-B0/B1 | موديلات ضخمة جدًا (ResNet-101+) |
| داتا كبيرة جدًا (ملايين) | ResNet-101/152، EfficientNet-B5-B7، InceptionV3، Vision Transformers | موديلات صغيرة (LeNet) |
| صور دقة عالية (طبية/أقمار صناعية) | EfficientNet-B3-B7، ResNet-50/ResNeXt، UNet/Mask R-CNN (segmentation) | شبكات ضحلة (VGG, LeNet) |
| تطبيقات Real-time (موبايل/edge) | MobileNetV2/V3، EfficientNet-B0/B1، YOLO/SSD | موديلات ثقيلة (VGG, ResNet-152) |

### ❓ أسئلة انترفيو محتملة — الجزء السادس

1. ما الفرق بين Feature Extraction و Fine-Tuning في الـ Transfer Learning؟
2. ليه بنستخدم learning rate منخفض جدًا عند عمل Fine-tuning على مجال مختلف تمامًا؟
3. لو عندك 2000 صورة بس لمشروعك، هتختار تدرب CNN من الصفر ولا تستخدم Transfer Learning؟ وليه؟
4. إيه معنى "catastrophic forgetting" وإزاي بنتجنبه؟
5. إمتى تختار MobileNet بدل ResNet؟

---

<a name="summary"></a>
## 📝 خلاصة السيشن

| الموضوع | أهم نقطة تفتكرها |
|---|---|
| Output Layer | Regression = Linear, Binary = Sigmoid, Multi-class = Softmax |
| Activation Functions | ReLU هي المعيار في الـ hidden layers دلوقتي (بتحل Vanishing Gradient) |
| Softmax | بتحوّل القيم لاحتمالات مجموعها = 1 عن طريق الـ exponential |
| CNN Structure | Conv → ReLU → Pooling → Flatten → Dense |
| Convolution | بيستخرج features تلقائيًا باستخدام filters |
| Pooling | بيقلل الأبعاد ويحافظ على المعلومة المهمة |
| المعماريات | LeNet-5 → AlexNet → VGGNet → ResNet → EfficientNet (تطور تاريخي وتقني) |
| ResNet | حلّت مشكلة العمق بالـ Skip Connections |
| EfficientNet | بتكبّر Depth + Width + Resolution مع بعض (Compound Scaling) |
| Transfer Learning | استخدام موديل متدرب بدل التدريب من الصفر — يوفر وقت ومناسب للداتا الصغيرة |

---

*تم إعداد هذا الملف كمرجع شامل لمحتوى Session 3 — Deep Learning with Keras and TensorFlow (Convolutional Neural Networks).*