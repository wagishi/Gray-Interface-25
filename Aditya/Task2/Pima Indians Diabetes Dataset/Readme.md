# 🏪 Pima Indians Diabetes Classification

## 📌 Objective

To predict whether a patient has diabetes using diagnostic data like glucose level, insulin, BMI, age, etc. The dataset is sourced from the [UCI Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database).

---

## 🧹 Data Cleaning & Preprocessing

### ⚠ Handling Biologically Impossible Values

The following features had instances of 0 which are **not biologically valid**:

| Feature       | Zero Count |
| ------------- | ---------- |
| Glucose       | 5          |
| Insulin       | 374        |
| SkinThickness | 227        |
| BMI           | 11         |
| BloodPressure | 35         |

### 🔧 Imputation Strategy

* **Glucose, BMI, BloodPressure**:

  * Very few invalid values → Replaced with **median** of the entire column.

* **Insulin & SkinThickness**:

  * Many zero values → Replaced using **age-grouped median**:

    * Age groups: `21–30`, `31–40`, `41–50`, `51–60`, `61–70`, `71–81`
  * If a group's median was also 0 → used **overall column median** as fallback.

---

## ⚙️ Feature Scaling

Used **StandardScaler** to normalize features for better performance in distance-based models.

| Model                    | Scaling Effect            |
| ------------------------ | ------------------------- |
| Logistic Regression      | No significant change     |
| Random Forest Classifier | No significant change     |
| K-Nearest Neighbors      | ✅ Significant improvement |

---

## 🤖 Models Used

| Model                    | Accuracy  | Precision | Recall    | F1 Score  |
| ------------------------ | --------- | --------- | --------- | --------- |
| Logistic Regression      | 0.766     | 0.655     | 0.679     | 0.667     |
| Random Forest Classifier | **0.770** | **0.660** | **0.710** | **0.680** |
| K-Nearest Neighbors      | 0.760     | 0.667     | 0.655     | 0.661     |

✅ **Random Forest Classifier performed the best overall.**

---

## 🔍 Feature Importance (Random Forest)

Most influential features:

1. **Glucose**
2. **Insulin**
3. **Age**
4. **BMI**
5. **Blood Pressure**

---

## 🧪 Hyperparameter Tuning

* Tried tuning `RandomForest` model.
* Observation: **Hyperparameter tuning sometimes decreased performance** due to overfitting or inappropriate combinations.

---

## 💡 Why Did Random Forest Perform Better?

### 🌳 1. Strong Ensemble Power

* Random Forest averages multiple trees → reduces variance and overfitting.
* Handles **non-linear relationships** better than Logistic Regression.

### ⚖️ 2. Captures Feature Interactions

* Can learn relationships like: *"high glucose + low insulin → higher risk"*.
* Logistic Regression can't learn such combinations.

### 🤊 3. Not Affected by Feature Scale

* Unlike KNN and Logistic Regression, Random Forest doesn’t need feature scaling.

### 🌟 4. Robust to Outliers & Imputations

* Performs well despite the imputed zero-values in features like Insulin.

### 🧠 5. Handles Noise & Ranks Features

* Ignores irrelevant features naturally → reduces overfitting and enhances interpretability.

---

## 🔗 Google Colab Notebook

You can view and run the complete analysis on Google Colab:

👈 [Open in Colab](https://colab.research.google.com/drive/1CqmYi0SLOzZy5eQ3R1cn2yJlgLtstqiq?usp=sharing)

