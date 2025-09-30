from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import random
import math


# draws a scatterplot such that each cluster's points are in different colors
def draw_clustered_graph(k, X, clusters, centroids):
  colors = ['r', 'g', 'b', 'y', 'c', 'm']
  fig, ax = plt.subplots()
  for i in range(k):
    xpoints = []
    ypoints = []
    for j in range(len(X)):
      if clusters[j] == i:
        xpoints.append(X[j][0])
        ypoints.append(X[j][1])
    ax.scatter(xpoints, ypoints, s=7, c=colors[i])

  xpoints = []
  ypoints = []
  for c in centroids:
    xpoints.append(c[0])
    ypoints.append(c[1])
  ax.scatter(xpoints, ypoints, marker='*', s=200, c='#050505')
  plt.savefig("clustered_graph.png")


# calculates the euclidean distance between two points a and b
def calculate_dist(a, b):
  total = 0
  for i in range(len(a)):
    total += (a[i] - b[i])**2
  return total**0.5


# takes in a list of points from the same cluster then takes the average to find the centroid of the cluster
def calculate_centroid(points):
  x_sum = 0
  y_sum = 0
  for point in points:
    x_sum += point[0]
    y_sum += point[1]
  return (x_sum / len(points), y_sum / len(points))


# read in the data
data = pd.read_csv('customers.csv')
income = data['Annual Income']
spending = data['Spending Score']

# graph before any clustering
plt.scatter(income, spending, s=7)
plt.savefig("before_clustering.png")
plt.clf()

k = 5
# builds array of data points
X = list(zip(income, spending))

# initialize random centroids
centroids = []

for i in range(k):
  random_index = random.randint(0, len(income) - 1)
  x = X[random_index][0]
  y = X[random_index][1]
  centroids.append((x, y))

# build array of tuples to store old centroids
old_centroids = []
for i in range(k):
  old_centroids.append((0, 0))

# index i in clusters stores the cluster assigned for data point i
clusters = [0] * len(X)

# centroids have not moved from the last iteration, we can stop
while centroids != old_centroids:
  # calculate distance from each centroid for each data point and assign data point to the cluster of the closest centroid
  for i in range(len(X)):
    min_dist = math.inf
    for j in range(len(centroids)):
      dist = calculate_dist(X[i], centroids[j])
      if dist < min_dist:
        min_dist = dist
        clusters[i] = j

  # replace old centroids with current ones
  old_centroids = deepcopy(centroids)

  # calculate new centroids
  for i in range(k):
    points = []
    for j in range(len(X)):
      if clusters[j] == i:
        points.append(X[j])
    centroids[i] = calculate_centroid(points)

draw_clustered_graph(k, X, clusters, centroids)
