# Task 3: Heart Disease Prediction System

## Overview

A machine learning project that predicts the likelihood of heart disease using Random Forest and SVM classifiers. The project includes data preprocessing, model training, SHAP-based explainability, and a Flask web interface for user interaction.

---
## Dataset
https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

---
## Source Code
https://colab.research.google.com/drive/1zy_OuV0m7_6T4gthwD_Co5EXPi_ngjUS?usp=sharing
---
## Libraries Used

- Python
- pandas, numpy
- scikit-learn
- SHAP (Shapley Additive Explanations)
- Flask
- matplotlib, seaborn
- joblib

---

## Workflow

1. **Exploratory Data Analysis (EDA)**  
   - Summary statistics, null counts, distributions, correlation matrix
   - Count plots & boxplots for visual insights
   - Handled 0s in 'RestingBP' and 'Cholesterol' as missing values

2. **Data Preprocessing**  
   - Categorical columns: Encoded using `OrdinalEncoder` (RF) or `OneHotEncoder` (SVM)  
   - Numerical columns: Imputed using `SimpleImputer`, scaled for SVM pipeline  
   - Pipelines wrapped using `ColumnTransformer` + `Pipeline`

3. **Model Training**  
   - Models: `RandomForestClassifier` and `SVC (RBF kernel)`  
   - Evaluation: `accuracy_score`, `classification_report`

4. **Model Saving**  
   - Trained pipelines stored via `joblib` as:
     - `models/rf_model_pipeline.pkl`
     - `models/svm_model_pipeline.pkl`

5. **Explainability (SHAP)**  
   - Used `TreeExplainer` for Random Forest
   - Used `KernelExplainer` for SVM (on a subset due to performance)
   - Visualizations with `summary_plot` to show top influencing features

---

## 🌐 Web App (`app.py`)

A Flask-based web application that allows users to input features and get real-time heart disease predictions.

## Features

- **Model Selector**: Choose between `Random Forest` and `SVM`
- **Form Input**: Accepts clinical features like Age, Cholesterol, ChestPainType, etc.
- **Live Prediction**: Returns result with emoji-enhanced messages
- **Dynamic Loading**: Loads saved models on request
- **Result Display**:  
  - 💓 No Heart Disease Detected  
  - 💔 Positive for Heart Disease


## 🚀 How to Run

1. Clone the repo
2. Ensure the following models exist:
   - `models/rf_model_pipeline.pkl`
   - `models/svm_model_pipeline.pkl`
3. Install dependencies:
    pip install flask pandas joblib
4. Start the Flask server:
    python app.py
5. Visit `http://127.0.0.1:5000` to interact with the model

---
