import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    array = np.asarray(x, dtype=float)
    n = len(x)
    mean = np.mean(array)
    s_squared = np.sum(array**2 - mean**2) / (n - 1)
    return {
        "variance": float(s_squared),
        "standard_deviation": float(np.sqrt(s_squared))
    }