import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf = [(1 - p) if n == 0 else p for n in x]
    variance = p * (1 - p)
    return {
        "pmf": np.asarray(pmf, dtype=float),
        "mean": float(p),
        "variance": float(variance)
    }