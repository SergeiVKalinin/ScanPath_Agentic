# curve_type: hybrid
# description: Fermat spiral outer region transitioning to dense serpentine center
import numpy as np
N = 10000
# --- parameters ---
outer_fraction = 0.60  # 60% points in spiral
inner_fraction = 0.40  # 40% points in raster
n_spiral = int(N * outer_fraction)
n_raster = N - n_spiral
# Fermat spiral for outer region
num_turns_spiral = 30
theta_spiral = np.linspace(0, num_turns_spiral * 2 * np.pi, n_spiral)
r_spiral = np.sqrt(theta_spiral / (num_turns_spiral * 2 * np.pi)) * 0.5
x_spiral = 0.5 + r_spiral * np.cos(theta_spiral)
y_spiral = 0.5 + r_spiral * np.sin(theta_spiral)
# Dense serpentine for center (r < 0.4)
num_lines_center = 50
points_per_line_center = n_raster // num_lines_center
center_points_list = []
for i in range(num_lines_center):
    # Map to center region [0.1, 0.9] x [0.1, 0.9]
    y_coord = 0.1 + 0.8 * i / (num_lines_center - 1)
    if i % 2 == 0:
        x_coords = np.linspace(0.1, 0.9, points_per_line_center)
    else:
        x_coords = np.linspace(0.9, 0.1, points_per_line_center)
    y_coords = np.full(points_per_line_center, y_coord)
    center_points_list.append(np.column_stack([x_coords, y_coords]))
raster_points = np.vstack(center_points_list)
# Combine spiral then raster
x = np.concatenate([x_spiral, raster_points[:, 0]])
y = np.concatenate([y_spiral, raster_points[:, 1]])
points = np.column_stack([x, y])