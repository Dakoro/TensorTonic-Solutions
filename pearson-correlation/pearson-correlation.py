import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X = np.asarray(X, dtype=float)
    centered = X - X.mean(axis=0)
    cov_matrix = (centered.T @ centered) / (centered.shape[0] - 1)
    std_devs = np.sqrt(np.diag(cov_matrix))
    return cov_matrix / np.outer(std_devs, std_devs)