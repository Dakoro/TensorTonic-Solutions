import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    matrix = np.asarray(X, dtype=float)
    centered_matrix = matrix - np.mean(matrix, axis=0)
    return (centered_matrix.T @ centered_matrix) / (matrix.shape[0] - 1)