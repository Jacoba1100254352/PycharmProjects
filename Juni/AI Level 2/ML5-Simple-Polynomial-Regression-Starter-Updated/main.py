"""
Use scikit-learn to build a linear regression model and a polynomial regression model for the given data. Then test your model on an input value.
"""

import numpy as np


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([10, 8, 7.5, 7, 6, 6, 7, 9, 8.5, 11])
