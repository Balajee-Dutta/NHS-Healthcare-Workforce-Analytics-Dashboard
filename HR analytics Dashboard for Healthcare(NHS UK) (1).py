#!/usr/bin/env python3
"""
Our Python Script Name: attrition_risk_analysis.py

Purpose:
This script reads the NHS UK attrition dataset, trains two predictive models
(Logistic Regression and Random Forest) to estimate each employee's likelihood
of leaving (attrition), evaluates model performance, and saves the results
(including a new 'AttritionRisk' score) for use in dashboards or reports.

Audience:
Comments are written in simple terms so that anyone can follow along, even with
no technical background.
"""

# ------------------------------------------------------
# 1. Import necessary tools
# ------------------------------------------------------
# Purpose: Bring in all the packages we need to read data, build models, and measure performance.
import pandas as pd   # For reading and working with Excel data
import numpy as np    # For math and number handling
from sklearn.model_selection import train_test_split  # To split our data into 'train' and 'test'
from sklearn.linear_model import LogisticRegression   # A basic prediction model
from sklearn.ensemble import RandomForestClassifier   # A more powerful model that builds many small trees
from sklearn.metrics import classification_report, roc_auc_score  # To check how well our models work

# ------------------------------------------------------
# 2. Load the NHS dataset
# ------------------------------------------------------
# Purpose: Read in our Excel data about employees so we can analyze it.
data_file = 'NHS Attrition Data_UK.xlsx'
df = pd.read_excel(data_file)

# Show basic info in the terminal: how many employees, how many columns, and how many left vs stayed.
print("\n--- DATASET OVERVIEW ---")
print("Loaded data from:", data_file)
print("Total employees (rows):", df.shape[0])
print("Total columns (features):", df.shape[1])
print("Attrition counts (Yes = left, No = stayed):\n", df['Attrition'].value_counts(), "\n")

# ------------------------------------------------------
# 3. Prepare the data for modeling
# ------------------------------------------------------
# Purpose: Convert all words (like job roles, departments) into numbers so the models can use them.
df_encoded = pd.get_dummies(df, drop_first=True)
print("--- DATA PREPARATION ---")
print("All text converted to numbers. Number of columns now:", df_encoded.shape[1], "\n")

# ------------------------------------------------------
# 4. Choose what to predict (features vs target)
# ------------------------------------------------------
# Purpose: Separate the data into:
#   - X (features): Everything we use to predict (e.g., salary, overtime, department, etc.)
#   - y (target): What we want to predict (did the employee leave? Yes = 1, No = 0)
X = df_encoded.drop('Attrition_Yes', axis=1)
y = df_encoded['Attrition_Yes']
print("--- CHOOSING FEATURES & TARGET ---")
print("Using", X.shape[1], "features (columns) to predict attrition.")
print("Target classes (should be 0 and 1):", y.unique(), "\n")

# ------------------------------------------------------
# 5. Split the data for training and testing
# ------------------------------------------------------
# Purpose: To check if our models work well, we train them on part of the data (70%)
# and test them on the rest (30%). This simulates how well they'd work on new, unseen data.
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,        # 30% test, 70% train
    random_state=42,      # Makes results repeatable
    stratify=y            # Keeps left/stayed ratio the same in both sets
)
print("--- DATA SPLIT ---")
print("Training records:", X_train.shape[0])
print("Testing records:", X_test.shape[0], "\n")

# ------------------------------------------------------
# 6. Train and test Logistic Regression
# ------------------------------------------------------
# Purpose: This is a simple, classic model that tries to draw a line between employees who leave vs stay.
# We check how well it works on the test set.
print("--- LOGISTIC REGRESSION MODEL ---")
lr_model = LogisticRegression(max_iter=2000, random_state=42)
lr_model.fit(X_train, y_train)  # The model learns from the training data
y_pred_lr = lr_model.predict(X_test)  # Predicts stay/leave for the test data
y_prob_lr = lr_model.predict_proba(X_test)[:, 1]  # Gives the probability of leaving

# Show the results in the output terminal:
print("Classification Report (Logistic Regression):")
print(classification_report(y_test, y_pred_lr))
print("ROC-AUC Score (measures how well the model separates classes; higher is better):", roc_auc_score(y_test, y_prob_lr), "\n")

# ------------------------------------------------------
# 7. Train and test Random Forest
# ------------------------------------------------------
# Purpose: This is a more advanced model that builds many decision trees and averages their predictions.
# It's usually better at finding patterns than Logistic Regression.
print("--- RANDOM FOREST MODEL ---")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)  # Model learns from the training data
y_pred_rf = rf_model.predict(X_test)  # Predicts stay/leave for test data
y_prob_rf = rf_model.predict_proba(X_test)[:, 1]  # Probability of leaving

print("Classification Report (Random Forest):")
print(classification_report(y_test, y_pred_rf))
print("ROC-AUC Score (higher is better):", roc_auc_score(y_test, y_prob_rf), "\n")

# ------------------------------------------------------
# 8. Assign risk scores and display examples
# ------------------------------------------------------
# Purpose: Use the Random Forest model to assign a 'risk score' (chance of leaving)
# to each employee, then show a sample of these scores in the terminal.
print("--- GENERATING ATTRITION RISK SCORES ---")
risk_scores = rf_model.predict_proba(X)[:, 1]
df['AttritionRisk'] = risk_scores
print("Sample risk scores (first 5 employees):")
print(df[['Attrition', 'AttritionRisk']].head(), "\n")

# ------------------------------------------------------
# 9. Save the results for use in Power BI or Excel
# ------------------------------------------------------
# Purpose: Save the updated table (with risk scores) as a new Excel file, ready for dashboards or further analysis.
output_file = 'NHS_Attrition_Data_with_Risk.xlsx'
df.to_excel(output_file, index=False)
print("Saved updated dataset with attrition risk scores to:", output_file)