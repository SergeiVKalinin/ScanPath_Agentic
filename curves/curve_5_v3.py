# curve_type: variable_density_bidirectional_raster
# description: Bidirectional raster with sinusoidal line density variation, denser at x=0.25 and x=0.75
import numpy as np
N = 1000
# --- parameters ---
num_lines = 100
density_peaks = 2

y_positions = np.linspace(0, 1, num_lines)
line_density = 1 + 0.5 * np.sin(density_peaks * 2 * np.pi * y_positions)
line_density = line_density / np.sum(line_density)

points_per_line = (line_density * N).astype(int)
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