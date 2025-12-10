"""
Dataset: https://www.kaggle.com/prateekmaj21/disney-movies
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def draw_clustered_graph(k, X, clusters, centroids):
	colors = ['r', 'g', 'b', 'y', 'c', 'm']
	fig, ax = plt.subplots()
	for i in range(k):
		points = []
		for j in range(len(X)):
			if clusters[j] == i:
				points.append(X[j])
		points = np.array(points)
		ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i % len(colors)])
	ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='#050505')
	plt.savefig("clustered_graph.png")


data = pd.read_csv('disney.csv')
dates_raw = data['release_date']
years = []
for date in dates_raw:
	dash_index = date.index('-')
	years.append(int(date[:dash_index]))
gross = data['inflation_adjusted_gross']

# graph before any clustering
plt.scatter(years, gross, s=7)
plt.savefig("before_clustering.png")
plt.clf()

k = 3
X = list(zip(years, gross))

km = KMeans(
	n_clusters=k, init='random',
	n_init=10, max_iter=300,
	tol=1e-04, random_state=0
)
clusters = km.fit_predict(X)
centroids = km.fit(X).cluster_centers_

# graph after clustering
draw_clustered_graph(k, X, clusters, centroids)
