# curve_type: multi_weighted_adaptive_serpentine
# description: Enhanced adaptive serpentine with center_weight=2.2 and edge protection
import numpy as np
N = 1000
# --- parameters ---
num_lines = 95
center_weight = 2.2
edge_threshold = 0.5

y_positions = np.linspace(0, 1, num_lines)
normalized_y = (y_positions - 0.5) / 0.5
weights = 1 + center_weight * (1 - 4 * (normalized_y ** 2))
weights = np.maximum(weights, edge_threshold)
weights = weights / np.sum(weights)

points_per_line = (weights * N).astype(int)
points_per_line[-1] += N - np.sum(points_per_line)

x_coords = []
y_coords = []

for i, (y_val, num_points) in enumerate(zip(y_positions, points_per_line)):
    if num_points > 0:
        if i % 2 == 0:
            x_line = np.linspace(0, 1, num_points)
        else:
            x_line = np.linspace(1, 0, num_points)
        x_coords.extend(x_line)
        y_coords.extend([y_val] * num_points)

x = np.array(x_coords)
y = np.array(y_coords)
points = np.column_stack([x, y])