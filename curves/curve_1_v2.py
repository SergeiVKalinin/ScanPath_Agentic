# curve_type: serpentine
# description: Denser serpentine with 150 scan lines for improved smoothness
import numpy as np
N = 10000
# --- parameters ---
num_lines = 150  # increased from 100 for higher density
points_per_line = N // num_lines
# Create bidirectional serpentine pattern
points_list = []
for i in range(num_lines):
    y_coord = i / (num_lines - 1)
    if i % 2 == 0:  # left to right
        x_coords = np.linspace(0, 1, points_per_line)
    else:  # right to left
        x_coords = np.linspace(1, 0, points_per_line)
    y_coords = np.full(points_per_line, y_coord)
    points_list.append(np.column_stack([x_coords, y_coords]))
points = np.vstack(points_list)