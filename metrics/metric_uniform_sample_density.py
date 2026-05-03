# name: uniform_sample_density
# description: Standard deviation of point counts across 10x10 grid bins (lower is better, inverted for scoring)
# weight: 0.5
import numpy as np

def compute(points):
    """
    Input: points — numpy array of shape (N, 2), coordinates in [0,1]
    Output: score — float in [0, 1], higher is better
    """
    # Create 10x10 grid and count points in each bin
    hist, _, _ = np.histogram2d(points[:, 0], points[:, 1], bins=10, range=[[0, 1], [0, 1]])
    
    # Compute standard deviation of point counts
    std_dev = np.std(hist)
    
    # Normalize: lower std is better, so we invert
    # Use a reasonable scaling factor based on expected variation
    # For N points, perfect uniformity = N/100 per bin, worst case std ~ N/10
    N = len(points)
    max_std = N / 10.0  # Approximate worst-case standard deviation
    
    # Score: 1.0 for std=0 (perfect uniformity), 0.0 for high std
    score = max(0.0, 1.0 - (std_dev / max_std))
    
    return score