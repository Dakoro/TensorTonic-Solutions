import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    array = np.asarray(A, dtype=float)
    dim_A = array.shape
    AT = np.zeros((dim_A[1], dim_A[0]))
    for i in range(dim_A[0]):
        for j in range(dim_A[1]):
            AT[j][i] = A[i][j]
    return AT
