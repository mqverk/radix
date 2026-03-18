from .flat import FlatIndex
from .math.pq import ProductQuantization

class PQFlatIndex:
    """
    Combines PQ and flat search for hybrid indexing.
    """

    def __init__(self, num_subvectors):
        self.flat_index = FlatIndex()
        self.pq = ProductQuantization(num_subvectors)

    def train(self, data):
        """
        Train the PQ model and add data to the flat index.
        """
        self.pq.fit(data)
        for vector in data:
            self.flat_index.add(vector)

    def search(self, query, k):
        """
        Search for the top-k nearest neighbors using PQ and flat search.
        """
        pq_query = self.pq.encode(query)
        decoded_query = self.pq.decode(pq_query)
        return self.flat_index.search(decoded_query, k)