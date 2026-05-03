# curve_type: raster
# description: Standard unidirectional raster scan with flyback
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100  # number of scan lines
points_per_line = N // num_lines

x = np.zeros(N)
y = np.zeros(N)

for i in range(num_lines):
    start_idx = i * points_per_line
    end_idx = start_idx + points_per_line
    # Forward scan
    x[start_idx:end_idx] = np.linspace(0, 1, points_per_line)
    y[start_idx:end_idx] = i / (num_lines - 1)

points = np.column_stack([x, y])