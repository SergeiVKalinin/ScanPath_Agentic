# name: number_of_sharp_turns
# description: Standard deviation of second derivative (curvature variation)
# weight: 0.2
import numpy as np

def compute(points):
    """
    Input: points — numpy array of shape (N, 2), coordinates in [0,1]
    Output: score — float in [0, 1], higher is better
    """
    if len(points) < 3:
        return 1.0  # Not enough points to compute second derivative
    
    # Compute first derivative (velocity vectors)
    first_derivative = np.diff(points, axis=0)
    
    # Compute second derivative (acceleration/curvature)
    # This captures how the direction changes
    second_derivative = np.diff(first_derivative, axis=0)
    
    # Compute magnitude of second derivative at each point
    curvature_magnitudes = np.linalg.norm(second_derivative, axis=1)
    
    # Compute standard deviation of curvature magnitudes
    # High std means inconsistent turning (some sharp, some smooth)
    # Low std means consistent curvature throughout
    std_curvature = np.std(curvature_magnitudes)
    
    # Normalize by mean to get relative measure
    mean_curvature = np.mean(curvature_magnitudes)
    
    if mean_curvature == 0:
        return 1.0  # Straight line, no turns
    
    normalized_std = std_curvature / mean_curvature
    
    # Convert to score: lower std is better (more uniform turning)
    # Use exponential decay to map to [0,1]
    score = np.exp(-normalized_std)
    
    return float(score)