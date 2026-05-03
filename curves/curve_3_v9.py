# curve_type: parallel_lines_perturbed
# description: Higher frequency exploration with primes 53-71, inspired by curve_2_v5
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
# High-frequency prime system (53, 59, 61, 67)
x_primary_freq = 53
x_primary_amp = 0.007
x_secondary_freq = 61
x_secondary_amp = 0.004
y_primary_freq = 59
y_primary_amp = 0.006
y_secondary_freq = 67
y_secondary_amp = 0.003
# Generate points
points_list = []
for i in range(num_lines):
    base_y = i / (num_lines - 1)
    t = np.linspace(0, 1, N // num_lines + 1)
    x = t.copy()
    y = np.full_like(t, base_y)
    # Apply ultra-fine high-frequency perturbations
    x += x_primary_amp * np.sin(2 * np.pi * x_primary_freq * t)
    x += x_secondary_amp * np.sin(2 * np.pi * x_secondary_freq * t)
    y += y_primary_amp * np.sin(2 * np.pi * y_primary_freq * t)
    y += y_secondary_amp * np.sin(2 * np.pi * y_secondary_freq * t)
    points_list.append(np.column_stack([x, y]))
points = np.vstack(points_list)
points[:, 0] = np.clip(points[:, 0], 0, 1)
points[:, 1] = np.clip(points[:, 1], 0, 1)