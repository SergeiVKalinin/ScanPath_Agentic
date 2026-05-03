# name: time_dependence_of_dose
# description: Standard deviation of visit counts per spatial bin
# weight: 0.3
import numpy as np

def compute(points):
    """
    Input: points — numpy array of shape (N, 2), coordinates in [0,1]
    Output: score — float in [0, 1], higher is better
    """
    # Divide the [0,1]x[0,1] space into a grid of bins
    n_bins = 20  # 20x20 grid for reasonable resolution
    
    # Compute 2D histogram to count visits to each bin
    hist, _, _ = np.histogram2d(
        points[:, 0], 
        points[:, 1], 
        bins=n_bins, 
        range=[[0, 1], [0, 1]]
    )
    
    # Flatten the histogram to get visit counts per bin
    visit_counts = hist.flatten()
    
    # Compute standard deviation of visit counts
    # Lower std means bins are visited more uniformly (ideally once)
    std_visits = np.std(visit_counts)
    
    # Normalize by the mean to get a relative measure
    mean_visits = np.mean(visit_counts)
    
    if mean_visits == 0:
        return 0.0
    
    # Normalized standard deviation
    normalized_std = std_visits / mean_visits
    
    # Convert to score: lower std is better
    # Use exponential decay to map to [0,1]
    score = np.exp(-normalized_std)
    
    return float(score)