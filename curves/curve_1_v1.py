# curve_type: raster
# description: basic raster scan pattern
import numpy as np
N = 1000
# --- parameters ---
num_lines = 20  # number of horizontal lines
# --- generation ---
t = np.linspace(0, 1, N)
line_idx = np.floor(t * num_lines)
y = line_idx / num_lines
# alternate direction per line
x = np.where(line_idx % 2 == 0, t * num_lines - line_idx, 1 - (t * num_lines - line_idx))
points = np.column_stack([x, y])