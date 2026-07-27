# Brain Tumor MRI Classification — Model Comparison Report

**Project:** AUTO_CARE... *(placeholder — actual: Brain Tumor MRI 4-Class Classification)*
**Dataset:** [Brain Tumor MRI Dataset (Kaggle)](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
**Classes (4):** `glioma`, `meningioma`, `notumor`, `pituitary`
**Task:** Build & compare 3 models — (1) Vanilla CNN from scratch, (2) Transfer Learning (frozen), (3) Fine-tuned pretrained model.

---

## 📂 Dataset Summary

| Split | Images | Notes |
|---|---|---|
| Training | 4,760 | 224x224, balanced across 4 classes |
| Validation | 840 | held out from training set |
| Test | 1,600 | 400 per class |

---

## 🧠 Model 1: Vanilla CNN (From Scratch)

### Architecture
- 4 Convolutional blocks (channels: 32 → 64 → 128 → 256)
- 2 Fully Connected layers
- **Total parameters:** 422,788 (all trainable — no pretrained weights, no freezing)

### Training Setup
- **Epochs:** 20
- **Best epoch:** 19 (based on validation accuracy)
- **LR schedule:** started at 0.001, decayed to 0.00025 by epoch 18-20

### Results

| Metric | Value |
|---|---|
| Final Train Accuracy | 89.92% |
| Final Train Loss | 0.2782 |
| Best Validation Accuracy | 81.75% (epoch 19) |
| **Final Test Accuracy** | **81.75%** ⚠️ *(corrected — see note below)* |

> ⚠️ **Note on discrepancy:** the raw training log printed "Final Test Accuracy: 68.94%", but this value actually matches the *last epoch's validation accuracy* (epoch 20), not the true evaluation after reloading the best saved weights. The Confusion Matrix and Classification Report (computed on the actual test set with the best model) show accuracy = **81.75% / 82%**, which is the trustworthy figure. This looks like a logging bug in the training script — worth checking for Models 2 & 3 as well.

### Classification Report (Test Set)

| Class | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| glioma | 0.99 | 0.59 | 0.74 | 400 |
| meningioma | 0.71 | 0.74 | 0.72 | 400 |
| notumor | 0.82 | 0.97 | 0.89 | 400 |
| pituitary | 0.83 | 0.96 | 0.89 | 400 |
| **Accuracy** | | | **0.82** | 1600 |
| Macro avg | 0.84 | 0.82 | 0.81 | 1600 |
| Weighted avg | 0.84 | 0.82 | 0.81 | 1600 |

### Confusion Matrix (Test Set)

| True \ Pred | glioma | meningioma | notumor | pituitary |
|---|---|---|---|---|
| **glioma** | 237 | 101 | 37 | 25 |
| **meningioma** | 1 | 297 | 50 | 52 |
| **notumor** | 2 | 9 | 388 | 1 |
| **pituitary** | 0 | 14 | 0 | 386 |

### Observations
- Model achieves very high **precision on glioma (0.99)** but very low **recall (0.59)** — meaning when it predicts glioma it's almost always right, but it misses a lot of actual glioma cases (confuses them mostly with meningioma).
- `notumor` and `pituitary` classes are classified very well (recall 0.97 and 0.96).
- Training accuracy (89.92%) noticeably higher than test accuracy (81.75-82%) — some overfitting, expected for a from-scratch CNN without pretrained features.
- Validation accuracy was very unstable across epochs (jumping between ~46% and ~82%), suggesting the model/LR schedule could benefit from more regularization or a smoother LR decay.

---

## 🧠 Model 2: Transfer Learning — ResNet50 (Frozen Weights)

### Architecture
- **Backbone:** ResNet50, pretrained on ImageNet (1.2M images, 1000 classes), 50 layers with residual connections
- **Frozen:** entire backbone (23,508,032 params)
- **Trainable:** only the new final FC layer (8,196 params)
- **Total parameters:** 23,516,228

### Training Setup
- **Epochs:** 20
- **Best epoch:** 17-20 (val accuracy plateaus around 90.0-90.36%)
- **LR schedule:** 0.001 → 0.0005 (halved around epoch 14)

### Results

| Metric | Value |
|---|---|
| Final Train Accuracy | 92.54% |
| Final Train Loss | 0.2159 |
| Best Validation Accuracy | 90.36% |
| **Final Test Accuracy** | **87.38%** ✅ *(consistent with confusion matrix: 1398/1600)* |

> ✅ No discrepancy this time — the reported test accuracy matches the confusion matrix diagonal sum exactly (293+322+395+388 = 1398/1600 = 87.38%).

### Classification Report (Test Set)

| Class | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| glioma | 0.91 | 0.73 | 0.81 | 400 |
| meningioma | 0.80 | 0.81 | 0.80 | 400 |
| notumor | 0.87 | 0.99 | 0.92 | 400 |
| pituitary | 0.92 | 0.97 | 0.95 | 400 |
| **Accuracy** | | | **0.87** | 1600 |
| Macro avg | 0.88 | 0.87 | 0.87 | 1600 |
| Weighted avg | 0.88 | 0.87 | 0.87 | 1600 |

### Confusion Matrix (Test Set)

| True \ Pred | glioma | meningioma | notumor | pituitary |
|---|---|---|---|---|
| **glioma** | 293 | 68 | 34 | 5 |
| **meningioma** | 24 | 322 | 27 | 27 |
| **notumor** | 1 | 4 | 395 | 0 |
| **pituitary** | 3 | 9 | 0 | 388 |

### Observations
- Huge jump vs Model 1: test accuracy up from ~81.75% to **87.38%**, using only **8,196 trainable parameters** (vs 422,788 for the CNN from scratch) — this shows the power of pretrained ImageNet features even without any fine-tuning.
- Glioma recall improved a lot (0.59 → 0.73) but is still the weakest class — still gets confused with meningioma (68 cases) and notumor (34 cases).
- `notumor` (recall 0.99) and `pituitary` (recall 0.97) are near-perfect.
- Train/Val curves are much more stable than Model 1 (no wild oscillation), and the gap between train (92.5%) and val (90.4%) is small — healthier generalization, less overfitting than the scratch CNN.

---

## 🧠 Model 3: Fine-Tuned ResNet50

### Architecture & Strategy
- **Backbone:** ResNet50, pretrained on ImageNet
- **Frozen:** layer1-3
- **Fine-tuned (unfrozen):** layer4 + new FC head
- **Total parameters:** 24,033,604
- **Trainable parameters:** 15,490,308 (64.5% of total)

**Differential Learning Rates** (key design choice):
- `layer4` (pretrained, already good features) → LR = `1e-5` (gentle updates, avoid destroying learned features)
- `fc` head (new, random init) → LR = `1e-4` (needs to learn from scratch, faster)

### Training Setup
- **Epochs:** 15
- **Best epoch:** 13 (val accuracy 94.76%)
- **Test set:** evaluated only once at the very end (proper protocol — no leakage/no selection bias)

### Results

| Metric | Value |
|---|---|
| Final Train Accuracy | 97.73% |
| Final Train Loss | 0.0730 |
| Best Validation Accuracy | 94.76% (epoch 13) |
| **Final Test Accuracy** | **91.38%** ✅ *(consistent with confusion matrix: 1462/1600)* |

### Classification Report (Test Set)

| Class | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| glioma | 0.96 | 0.77 | 0.86 | 400 |
| meningioma | 0.86 | 0.92 | 0.89 | 400 |
| notumor | 0.88 | 0.98 | 0.93 | 400 |
| pituitary | 0.97 | 0.98 | 0.98 | 400 |
| **Accuracy** | | | **0.91** | 1600 |
| Macro avg | 0.92 | 0.91 | 0.91 | 1600 |
| Weighted avg | 0.92 | 0.91 | 0.91 | 1600 |

### Confusion Matrix (Test Set)

| True \ Pred | glioma | meningioma | notumor | pituitary |
|---|---|---|---|---|
| **glioma** | 308 | 50 | 40 | 2 |
| **meningioma** | 11 | 366 | 14 | 9 |
| **notumor** | 1 | 5 | 394 | 0 |
| **pituitary** | 0 | 6 | 0 | 394 |

### Observations
- Best model overall: **91.38% test accuracy**, clear improvement over both previous models.
- Glioma recall keeps improving across the 3 models: 0.59 → 0.73 → **0.77** — still the hardest class, still mainly confused with meningioma (50 cases) and notumor (40 cases), but the gap is closing.
- Pituitary is now almost perfect (0.97 precision, 0.98 recall).
- Train accuracy (97.73%) vs test accuracy (91.38%) shows more overfitting than Model 2 (frozen) — expected, since 15.5M parameters are being updated vs only 8,196. The differential LR strategy (tiny LR on layer4, higher LR on the head) successfully prevented catastrophic forgetting of the pretrained features while still improving on Model 2.
- Val accuracy peaked at epoch 13 (94.76%) then slightly declined (epoch 14-15) — mild sign of overfitting starting, correctly caught by saving best checkpoint instead of the last one.

---

## 📊 Final Comparison (All 3 Models)

| Model | Test Accuracy | Macro F1 | Trainable Params | Glioma Recall | Notes |
|---|---|---|---|---|---|
| Vanilla CNN (Scratch) | 81.75% | 0.81 | 422,788 (100%) | 0.59 | Weakest; unstable val curve, biggest train/test gap |
| ResNet50 Transfer Learning (Frozen) | 87.38% | 0.87 | 8,196 (0.03%) | 0.73 | Big jump w/ almost no trainable params; most stable curves |
| **ResNet50 Fine-tuned** | **91.38%** ✅ | **0.91** ✅ | 15,490,308 (64.5%) | **0.77** ✅ | **Best overall**; small extra overfitting vs frozen model |

### Accuracy Progression
```
Vanilla CNN (Scratch)  →  81.75%
Transfer Learning       →  87.38%   (+5.63 pts over scratch)
Fine-Tuned              →  91.38%   (+4.00 pts over frozen, +9.63 pts over scratch)
```

### Per-class Recall Across Models

| Class | Vanilla CNN | Frozen TL | Fine-tuned |
|---|---|---|---|
| glioma | 0.59 | 0.73 | 0.77 |
| meningioma | 0.74 | 0.81 | 0.92 |
| notumor | 0.97 | 0.99 | 0.98 |
| pituitary | 0.96 | 0.97 | 0.98 |

---

## 🏆 Conclusion

1. **Pretrained features matter a lot.** Just freezing a pretrained ResNet50 and training a tiny FC head (8,196 params) beat a full from-scratch CNN (422,788 params) by **+5.63 points** — proof that ImageNet features transfer well to medical MRI images, even though the domains look very different.

2. **Fine-tuning gives the best results.** Unfreezing `layer4` with a small learning rate (`1e-5`) on top of a higher-LR FC head (`1e-4`) pushed accuracy up another **+4.00 points** to **91.38%**, the best of the three models. The differential learning rate strategy was key — it let the model adapt deeper, task-specific features without destroying the general-purpose pretrained ones.

3. **Glioma is consistently the hardest class** for all three models (lowest recall/precision every time), most often confused with meningioma and notumor. This is a known challenge in this dataset (glioma boundaries can look visually similar to meningioma on MRI) and would be a good area for further work (e.g. more targeted augmentation, class-balanced loss, or ensembling).

4. **Recommended model:** the **Fine-tuned ResNet50** — best accuracy (91.38%), best macro F1 (0.91), and the best glioma recall of the three, at an acceptable cost of training more parameters and slightly more overfitting risk than the frozen model.

### Possible Next Steps
- Try unfreezing more layers (layer3+layer4) with even smaller LR to see if glioma recall improves further.
- Add stronger data augmentation (rotation, contrast) targeted at glioma/meningioma confusion.
- Try a different backbone (EfficientNet, DenseNet) for comparison.
- Use class-weighted loss to explicitly penalize glioma misclassification more.