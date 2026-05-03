# curve_type: raster
# description: Rotated raster scan at 45 degrees
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100  # number of scan lines
points_per_line = N // num_lines
rotation_angle = 45  # degrees
# --- generate curve ---
x_rot = np.zeros(N)
y_rot = np.zeros(N)
for i in range(num_lines):
    start_idx = i * points_per_line
    end_idx = start_idx + points_per_line
    # generate line in original coordinates
    x_temp = np.linspace(-0.7071, 0.7071, points_per_line)
    y_temp = np.full(points_per_line, -0.7071 + i * 1.4142 / (num_lines - 1))
    # rotate by 45 degrees
    angle_rad = np.radians(rotation_angle)
    x_rot[start_idx:end_idx] = x_temp * np.cos(angle_rad) - y_temp * np.sin(angle_rad)
    y_rot[start_idx:end_idx] = x_temp * np.sin(angle_rad) + y_temp * np.cos(angle_rad)
# normalize to [0, 1]
x = (x_rot - x_rot.min()) / (x_rot.max() - x_rot.min())
y = (y_rot - y_rot.min()) / (y_rot.max() - y_rot.min())
points = np.column_stack([x, y])