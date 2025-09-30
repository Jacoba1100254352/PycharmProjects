import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Dataset: https://sci2s.ugr.es/keel/dataset.php?cod=56#sub2

# read in data and replace categories with dictionary values
data = pd.read_csv('cars.csv')

# dictionaries to translate categories to values
levels = {"vhigh": 0, "high": 1, "med": 2, "low": 3}
doors = {"2":2, "3":3, "4":4, "5more":5}
persons ={"2": 2, "4":4, "more":5}
lug_boot = {"small": 0, "med": 1, "big": 2}
safety = {"high": 1, "med": 2, "low": 3}
cleanup_nums = {"buying": levels, "maintenance": levels, "doors": doors, "persons": persons, "lug boot": lug_boot, "safety": safety}

data.replace(cleanup_nums, inplace = True)

# build feature vectors and labels
X = data.drop("acceptability", axis = 1)
y = data["acceptability"]

# Convert pandas dataframe to numpy array
X = X.values
y = y.values

# split data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 100)

# build and train classifier
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)

# run classifier on test data
y_pred = knn.predict(x_test)
print("Accuracy: " + str(accuracy_score(y_test, y_pred)))
print()

# data point we want to classify written as (year, rating)
data_pt = [0, 0, 2, 2, 0, 3]


# run on your data point
label = knn.predict([data_pt])[0]
print("Data point " + str(data_pt) + " is classified as " + str(label))