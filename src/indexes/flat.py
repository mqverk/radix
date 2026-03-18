from .math import euclidean_distance

class FlatIndex:
    """
    Implements a flat index for brute-force search.
    """

    def __init__(self):
        self.data = []

    def add(self, vector):
        """
        Add a vector to the index.
        """
        self.data.append(vector)

    def search(self, query, k):
        """
        Perform a brute-force search to find the top-k nearest neighbors.
        """
        distances = [(euclidean_distance(query, vec), vec) for vec in self.data]
        distances.sort(key=lambda x: x[0])
        return distances[:k]