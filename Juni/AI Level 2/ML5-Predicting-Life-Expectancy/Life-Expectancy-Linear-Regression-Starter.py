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
