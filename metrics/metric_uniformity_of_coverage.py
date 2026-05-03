# name: uniformity_of_coverage
# description: Coefficient of variation of point density across spatial bins
# weight: 0.5
import numpy as np

def compute(points):
    """
    Input: points — numpy array of shape (N, 2), coordinates in [0,1]
    Output: score — float in [0, 1], higher is better
    """
    # Divide the [0,1]x[0,1] space into a grid of bins
    n_bins = 20  # 20x20 grid for reasonable resolution
    
    # Compute 2D histogram to count points in each bin
    hist, _, _ = np.histogram2d(
        points[:, 0], 
        points[:, 1], 
        bins=n_bins, 
        range=[[0, 1], [0, 1]]
    )
    
    # Flatten the histogram to get counts per bin
    bin_counts = hist.flatten()
    
    # Compute coefficient of variation (std / mean)
    # Only consider non-empty bins to avoid division issues
    non_zero_counts = bin_counts[bin_counts > 0]
    
    if len(non_zero_counts) == 0:
        return 0.0
    
    mean_count = np.mean(non_zero_counts)
    std_count = np.std(non_zero_counts)
    
    if mean_count == 0:
        return 0.0
    
    cv = std_count / mean_count
    
    # Convert to score: lower CV is better, so invert and normalize
    # Use exponential decay to map CV to [0,1] where 0 CV gives 1.0
    score = np.exp(-cv)
    
    return float(score)