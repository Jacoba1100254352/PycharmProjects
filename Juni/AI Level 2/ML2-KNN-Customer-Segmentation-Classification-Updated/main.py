from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

def calculate_dist(a, b):
  total = 0
  for i in range(len(a)):
    total += (a[i] - b[i])**2
  return total ** 0.5

def is_same(a, b):
  for i in range(len(a)):
    if a != b:
      return False
  return True

def calculate_centroid(points):
  x_sum = 0
  y_sum = 0
  for point in points:
    x_sum += point[0]
    y_sum += point[1]
  return (x_sum/len(points), y_sum/len(points))

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
    print("Cluster Number: " + str(i) + " | Color: " + colors[i])

  xpoints = []
  ypoints = []
  for c in centroids:
    xpoints.append(c[0])
    ypoints.append(c[1])
  ax.scatter(xpoints, ypoints, marker='*', s=200, c='#050505')
  plt.savefig("clustered_graph.png")
  print()

# read in the data
data = pd.read_csv('customers.csv')
income = data['Annual Income']
spending = data['Spending Score']

# graph before any clustering
plt.scatter(income, spending, s= 7)
plt.savefig("before_clustering.png")
plt.clf()

k = 5
# builds array of data points
X = list(zip(income, spending))

# initialize random centroids
centroids = []

for i in range(k):
  random_index = random.randint(0, len(income)-1)
  x = X[random_index][0]
  y = X[random_index][1]
  centroids.append((x,y))

# build array of tuples to store old centroids
old_centroids = []
for i in range(k):
  old_centroids.append((0,0))

# index i in clusters stores the cluster assigned for data point i
clusters = [0]*len(X)

# if error is 0 then the centroids have not moved from the last iteration (therefore we can stop)
while not is_same(centroids, old_centroids):
  # calculate distance from each centroid for each data point
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


###### KNN Implementation ######
# another k value for KNN (different than the clustering k value)
k2 = 3

# data pt we want to classify written as (income, spending)
data_pt = (90, 20)

# find k2 closest neighbors
# dictionary maps each of the k2 neighbors to their distance
k2_nearest = {}

# loop through each point and calculate its distance from the point we want to classify
for point in X:
  dist = calculate_dist(point, data_pt)

  # if dictionary doesn't have k values yet, add the current data point
  if len(k2_nearest) < k2:
    k2_nearest[point] = dist
  # if dictionary has k values, find the largest distance value in the dictionary and check if the current distance is less. If so, swap the old max out and place new data point into dictionary. 
  else:
    max_neighbor = (-1, -1)
    max_dist = -1
    for neighbor in k2_nearest:
      if k2_nearest[neighbor] > max_dist:
        max_neighbor = neighbor
        max_dist = k2_nearest[neighbor]
    
    if max_dist > dist:
      k2_nearest.pop(max_neighbor)
      k2_nearest[point] = dist

# dict to store the amount of neighbors that fall in each cluster
k2_neighbors_count = {}

# count the number of data points in k nearest neighbors that fall into each cluster
for point in k2_nearest:
  index = X.index(point)
  cluster = clusters[index]
  if cluster in k2_neighbors_count:
    k2_neighbors_count[cluster] += 1
  else:
    k2_neighbors_count[cluster] = 1

# find k in dictionary with max number of points. This is the final classification of your point.
max_label = -1
max_count = -1
for key in k2_neighbors_count:
  if k2_neighbors_count[key] > max_count:
    max_count = k2_neighbors_count
    max_label = key

print(str(data_pt) + " is classified as part of cluster " + str(max_label))