"""
Use scikit-learn to build a linear regression model and a polynomial regression model for the given data. Then test your model on an input value.
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([10, 8, 7.5, 7, 6, 6, 7, 9, 8.5, 11])

plt.scatter(x, y, s=50)
plt.savefig("before.png")
plt.clf()

# Try a linear model
print('Linear Model: ')
model = LinearRegression().fit(x, y)

b = model.intercept_
coefs = model.coef_
print("y intercept: " + str(b))
print("coefficients: " + str(coefs))

plt.scatter(x, y, s=50)
plt.plot(x, x * coefs[0] + b, 'r')
plt.savefig("linear.png")
plt.clf()

test = np.array([6]).reshape(-1, 1)
print("Predicted value of y for x = 7: " + str(model.predict(test)[0]))
print()

# try a polynomial model 
# degree = degree of polynomial
print('Polynomial Model: ')
x_modified = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)

model = LinearRegression().fit(x_modified, y)

b = model.intercept_
# index 0 is the coefficient of x, index 1 is the coefficient of x^2 and so on
coefs = model.coef_
print("y intercept: " + str(b))
print("coefficients: " + str(coefs))

plt.scatter(x, y, s=50)
plt.plot(x, x * x * coefs[1] + x * coefs[0] + b, 'r')
plt.savefig("polynomial.png")
plt.clf()

test = np.array([6]).reshape(-1, 1)
test_modified = PolynomialFeatures(degree=2, include_bias=False).fit_transform(test)
print("Predicted value of y for x = 7: " + str(model.predict(test_modified)[0]))
