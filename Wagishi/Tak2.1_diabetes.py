# Task **2.1**

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

diabetes = pd.read_csv("diabetes.csv")

diabetes.head()

diabetes.isnull().sum()

diabetes.shape

diabetes.info()

diabetes.describe()

col_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
             'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

plt.figure(figsize=(12, 8))
for i, col in enumerate(col_names[:-1], 1):
    plt.subplot(3, 3, i)
    sns.histplot(diabetes[col].dropna(), kde=True)
    plt.title(col)
plt.tight_layout()
plt.show()

col_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
             'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

fig, axes = plt.subplots(8, 2, figsize=(12, 32)) 
for i, col in enumerate(col_names):
    
    sns.scatterplot(data=diabetes, x=col, y='Outcome', ax=axes[i, 0])
    axes[i, 0].set_title(f'Scatter Plot of {col} vs. Outcome')
    axes[i, 0].set_xlabel(col)
    axes[i, 0].set_ylabel('Outcome')

    sns.kdeplot(data=diabetes, x=col, hue='Outcome', ax=axes[i, 1])
    axes[i, 1].set_title(f'Distribution of {col} by Outcome')
    axes[i, 1].set_xlabel(col)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(diabetes.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Feature Correlations')
plt.show()

#Only glucose is correlated to outcome

x = diabetes.drop('Outcome', axis=1)
y = diabetes['Outcome']
x_train, x_test, y_train, y_test = train_test_split(x, y, stratify=y, test_size=0.2, random_state=42)

scaler = StandardScaler().fit(x_train)
x_train_s = scaler.transform(x_train)
x_test_s = scaler.transform(x_test)

lr = LogisticRegression()
lr.fit(x_train_s, y_train)

y_pred = lr.predict(x_test_s)
lr.score(x_test_s,y_test)*100

linear=LinearRegression()
linear.fit(x_train_s,y_train)

y_pred = linear.predict(x_test_s)
linear.score(x_test_s,y_test)*100

