# curve_type: raster
# description: Rotated raster scan (45 degrees)
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100  # number of scan lines
points_per_line = N // num_lines
angle = np.pi / 4  # 45 degrees rotation

x = np.zeros(N)
y = np.zeros(N)

for i in range(num_lines):
    start_idx = i * points_per_line
    end_idx = start_idx + points_per_line
    # Create line in standard orientation
    x_temp = np.linspace(0, 1, points_per_line)
    y_temp = np.full(points_per_line, i / (num_lines - 1))
    
    # Rotate and center
    x_rot = x_temp * np.cos(angle) - y_temp * np.sin(angle)
    y_rot = x_temp * np.sin(angle) + y_temp * np.cos(angle)
    
    x[start_idx:end_idx] = x_rot
    y[start_idx:end_idx] = y_rot

# Normalize to [0, 1]
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())

points = np.column_stack([x, y])