"""
Dataset: https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv

Use scikit-learn to build a Naive Bayes classifier for the type of species a flower is. Then run your classifier on some test data to determine its accuracy.
"""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


# Dataset: https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv

# read in data
data = pd.read_csv('iris.csv')

# build feature vectors(X) and label(y) for each vector
X = data.drop("species", axis=1)
y = data["species"]

print(X.head())
print()
print(y.head())
print()

# Convert pandas dataframe to numpy array
X = X.values
y = y.values

# split into testing and training data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# create and train Naive Bayes classifier
model = MultinomialNB()
model.fit(x_train, y_train)

# run classifier on the training data and check accuracy
y_pred = model.predict(x_test)
print("Accuracy: " + str(accuracy_score(y_test, y_pred) * 100) + " %")
print()

# run classifier on your own feature vectors
custom_vectors = [[5.2, 3.1, 1.6, 0.3], [6.0, 3.0, 4.8, 1.1], [7.5, 3.0, 6.2, 2.0]]
print(model.predict(custom_vectors))
