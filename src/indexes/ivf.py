from .math import euclidean_distance
from .math.kmeans import kmeans

class IVFIndex:
    """
    Implements an Inverted File (IVF) index for efficient search.
    """

    def __init__(self, num_clusters):
        self.num_clusters = num_clusters
        self.clusters = {}
        self.centroids = []

    def train(self, data):
        """
        Train the IVF index by clustering the data.
        """
        self.centroids, clusters = kmeans(data, self.num_clusters)
        for i, points in clusters.items():
            self.clusters[i] = points

    def add(self, vector):
        """
        Add a vector to the nearest cluster.
        """
        distances = [euclidean_distance(vector, centroid) for centroid in self.centroids]
        cluster_index = distances.index(min(distances))
        if cluster_index not in self.clusters:
            self.clusters[cluster_index] = []
        self.clusters[cluster_index].append(vector)

    def search(self, query, k):
        """
        Search for the top-k nearest neighbors in the index.
        """
        distances = [euclidean_distance(query, centroid) for centroid in self.centroids]
        nearest_cluster = distances.index(min(distances))
        candidates = self.clusters.get(nearest_cluster, [])
        candidates_distances = [(euclidean_distance(query, vec), vec) for vec in candidates]
        candidates_distances.sort(key=lambda x: x[0])
        return candidates_distances[:k]