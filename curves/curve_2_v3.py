# curve_type: hybrid_serpentine_spiral
# description: Outer bidirectional raster transitions to inner spiral at r=0.5 boundary
import numpy as np
N = 1000
# --- parameters ---
num_lines = 65
transition_radius = 0.5
outer_points = int(0.7 * N)
inner_points = N - outer_points

# Outer region: bidirectional raster
y_lines = np.linspace(0, 1, num_lines)
x_coords = []
y_coords = []
total_outer = 0

for i, y_val in enumerate(y_lines):
    points_this_line = max(1, int(outer_points / num_lines))
    if i % 2 == 0:
        x_line = np.linspace(0, 1, points_this_line)
    else:
        x_line = np.linspace(1, 0, points_this_line)
    x_coords.extend(x_line)
    y_coords.extend([y_val] * points_this_line)
    total_outer += points_this_line
    if total_outer >= outer_points:
        break

# Inner region: spiral from transition radius to center
num_turns_inner = 15
theta_inner = np.linspace(0, num_turns_inner * 2 * np.pi, inner_points)
r_inner = transition_radius * (1 - np.sqrt(theta_inner / (num_turns_inner * 2 * np.pi)))

x_inner = 0.5 + r_inner * np.cos(theta_inner)
y_inner = 0.5 + r_inner * np.sin(theta_inner)

x = np.concatenate([x_coords[:outer_points], x_inner])[:N]
y = np.concatenate([y_coords[:outer_points], y_inner])[:N]
points = np.column_stack([x, y])