import heapq

def top_k(elements, k):
    """
    Retrieve the top-k elements from a list.

    :param elements: List of tuples (value, data).
    :param k: Number of top elements to retrieve.
    :return: List of top-k elements.
    """
    return heapq.nlargest(k, elements, key=lambda x: x[0])

# Placeholder for top-k nearest neighbors implementation