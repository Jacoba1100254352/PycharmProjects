"""
Use scikit-learn to build a linear regression model for the given dataset. Then test your model on an input value.
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([4, 5, 6, 3, 5, 7, 3, 9, 13, 14])

plt.scatter(x, y, s=50)
plt.savefig("before.png")
plt.clf()

model = LinearRegression()
model.fit(x, y)

# line of best fit has form y = mx + b where m = slope and b = y-intercept
corr = model.score(x, y)
b = model.intercept_
m = model.coef_[0]
print("Correlation Between x and y: " + str(corr))
print("y intercept: " + str(b))
print("slope: " + str(m))

plt.scatter(x, y, s=50)
plt.plot(x, x * m + b, 'r')
plt.savefig("after.png")
plt.clf()

test = np.array([7]).reshape(-1, 1)
print("Predicted value of y for x = 7: " + str(model.predict(test)[0]))
