
# 🎧 Spotify 2023 Stream Prediction

This project performs **Exploratory Data Analysis (EDA)** and builds **machine learning models** to predict the number of streams for a track using the Spotify 2023 dataset.

---

## 📌 Project Highlights

- 📊 Cleaned and analyzed real-world Spotify data
- 🧹 Handled missing values using median and mode
- 🔁 Converted categorical features to numeric with one-hot encoding
- 📈 Built and evaluated regression models to predict stream counts
- 📉 Visualized key relationships between audio features and popularity

---

## Key Steps in the EDA

## 1. Data Loading and Initial Exploration

Loaded the dataset into a Pandas DataFrame.

Checked for missing values, duplicates, and data types.

Summarized basic statistics (mean, median, min, max) for numerical columns.

## 2. Data Cleaning

Handled missing values by either imputing or dropping them based on context.

Corrected data types (e.g., converting 'streams' to numeric).

Standardized categorical values (e.g., converting 'key' and 'mode' to consistent formats).

## 3. Feature Analysis

Explored distributions of numerical features (e.g., streams, danceability, energy) using histograms and box plots.

Analyzed categorical features (e.g., artist names, key, mode) using bar charts and count plots.

Investigated correlations between audio features and streaming performance.

## 4. Trends Over Time

Visualized the release trends of tracks over months/years.

Compared the performance of tracks released in different years.

## 5. Artist and Track Insights

Identified the most popular artists based on streams and playlist inclusions.

Highlighted top-performing tracks and their audio characteristics.

Explored collaborations (tracks with multiple artists) and their impact on popularity.

## 6. Audio Feature Insights
Analyzed how audio features (e.g., danceability, valence) relate to track popularity.

Compared feature distributions across different genres or artist groups.

## 7. Interactive Visualizations
Created interactive plots (e.g., scatter plots, heatmaps) to explore relationships between features.

Used Seaborn and Matplotlib for static visualizations.

---



## 🔧 Tools & Libraries Used

- Python
- pandas & NumPy
- matplotlib & seaborn
- scikit-learn

---

## 🧪 Models Implemented

| Model               | R² Score | RMSE         |
|--------------------|----------|--------------|
| Linear Regression  | 0.712        | 7.800          |




## 📊 Visualizations Included

- Heatmap of feature correlation
- Top 10 artists by total streams
- Histograms of audio features

---



## 📂 Dataset

The dataset used is `spotify-2023.csv` — a snapshot of popular Spotify tracks in 2023, containing audio features and stream counts.

---


      


# 🩺 Diabetes Prediction Project

This project involves analyzing and modeling a dataset of patient health metrics to predict the likelihood of diabetes.

---

## 📌 Project Highlights

- Performed Exploratory Data Analysis (EDA) on key health indicators
- Handled missing or zero-value data in medically relevant columns
- Built machine learning models to predict diabetes occurrence
- Evaluated models using accuracy, precision, recall, and F1-score
- Visualized patterns in health metrics related to diabetes

---

## Dataset Overview

-This dataset contains medical records of patients with information about various health metrics and whether they have diabetes (Outcome = 1) or not (Outcome = 0).

 Variables:
 Pregnancies: Number of times pregnant

Glucose: Plasma glucose concentration (mg/dL)

BloodPressure: Diastolic blood pressure (mm Hg)

SkinThickness: Triceps skin fold thickness (mm)

Insulin: 2-Hour serum insulin (mu U/ml)

BMI: Body mass index (weight in kg/(height in m)^2)

DiabetesPedigreeFunction: Diabetes pedigree function

Age: Age in years

Outcome: 1 = has diabetes, 0 = no diabetes

## EDA Steps Performed

### 1. Data Loading and Initial Inspection

-Loaded the dataset into a pandas DataFrame

-Checked the first few rows to understand the structure

-Verified the data types of each column

-Checked for missing values (zeros in medical measurements may indicate missing data)

## 2. Data Cleaning
-Identified and handled missing values (represented as zeros in some medical measurements)

-Checked for duplicates and removed if any

Verified data ranges for each variable to identify potential outliers

3. Statistical Analysis
Calculated basic statistics (mean, median, standard deviation, min, max) for each variable

Compared statistics between diabetic and non-diabetic groups

Analyzed the distribution of the target variable (Outcome)

4. Visualization
Created histograms for each numerical variable to understand distributions

Generated boxplots to identify outliers and compare distributions between groups

Produced correlation heatmap to understand relationships between variables

Created scatter plots for key variable pairs

Visualized the imbalance in the target variable

5. Feature Analysis
Analyzed how each feature relates to the outcome

Identified features with the strongest correlation to diabetes

Examined age distribution across outcomes

Investigated BMI patterns between diabetic and non-diabetic patients



## 🔧 Tools & Libraries Used

- Python
- pandas & NumPy
- seaborn & matplotlib
- scikit-learn

---

## 📊 Features in Dataset

- `Pregnancies`: Number of times pregnant
- `Glucose`: Plasma glucose concentration
- `BloodPressure`: Diastolic blood pressure
- `SkinThickness`: Triceps skin fold thickness
- `Insulin`: Serum insulin
- `BMI`: Body Mass Index
- `DiabetesPedigreeFunction`: Diabetes likelihood based on family history
- `Age`: Patient age
- `Outcome`: 1 if diabetic, 0 otherwise

---

## 🧪 Models Implemented

| Model                 | Accuracy |
|----------------------|----------|
| Logistic Regression  | 0.7489    | 






## 📂 Dataset

The dataset is a classic diabetes dataset from the Pima Indian heritage population, often used for medical ML research.

---






