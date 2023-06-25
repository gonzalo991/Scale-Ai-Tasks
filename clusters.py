import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate sample data
np.random.seed(0)
X = np.concatenate((np.random.randn(200, 2) * 0.5 + [2, 2],
                    np.random.randn(200, 2) * 0.5 + [-2, -2]))

# Perform K-means clustering
k = 2  # Number of clusters
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

# Obtain cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plot the data points and cluster centroids
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=150, linewidths=3, color='red')
plt.title('K-means Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
