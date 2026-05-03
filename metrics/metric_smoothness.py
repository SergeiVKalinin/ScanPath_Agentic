# name: smoothness
# description: Standard deviation of curvature values (lower is better, favors smoother curves)
# weight: 0.2
import numpy as np

def compute(points):
    """
    Input: points — numpy array of shape (N, 2), coordinates in [0,1]
    Output: score — float in [0, 1], higher is better
    """
    if len(points) < 3:
        return 1.0  # Not enough points to compute curvature
    
    # Compute curvature at each point using finite differences
    curvatures = []
    
    for i in range(1, len(points) - 1):
        p0, p1, p2 = points[i-1], points[i], points[i+1]
        
        # Vectors
        v1 = p1 - p0
        v2 = p2 - p1
        
        # Compute curvature using the formula: k = |v1 × v2| / |v1|^3
        # For 2D: cross product gives scalar
        cross = v1[0] * v2[1] - v1[1] * v2[0]
        v1_norm = np.linalg.norm(v1)
        
        if v1_norm > 1e-10:
            # Menger curvature formula (more stable)
            area = abs(cross) / 2.0
            a = np.linalg.norm(p1 - p0)
            b = np.linalg.norm(p2 - p1)
            c = np.linalg.norm(p2 - p0)
            
            if a * b * c > 1e-10:
                curvature = 4.0 * area / (a * b * c)
            else:
                curvature = 0.0
        else:
            curvature = 0.0
        
        curvatures.append(curvature)
    
    if len(curvatures) == 0:
        return 1.0
    
    curvatures = np.array(curvatures)
    
    # Compute standard deviation of curvatures
    std_dev = np.std(curvatures)
    
    # Normalize: typical curvature std for scan curves ranges 0-10
    # Lower std means smoother, more consistent curvature
    max_std = 10.0
    score = max(0.0, 1.0 - min(std_dev / max_std, 1.0))
    
    return score