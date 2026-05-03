# curve_type: raster
# description: Interlaced raster scan (odd/even lines)
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100  # number of scan lines
points_per_line = N // num_lines

x = np.zeros(N)
y = np.zeros(N)

# First pass: odd lines
half_lines = num_lines // 2
points_per_pass = N // 2

for i in range(half_lines):
    start_idx = i * points_per_line
    end_idx = start_idx + points_per_line
    line_num = 2 * i
    x[start_idx:end_idx] = np.linspace(0, 1, points_per_line)
    y[start_idx:end_idx] = line_num / (num_lines - 1)

# Second pass: even lines
for i in range(half_lines):
    start_idx = points_per_pass + i * points_per_line
    end_idx = start_idx + points_per_line
    line_num = 2 * i + 1
    x[start_idx:end_idx] = np.linspace(0, 1, points_per_line)
    y[start_idx:end_idx] = line_num / (num_lines - 1)

points = np.column_stack([x, y])