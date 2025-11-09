"""
Dataset: https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv
"""

import matplotlib.pyplot as plt
import numpy as np


# draws a scatterplot such that each cluster's points are in different colors
def draw_clustered_graph(k, X, clusters, centroids):
	colors = ['r', 'g', 'b', 'y', 'c', 'm']
	fig, ax = plt.subplots()
	for i in range(k):
		points = []
		for j in range(len(X)):
			if clusters[j] == i:
				points.append(X[j])
		points = np.array(points)
		ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
	ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='#050505')
	plt.savefig("clustered_graph.png")
