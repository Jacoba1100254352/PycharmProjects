"""
Dataset: https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python
"""

import matplotlib.pyplot as plt


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
