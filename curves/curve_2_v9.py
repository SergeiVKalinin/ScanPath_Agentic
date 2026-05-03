# curve_type: parallel_lines_perturbed
# description: Amplitude modulation with time-varying perturbations, inspired by curve_2_v7
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
# Quad-frequency system with amplitude modulation
x_primary_freq = 19
x_primary_amp_base = 0.009
x_secondary_freq = 31
x_secondary_amp_base = 0.004
y_primary_freq = 23
y_primary_amp_base = 0.007
y_secondary_freq = 37
y_secondary_amp_base = 0.003
# Modulation parameters
mod_freq = 3
mod_depth = 0.3
# Generate points
points_list = []
for i in range(num_lines):
    base_y = i / (num_lines - 1)
    t = np.linspace(0, 1, N // num_lines + 1)
    x = t.copy()
    y = np.full_like(t, base_y)
    # Time-varying amplitudes
    x_primary_amp = x_primary_amp_base * (1 + mod_depth * np.sin(2 * np.pi * mod_freq * t))
    x_secondary_amp = x_secondary_amp_base * (1 + mod_depth * np.sin(2 * np.pi * mod_freq * t))
    y_primary_amp = y_primary_amp_base * (1 + mod_depth * np.sin(2 * np.pi * mod_freq * t))
    y_secondary_amp = y_secondary_amp_base * (1 + mod_depth * np.sin(2 * np.pi * mod_freq * t))
    # Apply modulated perturbations
    x += x_primary_amp * np.sin(2 * np.pi * x_primary_freq * t)
    x += x_secondary_amp * np.sin(2 * np.pi * x_secondary_freq * t)
    y += y_primary_amp * np.sin(2 * np.pi * y_primary_freq * t)
    y += y_secondary_amp * np.sin(2 * np.pi * y_secondary_freq * t)
    points_list.append(np.column_stack([x, y]))
points = np.vstack(points_list)
points[:, 0] = np.clip(points[:, 0], 0, 1)
points[:, 1] = np.clip(points[:, 1], 0, 1)