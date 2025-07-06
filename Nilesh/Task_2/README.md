# Task 2(i): Diabetes Dataset Analysis and Training Logistic Regression Model

## Overview
This project explores a dataset related to diabetes, performs exploratory data analysis (EDA), and builds a Logistic Regression model to predict the outcome of diabetes diagnosis.

## Dataset
- Source: https://www.kaggle.com/datasets/mathchi/diabetes-data-set
- The dataset contains various medical variables that influence the presence of diabetes in patients.

## Source Code
    https://colab.research.google.com/drive/1UWJXyB29duPhAfq8omJCSxQ1hlDvQ4dQ?usp=sharing

## Libraries Used
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `sklearn`

## Steps Performed
1. Load and Inspect Data
   - Read dataset using `pandas`
   - Check shape, info, and summary statistics

2. Data Cleaning
   - Check for missing values

3. Exploratory Data Analysis (EDA)
   - Compute correlation matrix and visualize with a heatmap
   - Plot histograms of numeric features
   - Create boxplots to identify outliers
   - Use pair plots to analyze feature relationships with the target variable

4. Model Building
   - Standardize features using `StandardScaler`
   - Split dataset into training and testing sets (80-20 split)
   - Train a Logistic Regression model
   - Make predictions and evaluate the model with:
     - `Classification Report`
     - `Accuracy Score`

## Results
- The trained Logistic Regression model provides accuracy scores for both the training and test sets.

# Task 2(ii): Spotify Streams Analysis and Prediction

## Overview
This project involves an exploratory data analysis (EDA) and predictive modeling using spotify-2023 dataset. We clean and visualize the data to uncover insights, then use Linear Regression to predict streaming numbers based on playlist presence.

## Dataset
- Source: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023
- The dataset contains information about songs, their streaming counts, and playlist appearances across various platforms.

## Source Code
    https://colab.research.google.com/drive/1Ph9E7TrE5eb61G1_m1G1bt1TSL5QYn8T?usp=sharing

## Libraries Used
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `sklearn`

## Steps Performed

### 1. Data Loading & Inspection
- Loaded the dataset (`spotify-2023.csv`) using pandas.
- Explored dataset structure using `.shape`, `.head()`, `.info()`.

### 2. Data Cleaning & Preprocessing
- Removed commas from numeric columns (`streams`, `in_deezer_playlists`, `in_shazam_charts`) to ensure proper conversion.
- Converted relevant features to numeric format while handling missing values.
- Filled missing values for streams and in_shazam_charts with `0`, and key with `"Unknown"`.

### 3. Exploratory Data Analysis (EDA)
- Created a distribution plot of streaming counts with logarithmic scaling.
- Generated a heatmap showing correlations between numerical features.
- Identified top features most correlated with `streams`.
- Created scatter plots for the strongest correlated features.
- Displayed a box plot to visualize outliers in streaming counts.

### 4. Linear Regression Model
- Selected input features (`in_spotify_playlists`, `in_apple_playlists`, `in_deezer_playlists`) and target (`streams`).
- Split dataset into training (80%) and testing (20%) subsets.
- Trained a Linear Regression model using scikit-learn.
- Evaluated model performance using R² score and Root Mean Square Error (RMSE).

## Results
The trained Linear Regression model predicts streams for the test dataset.
