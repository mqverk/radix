from .ivf import IVFIndex
from .math.pq import ProductQuantization

class IVFPQIndex:
    """
    Combines IVF and PQ for efficient approximate nearest neighbor search.
    """

    def __init__(self, num_clusters, num_subvectors):
        self.ivf = IVFIndex(num_clusters)
        self.pq = ProductQuantization(num_subvectors)

    def train(self, data):
        """
        Train the IVF and PQ models.
        """
        self.ivf.train(data)
        self.pq.fit(data)

    def add(self, vector):
        """
        Add a vector to the index.
        """
        self.ivf.add(vector)

    def search(self, query, k):
        """
        Search for the top-k nearest neighbors using IVF and PQ.
        """
        distances = [
            (euclidean_distance(query, centroid), centroid_index)
            for centroid_index, centroid in enumerate(self.ivf.centroids)
        ]
        distances.sort(key=lambda x: x[0])
        nearest_cluster = distances[0][1]

        candidates = self.ivf.clusters.get(nearest_cluster, [])
        pq_codes = [self.pq.encode(vec) for vec in candidates]
        decoded_candidates = [self.pq.decode(code) for code in pq_codes]

        candidates_distances = [
            (euclidean_distance(query, vec), vec) for vec in decoded_candidates
        ]
        candidates_distances.sort(key=lambda x: x[0])
        return candidates_distances[:k]