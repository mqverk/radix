import random
from .math import euclidean_distance

def kmeans(data, k, max_iterations=100):
    """
    Perform K-Means clustering on the given data.

    :param data: List of data points (list of lists).
    :param k: Number of clusters.
    :param max_iterations: Maximum number of iterations.
    :return: Cluster centers and assignments.
    """
    # Initialize centroids randomly
    centroids = random.sample(data, k)

    for _ in range(max_iterations):
        clusters = {i: [] for i in range(k)}

        # Assign points to the nearest centroid
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)

        # Update centroids
        new_centroids = []
        for i in range(k):
            cluster_points = clusters[i]
            if cluster_points:
                new_centroids.append([sum(dim) / len(cluster_points) for dim in zip(*cluster_points)])
            else:
                new_centroids.append(centroids[i])

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids, clusters