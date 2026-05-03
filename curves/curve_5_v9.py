# curve_type: parallel_lines_perturbed
# description: Asymmetric 3:1 harmonic frequency ratios, inspired by curve_2_v7
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
# Harmonic 3:1 frequency relationships
x_primary_freq = 15
x_primary_amp = 0.009
x_secondary_freq = 45
x_secondary_amp = 0.003
y_primary_freq = 21
y_primary_amp = 0.009
y_secondary_freq = 63
y_secondary_amp = 0.003
# Generate points
points_list = []
for i in range(num_lines):
    base_y = i / (num_lines - 1)
    t = np.linspace(0, 1, N // num_lines + 1)
    x = t.copy()
    y = np.full_like(t, base_y)
    # Apply harmonic perturbations with 3:1 ratio
    x += x_primary_amp * np.sin(2 * np.pi * x_primary_freq * t)
    x += x_secondary_amp * np.sin(2 * np.pi * x_secondary_freq * t)
    y += y_primary_amp * np.sin(2 * np.pi * y_primary_freq * t)
    y += y_secondary_amp * np.sin(2 * np.pi * y_secondary_freq * t)
    points_list.append(np.column_stack([x, y]))
points = np.vstack(points_list)
points[:, 0] = np.clip(points[:, 0], 0, 1)
points[:, 1] = np.clip(points[:, 1], 0, 1)