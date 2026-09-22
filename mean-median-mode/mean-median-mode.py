from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    array = np.asarray(x, dtype=float)
    counter = Counter(x)
    mode, _ = counter.most_common(n=1)[0]
    return {
        "mean": float(np.mean(array)),
        "median": float(np.median(array)),
        "mode": float(mode)
    }