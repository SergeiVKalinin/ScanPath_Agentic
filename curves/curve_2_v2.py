# curve_type: serpentine
# description: Edge-weighted serpentine with inverse density profile
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100  # keep consistent with top performer
base_points = 50  # baseline points per line
# Calculate edge-weighted allocation
normalized_positions = np.linspace(0, 1, num_lines)
weights = 1.0 + 2.0 * (4 * (normalized_positions - 0.5)**2)  # peaks at edges
weights = weights / weights.sum()
points_per_line = (weights * N).astype(int)
# Adjust for exact N
points_per_line[-1] += N - points_per_line.sum()
# Create bidirectional serpentine
points_list = []
for i in range(num_lines):
    y_coord = i / (num_lines - 1)
    n_pts = points_per_line[i]
    if n_pts > 0:
        if i % 2 == 0:
            x_coords = np.linspace(0, 1, n_pts)
        else:
            x_coords = np.linspace(1, 0, n_pts)
        y_coords = np.full(n_pts, y_coord)
        points_list.append(np.column_stack([x_coords, y_coords]))
points = np.vstack(points_list)