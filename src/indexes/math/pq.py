import numpy as np

class ProductQuantization:
    """
    Implements Product Quantization (PQ) for dimensionality reduction and approximate nearest neighbor search.
    """

    def __init__(self, num_subvectors: int):
        self.num_subvectors = num_subvectors
        self.codebooks = []

    def fit(self, data):
        """
        Fit the PQ model to the data.
        """
        n, d = data.shape
        assert d % self.num_subvectors == 0, "Dimensionality must be divisible by the number of subvectors."

        subvector_size = d // self.num_subvectors
        self.codebooks = []

        for i in range(self.num_subvectors):
            subvector_data = data[:, i * subvector_size:(i + 1) * subvector_size]
            centroids, _ = kmeans(subvector_data.tolist(), k=256)
            self.codebooks.append(np.array(centroids))

    def encode(self, vector):
        """
        Encode a vector into PQ codes.
        """
        subvector_size = len(vector) // self.num_subvectors
        codes = []

        for i in range(self.num_subvectors):
            subvector = vector[i * subvector_size:(i + 1) * subvector_size]
            distances = [euclidean_distance(subvector, centroid) for centroid in self.codebooks[i]]
            codes.append(np.argmin(distances))

        return codes

    def decode(self, codes):
        """
        Decode PQ codes back into an approximate vector.
        """
        subvector_size = len(self.codebooks[0][0])
        vector = []

        for i, code in enumerate(codes):
            vector.extend(self.codebooks[i][code])

        return np.array(vector)