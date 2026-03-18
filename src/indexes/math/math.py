import math

def euclidean_distance(vec1, vec2):
    """
    Calculate the Euclidean distance between two vectors.
    """
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(vec1, vec2)))

def dot_product(vec1, vec2):
    """
    Calculate the dot product of two vectors.
    """
    return sum(x * y for x, y in zip(vec1, vec2))