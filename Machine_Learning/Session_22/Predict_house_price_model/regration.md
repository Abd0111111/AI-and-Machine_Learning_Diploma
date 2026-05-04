# Regression Models Guide

## 1. Linear Regression

### Import

```python
from sklearn.linear_model import LinearRegression
```

### Description

* Basic model
* Assumes linear relationship

### Advantages

* Simple
* Fast
* Easy to interpret

### Disadvantages

* Poor with non-linear data
* Sensitive to outliers

### When to use

* Data is linear
* Need baseline model

---

## 2. Ridge Regression

### Import

```python
from sklearn.linear_model import Ridge
```

### Description

* Adds L2 regularization

### Advantages

* Reduces overfitting
* Handles multicollinearity

### Disadvantages

* Does not remove features

### When to use

* Many correlated features

---

## 3. Lasso Regression

### Import

```python
from sklearn.linear_model import Lasso
```

### Description

* Adds L1 regularization

### Advantages

* Feature selection
* Reduces overfitting

### Disadvantages

* Can remove useful features

### When to use

* Need feature selection

---

## 4. ElasticNet

### Import

```python
from sklearn.linear_model import ElasticNet
```

### Description

* Combination of Ridge and Lasso

### Advantages

* Balanced regularization

### Disadvantages

* Needs tuning

### When to use

* Mixed feature behavior

---

## 5. Decision Tree Regressor

### Import

```python
from sklearn.tree import DecisionTreeRegressor
```

### Description

* Tree-based model

### Advantages

* Handles non-linearity
* Easy to visualize

### Disadvantages

* Overfitting risk

### When to use

* Non-linear data

---

## 6. Random Forest Regressor

### Import

```python
from sklearn.ensemble import RandomForestRegressor
```

### Description

* Ensemble of trees

### Advantages

* High accuracy
* Reduces overfitting

### Disadvantages

* Slower
* Less interpretable

### When to use

* General purpose

---

## 7. Gradient Boosting Regressor

### Import

```python
from sklearn.ensemble import GradientBoostingRegressor
```

### Description

* Sequential trees

### Advantages

* High performance

### Disadvantages

* Slow training

### When to use

* Need best accuracy

---

## 8. Support Vector Regression

### Import

```python
from sklearn.svm import SVR
```

### Description

* Margin-based model

### Advantages

* Works with small data

### Disadvantages

* Slow with large data

### When to use

* Small dataset

---

## 9. K-Nearest Neighbors Regressor

### Import

```python
from sklearn.neighbors import KNeighborsRegressor
```

### Description

* Distance-based model

### Advantages

* Simple

### Disadvantages

* Slow prediction

### When to use

* Small datasets

---

## Comparison Table

| Model             | Handles Non-linearity | Overfitting Risk | Speed  | Feature Selection |
| ----------------- | --------------------- | ---------------- | ------ | ----------------- |
| Linear Regression | No                    | Low              | Fast   | No                |
| Ridge             | No                    | Low              | Fast   | No                |
| Lasso             | No                    | Low              | Fast   | Yes               |
| ElasticNet        | No                    | Low              | Fast   | Partial           |
| Decision Tree     | Yes                   | High             | Medium | No                |
| Random Forest     | Yes                   | Low              | Medium | No                |
| Gradient Boosting | Yes                   | Medium           | Slow   | No                |
| SVR               | Yes                   | Medium           | Slow   | No                |
| KNN               | Yes                   | Medium           | Slow   | No                |
