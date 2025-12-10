# -*- coding: utf-8 -*-
"""
Life Expectancy Linear + Polynomial Regression

Original file is located at
    https://colab.research.google.com/drive/1Y0Rm_Pi6Gj-tXNlf-tGEcpLqUAShrwIR
"""

"""
Dataset: https://www.kaggle.com/kumarajarshi/life-expectancy-who

Build a linear regression model and a polynomial regression model that predicts the life expectancy of a person based on their characteristics. Determine which model best fits the data.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# Load CSV dataset from URL
filepath = 'https://static.junilearning.com/ai_level_2/life_expectancy.csv'
# dataset: https://www.kaggle.com/kumarajarshi/life-expectancy-who
data = pd.read_csv(filepath)

# Remove non-numeric or categorical columns
data = data.drop('Country', axis=1)
data = data.drop('Status', axis=1)

# Remove rows with missing values
data.dropna(inplace=True)

print("Dataset preview:")
print(data.head())
print()

# Separate features (X) and target values (y)
X = np.array(data.drop('Life expectancy ', axis=1))
y = np.array(data['Life expectancy '])

print("Feature matrix shape:", X.shape)
print("Target vector shape:", y.shape)
print()

# ------------------------ LINEAR REGRESSION ------------------------

# Split into training and test sets
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train linear regression model
model = LinearRegression()
model.fit(x_train, y_train)

# Evaluate linear model (R² score)
accuracy = model.score(x_test, y_test)
print("Linear Regression Score: " + str(accuracy * 100) + " %")
print()

# ---------------------- POLYNOMIAL REGRESSION ----------------------

# Expand features to include polynomial terms (degree 2)
x_modified = PolynomialFeatures(degree=2, include_bias=False).fit_transform(X)

# Split polynomial features into train/test sets
x_train, x_test, y_train, y_test = train_test_split(
    x_modified, y, test_size=0.25, random_state=42
)

# Recreate X and y (not strictly necessary but mirrors original script)
X = np.array(data.drop('Life expectancy ', axis=1))
y = np.array(data['Life expectancy '])

# Train model on polynomial features
model.fit(x_train, y_train)

# Evaluate polynomial model (R² score)
accuracy = model.score(x_test, y_test)
print("Polynomial Regression Score: " + str(accuracy * 100) + " %")
print()
