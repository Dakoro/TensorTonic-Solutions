import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    ord_map = {'l1': 1, 'l2': 2, 'max': np.inf}
    array = np.asarray(matrix, dtype=float)
    
    if norm_type not in ord_map:
        raise ValueError("norm_type must be 'l1', 'l2', or 'max'")
    
    norm_ord = ord_map[norm_type]

    if axis is None:
        # Calculate norm over the flattened matrix
        norm_val = np.linalg.norm(array.ravel(), ord=norm_ord)
    else:
        # Calculate norm along the specified axis
        # keepdims=True ensures the result maintains matrix dimensions for broadcasting
        norm_val = np.linalg.norm(array, ord=norm_ord, axis=axis, keepdims=True)
        
    # Prevent division by zero for zero-vectors
    norm_val = np.where(norm_val == 0, 1.0, norm_val)
    
    return matrix / norm_val