# curve_type: diagonal_serpentine
# description: serpentine pattern rotated 45 degrees scanning diagonally
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100
points_per_line = N // num_lines

x = np.zeros(N)
y = np.zeros(N)

for i in range(num_lines):
    start_idx = i * points_per_line
    end_idx = start_idx + points_per_line
    
    # diagonal position (0 to sqrt(2))
    diag_pos = i / (num_lines - 1) * np.sqrt(2)
    
    # create line perpendicular to diagonal
    t = np.linspace(0, 1, points_per_line)
    if i % 2 == 1:
        t = t[::-1]
    
    # parametric diagonal line
    if diag_pos <= 1:
        # lower triangle
        x_base = diag_pos * t
        y_base = diag_pos * (1 - t)
    else:
        # upper triangle
        offset = diag_pos - 1
        x_base = offset + (1 - offset) * t
        y_base = 1 - (1 - offset) * (1 - t)
    
    x[start_idx:end_idx] = x_base
    y[start_idx:end_idx] = y_base

# normalize to [0,1]
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])