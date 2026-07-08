# 🔥 Session 4 — إعادة بناء الموديلات بـ PyTorch (Breast Cancer + Car Purchasing)

## 📌 مقدمة السيشن

في الـ Session 3 بنينا موديل الـ Regression بتاع `car_purchasing` باستخدام **Keras/TensorFlow**، وكانت الفلسفة إن كل حاجة (بناء الطبقات، الـ training loop، الـ optimizer) بتتعمل تلقائيًا جوه `model.fit()`.

في السيشن دي، بناخد **نفس المشكلتين** (breast cancer classification + car purchasing regression) ونعيد بناءهم من الصفر بـ **PyTorch**، وده هيفرق معاك جدًا لأن PyTorch مش بيخبي أي حاجة عنك — إنت اللي بتكتب الـ training loop بإيدك، وده بيدّيك تحكم كامل وفهم أعمق لإيه اللي بيحصل فعليًا جوه أي شبكة عصبية.

الملف ده هيشرحلك **أول حاجة إزاي PyTorch شغالة وإيه الـ building blocks بتاعتها**، وبعدين هنطبق الكلام ده على الموديلين اللي بنيتهم بالظبط في الـ notebook بتاعك.

---

## 📚 جدول المحتويات

1. [الجزء الأول: PyTorch إيه، وليه مختلفة عن Keras](#part1)
2. [الجزء الثاني: البنية العامة لأي مشروع PyTorch (Building Blocks)](#part2)
3. [الجزء الثالث: شرح تفصيلي لموديل Breast Cancer (Classification)](#part3)
4. [الجزء الرابع: شرح تفصيلي لموديل Car Purchasing (Regression)](#part4)
5. [الجزء الخامس: مقارنة بين الموديلين](#part5)
6. [خلاصة السيشن](#summary)

---

<a name="part1"></a>
## 1️⃣ الجزء الأول: PyTorch إيه، وليه مختلفة عن Keras

### 🔹 الفرق الجوهري في الفلسفة

| النقطة | Keras/TensorFlow | PyTorch |
|---|---|---|
| بناء الموديل | `Sequential()` + `.add()` — تصريحي (Declarative) | Class بترث من `nn.Module` — برمجي (Imperative) |
| التدريب | `model.fit()` — كل حاجة تلقائية | Training Loop بتكتبه إنت بإيدك (for loop) |
| حساب الـ Gradients | تلقائي جوه `.fit()` | `loss.backward()` — إنت اللي بتستدعيها |
| تحديث الأوزان | تلقائي | `optimizer.step()` — إنت اللي بتستدعيها |
| مرونة التعديل | أقل (خصوصًا في معماريات معقدة) | أعلى بكتير (كل خطوة تحت سيطرتك) |

> 💡 **الخلاصة**: Keras بتقولك "قولّي المعمار وأنا هدرب لك الموديل تلقائيًا". PyTorch بتقولك "دي كل الأدوات، وإنت اللي هتحدد إزاي تستخدمها خطوة بخطوة".

الفرق ده هو اللي خلانا نضطر — زي ما هتلاحظ في الكود — نكتب الـ **training loop يدويًا** بدل سطر واحد زي `model.fit(...)`.

### ❓ أسئلة انترفيو محتملة — الجزء الأول

1. ما الفرق الأساسي بين الـ Imperative style (PyTorch) والـ Declarative style (Keras)؟
2. ليه PyTorch بتُفضّل أكتر في الأبحاث (Research) بينما Keras بتُفضّل في التطبيقات السريعة (Production/Prototyping)؟
3. إيه معنى إن PyTorch بتستخدم Dynamic Computation Graph مقارنة بـ Static Graph؟

---

<a name="part2"></a>
## 2️⃣ الجزء الثاني: البنية العامة لأي مشروع PyTorch

أي مشروع PyTorch — أيًا كان نوعه (Regression أو Classification) — بيمر بنفس الخطوات السبعة دي بالظبط:

```
1. تجهيز البيانات (Tensors)
        ↓
2. تغليفها في Dataset + DataLoader
        ↓
3. بناء المعمار (Class ترث من nn.Module)
        ↓
4. تحديد Loss Function + Optimizer
        ↓
5. كتابة Training Loop يدويًا
        ↓
6. التقييم (Evaluation) على بيانات الاختبار
        ↓
7. حساب المقاييس (Metrics)
```

هنشرح كل خطوة بالتفصيل، ولية موجودة، بمعزل عن أي موديل معين — وبعدين هنطبقها على الموديلين.

---

### 🔹 الخطوة 1: تحويل البيانات إلى Tensors

PyTorch مش بيتعامل مع NumPy arrays أو Pandas DataFrames مباشرة أثناء التدريب — لازم تتحول لـ **Tensor**، وهو ببساطة "NumPy array لكن قادر يحسب Gradients ويشتغل على الـ GPU".

```python
X_train_tensor = torch.FloatTensor(X_train)
y_train_tensor = torch.FloatTensor(y_train).reshape(-1, 1)
```

| السطر | ليه محتاجينه |
|---|---|
| `torch.FloatTensor(...)` | تحويل الـ array لـ Tensor من نوع float32 (النوع الافتراضي لأوزان الشبكة) |
| `.reshape(-1, 1)` | الـ target (y) بيكون شكله `(n,)` في الأصل، لازم نحوّله لـ `(n, 1)` عشان يطابق شكل الـ output اللي الموديل هيطلعه (عمود واحد) |

> ⚠️ **ملاحظة مهمة**: لو نسيت الـ `reshape` هيحصل **Broadcasting Error** صامت — يعني الكود هيشتغل من غير Error واضح، لكن الـ Loss هتتحسب غلط لأن الأبعاد مش متطابقة (`(n,)` vs `(n,1)`).

---

### 🔹 الخطوة 2: Dataset + DataLoader

```python
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
```

| المكوّن | وظيفته |
|---|---|
| **`TensorDataset`** | بيربط الـ X والـ y مع بعض في كائن واحد، بحيث كل عنصر فيه هو زوج `(x_i, y_i)` |
| **`DataLoader`** | بيقسّم الداتا لـ **Batches** (دفعات صغيرة) تلقائيًا، ويعمل shuffle لها، وبيدّيك إياها Batch وراء التاني في الـ training loop |

**ليه بنستخدم Batches بدل ما ندرب على كل الداتا مرة واحدة؟**
- **الأداء**: تحديث الأوزان كل Batch بدل ما نستنى كل الداتا (Full Batch) → تعلّم أسرع
- **الذاكرة**: لو الداتا كبيرة جدًا مش هتتحمّل في الـ Memory دفعة واحدة
- **Generalization**: الـ Randomness في الـ shuffle بتساعد الموديل ميحفظش الترتيب ويتعلم الأنماط الحقيقية

`batch_size=16` يعني كل مرة الموديل هيشوف 16 عينة بس، يحسب الخطأ عليهم، يحدّث الأوزان، وبعدين ياخد الـ 16 اللي بعدهم — لحد ما يخلّص كل الداتا (ده اسمه **Epoch واحد**).

`shuffle=True` بيخلط ترتيب العينات في كل Epoch عشان الموديل ميتعودش على ترتيب معين.

---

### 🔹 الخطوة 3: بناء المعمار — `nn.Module`

ده **قلب** أي موديل PyTorch. أي شبكة عصبية بتتبني كـ Class بترث من `nn.Module`، وفيها دالتين أساسيتين:

```python
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        # تعريف الطبقات هنا
        self.fc1 = nn.Linear(input_size, hidden_size)
        ...

    def forward(self, x):
        # إزاي البيانات بتتحرك جوه الطبقات
        x = self.relu(self.fc1(x))
        ...
        return x
```

| الجزء | وظيفته |
|---|---|
| **`__init__`** | هنا بس بتعرّف (تحجز) الطبقات اللي هتستخدمها — زي ما تجهّز الأدوات قبل ما تشتغل. الترتيب هنا **مش مهم** |
| **`super().__init__()`** | لازم تتنادى الأول عشان تفعّل كل خصائص الـ `nn.Module` الأساسية (زي تتبع الـ parameters) — من غيرها الموديل مش هيشتغل صح |
| **`forward`** | هنا بيتحدد **الترتيب الفعلي** اللي البيانات بتمر بيه جوه الطبقات. دي اللي بتتنفذ فعليًا لما تكتب `model(x)` |
| **`nn.Linear(in, out)`** | طبقة Fully Connected — بتاخد `in` مدخلات وتطلع `out` مخرجات، وبتحسب `y = xW^T + b` |

> 💡 **ليه فصلنا `__init__` عن `forward`؟**
> `__init__` بيقول "دي الأدوات المتاحة عندي" (زي ما تجهّز عدة سباكة)، و`forward` بيقول "هستخدم الأدوات دي بالترتيب ده" (زي ما تنفّذ الشغل فعليًا). الفصل ده بيدّيك مرونة — ممكن تستخدم نفس الطبقة أكتر من مرة في `forward`، أو تغيّر تدفق البيانات من غير ما تغيّر تعريف الطبقات.

**استدعاء الموديل:**
```python
model = car_purchasing_model()
```
ده بينادي `__init__` وبيجهّز الطبقات بأوزان عشوائية ابتدائية.

```python
pred = model(xb)
```
ده بينادي `forward` تلقائيًا (PyTorch بتستخدم `__call__` اللي بينادي `forward` من وراك).

**فحص الأوزان:**
```python
for name, param in model.named_parameters():
    print(name)
```
بيطبعلك أسماء كل الـ parameters (weights + biases) في كل طبقة — مفيد للتأكد إن المعمار اتبنى صح.

---

### 🔹 الخطوة 4: Loss Function + Optimizer

```python
criterion = nn.MSELoss()          # أو nn.BCELoss() للـ classification
optimizer = torch.optim.Adam(model.parameters())
```

| المكوّن | وظيفته |
|---|---|
| **`criterion` (Loss Function)** | بيقيس "قد إيه توقع الموديل غلط" مقارنة بالقيمة الحقيقية |
| **`optimizer`** | الخوارزمية اللي بتحدّث الأوزان عشان تقلل الـ Loss (هنا Adam) |
| **`model.parameters()`** | بيدّي للـ optimizer كل الأوزان والـ biases القابلة للتدريب في الموديل عشان يعرف يحدّث مين بالظبط |

اختيار الـ Loss Function بيبقى حسب نوع المشكلة:

| نوع المشكلة | Loss Function |
|---|---|
| Regression | `nn.MSELoss()` |
| Binary Classification | `nn.BCELoss()` (لازم الـ output يكون بعد Sigmoid) |
| Multi-class Classification | `nn.CrossEntropyLoss()` (بياخد Logits مباشرة من غير Softmax) |

---

### 🔹 الخطوة 5: Training Loop — أهم جزء في PyTorch

ده الجزء اللي في Keras بيتم في سطر واحد (`model.fit()`)، وهنا بنكتبه يدويًا:

```python
epochs = 100
for epoch in range(epochs):
    for xb, yb in train_loader:
        pred = model(xb)              # 1. Forward Pass
        loss = criterion(pred, yb)    # 2. حساب الـ Loss
        optimizer.zero_grad()         # 3. تصفير الـ Gradients القديمة
        loss.backward()               # 4. Backward Pass (حساب الـ Gradients)
        optimizer.step()              # 5. تحديث الأوزان
```

خلّينا نفكك كل سطر — دي أهم 5 أسطر في PyTorch كلها:

| السطر | إيه اللي بيحصل بالظبط |
|---|---|
| **`pred = model(xb)`** | **Forward Pass**: الداتا بتعدي جوه الطبقات (زي ما اتحدد في `forward`) وبيطلع التوقع |
| **`loss = criterion(pred, yb)`** | بيقارن التوقع بالقيمة الحقيقية ويطلع رقم واحد يمثل "حجم الخطأ" |
| **`optimizer.zero_grad()`** | ⚠️ **خطوة حرجة**: PyTorch بيراكم (accumulate) الـ Gradients تلقائيًا افتراضيًا. لو ما صفّرتهاش، الـ gradients من الـ batch اللي فات هتتجمع مع الجديدة وتبوّظ التدريب |
| **`loss.backward()`** | **Backward Pass**: هنا بيتحسب مشتقة الـ Loss بالنسبة لكل weight في الموديل (Backpropagation) تلقائيًا عن طريق **Autograd** |
| **`optimizer.step()`** | بياخد الـ Gradients اللي اتحسبت وبيحدّث كل الأوزان فعليًا بناءً على خوارزمية Adam |

> 💡 **ليه الترتيب ده بالظبط مهم؟**
> لازم `zero_grad()` تيجي قبل `backward()` (عشان متراكمش gradients قديمة)، و`backward()` لازم تيجي قبل `step()` (عشان يكون فيه gradients أصلاً يتحدّث بيها). لو غيّرت الترتيب هيحصل خطأ منطقي (مش بالضرورة Error في الكود، لكن التدريب هيبقى غلط).

**طباعة الـ Loss كل 10 Epochs:**
```python
if (epoch+1) % 10 == 0:
    print(f"Epoch: {epoch+1}/{epochs} | Loss: {loss.item():.4f}")
```
`.item()` بتحوّل الـ Tensor (اللي فيه رقم واحد بس) لرقم Python عادي عشان تقدر تطبعه بشكل نضيف.

---

### 🔹 الخطوة 6: التقييم — `model.eval()` و `torch.no_grad()`

```python
model.eval()
with torch.no_grad():
    predictions = model(X_test_tensor)
```

| السطر | ليه محتاجينه |
|---|---|
| **`model.eval()`** | بيحوّل الموديل لوضع "التقييم" — مهم جدًا لو عندك طبقات زي `Dropout` أو `BatchNorm` بتتصرف مختلف وقت التدريب عن وقت الاختبار (في الموديلين بتوعنا مفيش منهم، لكنها Best Practice تتكتب دايمًا) |
| **`torch.no_grad()`** | بيقفل حساب الـ Gradients مؤقتًا — لأننا مش هندرب دلوقتي، بس بنعمل توقع. ده بيوفر ذاكرة ويسرّع الحساب |

---

### ❓ أسئلة انترفيو محتملة — الجزء الثاني

1. ليه لازم نستخدم `optimizer.zero_grad()` قبل كل `backward()`؟ إيه اللي هيحصل لو نسيتها؟
2. اشرح الفرق بين `__init__` و`forward` في `nn.Module`.
3. إيه وظيفة `DataLoader` ولية بنستخدم `batch_size` بدل ما ندرب على كل الداتا مرة واحدة؟
4. إيه معنى `torch.no_grad()` ولية بنستخدمها وقت التقييم بس؟
5. إيه الفرق بين `nn.MSELoss()` و`nn.BCELoss()`، ومتى تستخدم كل واحدة؟
6. إيه اللي بيحصل تقنيًا لما بننادي `loss.backward()`؟ (تلميح: Autograd + Chain Rule)

---

<a name="part3"></a>
## 3️⃣ الجزء الثالث: موديل Breast Cancer (Classification)

ده أول موديل — الهدف منه التنبؤ إذا كان الورم **Malignant (خبيث)** أو **Benign (حميد)** — يعني **Binary Classification**.

### 🔹 الفرق عن الـ Regression من البداية

```python
X = df.iloc[:, 2:]   # كل الأعمدة من الثالث لآخر عمود (الـ 30 feature)
y = df.iloc[:, 1]    # عمود الـ diagnosis (0 أو 1)
```

لاحظ إن العمود التاني (`diagnosis`) هو الـ target مش الأخير، لأن العمود الأول كان `id` (بيتشال). الداتا هنا أصلاً متحولة لأرقام (0/1) من قبل، عكس الـ car_purchasing اللي كان الـ target قيمة مستمرة.

### 🔹 تجهيز البيانات: StandardScaler مش MinMaxScaler

```python
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

| نقطة مهمة جدًا | التفاصيل |
|---|---|
| **`fit_transform` على Train بس** | الـ Scaler بيتعلم الـ mean والـ std **من بيانات التدريب فقط** |
| **`transform` بس (من غير fit) على Test** | بنستخدم نفس الـ mean/std اللي اتعلمها من الـ Train، عشان منعملش **Data Leakage** — لو عملنا `fit_transform` على الـ Test كمان، الموديل هيكون "شاف" معلومات إحصائية عن بيانات مفروض يكون عمره ما شافها |
| **`StandardScaler` هنا مش `MinMaxScaler`** | `StandardScaler` بيحوّل البيانات لمتوسط=0 وانحراف معياري=1 (بدل ما يحصرها بين 0 و1). بيتفضّل غالبًا مع الـ features اللي فيها Outliers، وهو الشائع أكتر في مشاكل الـ Classification الطبية |

> ⚠️ ملحوظة: في الكود الأصلي `X_train, X_test` بيتعملهم Scale لكن **`y` (الـ target) متعملوش reshape ولا Scale** — لأنه أصلاً 0/1 (Binary)، عكس الـ Regression اللي كان لازم نعمل `.reshape(-1, 1)` للـ y.

### 🔹 معمار الموديل

```python
class breast_cancer_model(nn.Module):
    def __init__(self):
        super(breast_cancer_model, self).__init__()
        self.fc1 = nn.Linear(30, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x
```

| الطبقة | Input → Output | الـ Activation |
|---|---|---|
| `fc1` | 30 → 64 | ReLU |
| `fc2` | 64 → 32 | ReLU |
| `fc3` (Output) | 32 → 1 | **Sigmoid** |

**ليه 30 في أول طبقة؟** لأن عدد الـ features في داتا breast cancer هو 30 عمود (بعد ما شلنا `id` و`diagnosis`).

**ليه Sigmoid في الآخر؟** لأنها **Binary Classification** — محتاجين قيمة بين 0 و1 تمثل احتمال إن الورم خبيث. ده بالظبط زي ما اتفقنا في Session 3: *Binary Classification = 1 neuron + Sigmoid*.

> 💡 قارن ده بموديل الـ Regression: هناك آخر طبقة (`fc3`) **من غير أي activation** خالص، لأن الهدف رقم حر مش احتمال محصور بين 0 و1.

### 🔹 الـ Loss المستخدم: BCELoss

```python
criterion = nn.BCELoss()  # Binary Cross Entropy
```

**BCE (Binary Cross Entropy)** هي الـ Loss المناسبة للـ Binary Classification. المعادلة:

$$BCE = -\frac{1}{N}\sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i) \right]$$

**الفكرة**: لو الموديل واثق وصح (مثلاً توقع 0.95 والحقيقي 1) → Loss صغيرة جدًا. لو الموديل واثق وغلط (توقع 0.95 والحقيقي 0) → Loss كبيرة جدًا (بتتصاعد لوغاريتميًا). ده بيخلي الموديل "يتعاقب" بشدة على الثقة الزايدة الغلط.

> ⚠️ **شرط أساسي لاستخدام `BCELoss`**: لازم يكون فيه **Sigmoid قبلها** في آخر طبقة (زي ما عملنا بالظبط في الموديل)، لأنها بتتوقع إن المدخلات ليها قيمة بين 0 و1. لو استخدمت `nn.BCEWithLogitsLoss()` بدلها، مكانش هيبقى لازم Sigmoid في الموديل، لأنها بتعمل Sigmoid جواها تلقائيًا (وأكتر استقرارًا رقميًا).

### 🔹 التدريب

```python
epochs = 50
for epoch in range(epochs):
    for xb, yb in train_loader:
        pred = model(xb)
        loss = criterion(pred, yb)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if (epoch+1) % 10 == 0:
        print(f"Epoch: {epoch+1}/{epochs} | Loss: {loss.item():.4f}")
```

نفس الخمس خطوات اللي شرحناها في الجزء الثاني بالظبط — بس هنا عدد الـ epochs أقل (50) لأن مشكلة الـ Classification دي أبسط نسبيًا وبتتقارب أسرع.

### 🔹 حاجات ناقصة ومهم تضيفها (اختياري)

الكود اللي بعتهولي واقف عند التدريب من غير تقييم. عشان تكمّل نفس منهجية موديل الـ Regression، تقدر تضيف:

```python
model.eval()
with torch.no_grad():
    y_pred_prob = model(X_test_tensor)
    y_pred = (y_pred_prob >= 0.5).float()   # تحويل الاحتمال لقرار 0/1

from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_test_tensor, y_pred))
print(classification_report(y_test_tensor, y_pred))
```

**ليه `>= 0.5`؟** لأن الـ Sigmoid بتطلع احتمال، ومحتاجين **threshold** (عتبة قرار) نحوّل بيه الاحتمال لفئة نهائية (0 أو 1). الـ 0.5 هو الافتراضي، لكن ممكن تغيّره حسب المشكلة (مثلاً لو مهم جدًا ميفوتناش أي حالة خبيثة، ممكن تنزل الـ threshold عن 0.5).

### ❓ أسئلة انترفيو محتملة — الجزء الثالث

1. ليه استخدمنا `StandardScaler` هنا و`fit` بس على الـ Train؟
2. ليه لازم يكون فيه Sigmoid قبل `BCELoss`؟ إيه البديل اللي مش محتاج Sigmoid يدوي؟
3. إزاي تحوّل ناتج الـ Sigmoid (احتمال) لقرار نهائي (0 أو 1)؟
4. إيه الفرق بين `BCELoss` و`CrossEntropyLoss`؟ استخدم كل واحدة إمتى؟
5. لو الداتا Imbalanced (مثلاً 90% حميد و10% خبيث)، إيه المشاكل اللي ممكن تواجهك وإزاي تتعامل معاها؟

---

<a name="part4"></a>
## 4️⃣ الجزء الرابع: موديل Car Purchasing (Regression)

ده تكرار لنفس موديل الـ Regression بتاع Session 3، لكن بـ PyTorch بدل Keras.

### 🔹 تجهيز البيانات

```python
X = df.iloc[:, 3:-1]
y = df.iloc[:, -1]

xsc = StandardScaler()
X = xsc.fit_transform(X)
ysc = StandardScaler()
y = ysc.fit_transform(y.values.reshape(-1, 1))
```

| نقطة | التفاصيل |
|---|---|
| **Scaler منفصل لكل من X و y** (`xsc`, `ysc`) | مهم جدًا نحتفظ بالـ `ysc` لوحده، عشان بعد التدريب هنحتاج نرجّع التوقعات لمقياسها الأصلي (بالدولار) باستخدام `ysc.inverse_transform()` |
| **`StandardScaler` بدل `MinMaxScaler`** | مختلف عن اللي استخدمناه في Session 3 (كان MinMaxScaler) — هنا التجربة استخدمت StandardScaler، وده اختيار تصميمي (design choice) ممكن يجرب الاتنين ويقارن النتائج |
| **`y.values.reshape(-1, 1)`** | لازم قبل الـ scaling برضو، لأن `StandardScaler` بيحتاج شكل 2D `(n_samples, n_features)` مش 1D array |

> ⚠️ لاحظ هنا حاجة مختلفة عن موديل الـ breast cancer: هنا استخدمنا `fit_transform` على **كل الداتا X كلها قبل الـ split** (مش بعده). ده بيُعتبر أقل صرامة من ناحية منع الـ Data Leakage مقارنة بموديل الـ breast cancer اللي عمل split الأول وبعدين fit على Train بس. لو حابب تحسّن الكود، الأفضل تعمل split الأول وبعدين `fit_transform` على Train و`transform` بس على Test — بالظبط زي ما عملت في موديل الـ classification.

### 🔹 تحويل الـ Tensors (من غير `.reshape` إضافي هنا)

```python
X_train_tensor = torch.FloatTensor(X_train)
X_test_tensor = torch.FloatTensor(X_test)
y_train_tensor = torch.FloatTensor(y_train)
y_test_tensor = torch.FloatTensor(y_test)
```

هنا مفيش `.reshape(-1, 1)` زي ما شرحنا في الجزء الثاني، **لأنها اتعملت بالفعل قبل كده** جوه سطر الـ Scaling (`y.values.reshape(-1, 1)`)، فالـ `y` بقى أصلاً بشكل `(n, 1)` قبل ما يتحول لـ Tensor.

### 🔹 DataLoader لـ Train و Test مع بعض

```python
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)
```

**ليه `shuffle=False` في الـ test_loader؟** لأن الترتيب مش مهم وقت التقييم (مفيش تدريب هيحصل)، وأحيانًا بيكون مهم تحافظ على الترتيب الأصلي عشان تقارن التوقعات بالقيم الحقيقية بنفس الترتيب لو هتعمل تحليل لاحقًا.

### 🔹 معمار الموديل + `set_deterministic_state`

```python
class car_purchasing_model(nn.Module):
    def __init__(self):
        super(car_purchasing_model, self).__init__()
        self.fc1 = nn.Linear(5, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        a1 = self.relu(self.fc1(x))
        a2 = self.relu(self.fc2(a1))
        yhat = self.fc3(a2)
        return yhat

set_deterministic_state(42)
model = car_purchasing_model()
```

| الطبقة | Input → Output | الـ Activation |
|---|---|---|
| `fc1` | 5 → 64 | ReLU |
| `fc2` | 64 → 32 | ReLU |
| `fc3` (Output) | 32 → 1 | **من غير activation (Linear)** |

**ليه 5 في أول طبقة؟** عدد الـ features بتاع car_purchasing بعد ما شلنا الاسم والإيميل والدولة (gender, age, annual salary, credit card debt, net worth).

**ليه من غير activation في الآخر؟** بالظبط زي Session 3 — الـ Regression محتاجة رقم حر (السعر بالدولار)، مش محصور بين 0 و1 أو موجب بس.

**`set_deterministic_state(42)`**: الدالة دي (اللي اتعرفت فوق في الـ notebook) بتثبّت كل مصادر العشوائية (Python, NumPy, PyTorch CPU/GPU) عشان لو شغّلت الكود تاني تاخد **نفس النتائج بالظبط**. مهم جدًا وقت المقارنة بين تجارب مختلفة أو الـ debugging.

### 🔹 التدريب

```python
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())

epochs = 100
for epoch in range(epochs):
    for xb, yb in train_loader:
        pred = model(xb)
        loss = criterion(pred, yb)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if (epoch+1) % 10 == 0:
        print(f"Epoch: {epoch+1}/{epochs} | Loss: {loss.item():.4f}")
```

نفس الـ 5 خطوات، لكن هنا `MSELoss` بدل `BCELoss` لأنها Regression مش Classification. وعدد الـ epochs أعلى (100) — كل مشكلة بتحتاج تجريب لعدد epochs مختلف.

### 🔹 التقييم والرجوع للمقياس الأصلي

```python
model.eval()
with torch.no_grad():
    predictions = model(X_test_tensor).numpy()
    true = y_test_tensor.numpy()
    predictions = ysc.inverse_transform(predictions)
    true = ysc.inverse_transform(true)
```

**نقطة جوهرية**: التوقعات والقيم الحقيقية اتعملهم Scale قبل التدريب (متوسط=0، انحراف=1)، فلو حسبنا الـ Error عليهم كده هيكون رقم بلا معنى (مش بالدولار). عشان كده لازم:

```python
ysc.inverse_transform(...)
```

يرجّع القيم لمقياسها الأصلي بالدولار **قبل** حساب أي Metric — ده أساسي عشان تقدر تفهم وتفسّر النتائج بمعنى حقيقي (مثلاً "الموديل بيغلط بمقدار 3000 دولار في المتوسط" بدل رقم مطبّع بلا معنى).

### 🔹 الرسم والمقاييس

```python
plt.plot(true, label='Actual')
plt.plot(predictions, label='Predicted')
```

رسم بياني بيقارن القيم الحقيقية بالتوقعات — كل ما الخطين قريبين من بعض، كل ما الموديل أدق.

```python
mse = mean_squared_error(true, predictions)
mae = mean_absolute_error(true, predictions)
mape = mean_absolute_percentage_error(true, predictions)
```

| Metric | المعنى |
|---|---|
| **MSE** | متوسط مربع الفرق — بيعاقب الأخطاء الكبيرة بشدة |
| **MAE** | متوسط الفرق المطلق — بنفس وحدة الـ target (دولار) وأسهل تفسيرًا |
| **MAPE** | متوسط النسبة المئوية للخطأ — مفيدة لمقارنة أداء الموديل بمعزل عن حجم الأرقام |

### ❓ أسئلة انترفيو محتملة — الجزء الرابع

1. ليه لازم نعمل `ysc.inverse_transform()` قبل ما نحسب MSE/MAE؟ إيه اللي هيحصل لو حسبناهم على البيانات الـ Scaled مباشرة؟
2. ليه محتاجين `ysc` منفصل عن `xsc`؟
3. إيه فايدة `set_deterministic_state`؟ إيه اللي ممكن يحصل لو ما استخدمناهاش؟
4. ليه هنا استخدمنا `MSELoss` مش `BCELoss`؟
5. لو عايز تحسّن الكود من ناحية منع Data Leakage، إيه التعديل اللي تقترحه على ترتيب الـ split والـ scaling؟

---

<a name="part5"></a>
## 5️⃣ الجزء الخامس: مقارنة شاملة بين الموديلين

| النقطة | Breast Cancer (Classification) | Car Purchasing (Regression) |
|---|---|---|
| **نوع المشكلة** | Binary Classification | Regression |
| **عدد الـ Input Features** | 30 | 5 |
| **معمار الطبقات المخفية** | 64 → 32 | 64 → 32 (نفس الحجم!) |
| **آخر طبقة** | 1 neuron + **Sigmoid** | 1 neuron + **من غير activation** |
| **الـ Scaler** | `StandardScaler`، fit على Train بس | `StandardScaler`، لكن fit على كل X قبل الـ split |
| **الـ y محتاج Scaling؟** | ❌ لأ (أصلاً 0/1) | ✅ أيوه (قيمة مستمرة بالدولار) |
| **Loss Function** | `BCELoss` | `MSELoss` |
| **عدد الـ Epochs** | 50 | 100 |
| **التقييم** | Threshold (>= 0.5) + Confusion Matrix | MSE / MAE / MAPE + Inverse Transform |

### 🔹 القاعدة العامة اللي تفتكرها دايمًا

> **آخر طبقة في الموديل + الـ Loss Function بتتحدد حسب نوع المشكلة، مش حسب حجم الداتا أو عدد الـ features.**

```
Regression          → Linear output          + MSELoss
Binary Class.        → Sigmoid output         + BCELoss
Multi-class Class.   → Softmax (أو Linear)    + CrossEntropyLoss
```

باقي المعمار (عدد الطبقات، عدد الـ neurons) بيتحدد بالتجربة (Hyperparameter Tuning) مش بقاعدة ثابتة.

---

<a name="summary"></a>
## 📝 خلاصة السيشن

| الموضوع | أهم نقطة تفتكرها |
|---|---|
| فلسفة PyTorch | إنت اللي بتكتب الـ training loop يدويًا، عكس Keras اللي بيعمله تلقائي |
| `nn.Module` | `__init__` بيعرّف الطبقات، `forward` بيحدد ترتيب مرورها |
| الخمس خطوات المقدسة | `pred = model(x)` → `loss = criterion(...)` → `zero_grad()` → `backward()` → `step()` |
| `zero_grad()` | لازم قبل كل `backward()` عشان الـ gradients ميتراكموش من الـ batch اللي فات |
| `torch.no_grad()` | بيتستخدم وقت التقييم بس عشان يوفر ذاكرة وحساب |
| Data Leakage | لازم الـ Scaler يعمل `fit` على Train بس، و`transform` بس على Test |
| Classification vs Regression | آخر طبقة + الـ Loss بيتحددوا حسب نوع المشكلة (Sigmoid+BCE مقابل Linear+MSE) |
| `inverse_transform` | لازم قبل حساب أي Metric لو كنت عملت Scaling للـ target، عشان تقيّم الموديل بالوحدة الحقيقية |
| `set_deterministic_state` | بيضمن تكرار نفس النتائج في كل تشغيل للكود |

---

*تم إعداد هذا الملف كمرجع شامل لمحتوى Session 4 — Deep Learning with PyTorch (Breast Cancer Classification + Car Purchasing Regression).*