# name: time_uniformity
# description: Standard deviation of time spent across bins (lower is better, penalizes rushing through areas)
# weight: 0.3
import numpy as np

def compute(points):
    """
    Input: points — numpy array of shape (N, 2), coordinates in [0,1]
    Output: score — float in [0, 1], higher is better
    """
    if len(points) < 2:
        return 1.0
    
    # Create 10x10 grid
    grid_size = 10
    time_grid = np.zeros((grid_size, grid_size))
    
    # Calculate time spent in each bin
    # Time is proportional to distance traveled (assuming constant velocity along curve)
    for i in range(len(points) - 1):
        p1, p2 = points[i], points[i + 1]
        
        # Segment distance (proxy for time)
        segment_time = np.linalg.norm(p2 - p1)
        
        # Find which bin this segment belongs to (use midpoint)
        mid = (p1 + p2) / 2.0
        bin_x = int(np.clip(mid[0] * grid_size, 0, grid_size - 1))
        bin_y = int(np.clip(mid[1] * grid_size, 0, grid_size - 1))
        
        time_grid[bin_x, bin_y] += segment_time
    
    # Only consider visited bins for standard deviation
    visited_bins = time_grid[time_grid > 0]
    
    if len(visited_bins) == 0:
        return 0.0
    
    # Compute standard deviation of time spent
    std_dev = np.std(visited_bins)
    mean_time = np.mean(visited_bins)
    
    # Normalize using coefficient of variation to make it scale-independent
    if mean_time > 0:
        cv = std_dev / mean_time
        # Score: lower CV is better (more uniform time distribution)
        score = max(0.0, 1.0 - min(cv, 1.0))
    else:
        score = 0.0
    
    return score