import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    array_a = np.asarray(a, dtype=float)
    array_b = np.asarray(b, dtype=float)

    dot_product = array_a @ array_b
    norm_a = np.linalg.norm(array_a)
    norm_b = np.linalg.norm(array_b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot_product / (norm_a * norm_b))