# curve_type: raster
# description: Interlaced raster scan (odd lines then even lines)
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100  # number of scan lines
points_per_line = N // num_lines
# --- generate curve ---
x = np.zeros(N)
y = np.zeros(N)
half_lines = num_lines // 2
# odd lines (0, 2, 4, ...)
for i in range(half_lines):
    start_idx = i * points_per_line
    end_idx = start_idx + points_per_line
    x[start_idx:end_idx] = np.linspace(0, 1, points_per_line)
    y[start_idx:end_idx] = (2 * i) / (num_lines - 1)
# even lines (1, 3, 5, ...)
for i in range(half_lines):
    start_idx = (half_lines + i) * points_per_line
    end_idx = start_idx + points_per_line
    x[start_idx:end_idx] = np.linspace(0, 1, points_per_line)
    y[start_idx:end_idx] = (2 * i + 1) / (num_lines - 1)
points = np.column_stack([x, y])