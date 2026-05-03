# curve_type: parallel_lines_perturbed
# description: Extended prime frequency set with 6 components, inspired by curve_5_v7
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
# Six-frequency prime system: 13, 17, 23, 29, 37, 43
x_amp_1 = 0.009
x_freq_1 = 13
x_amp_2 = 0.006
x_freq_2 = 23
x_amp_3 = 0.004
x_freq_3 = 37
y_amp_1 = 0.007
y_freq_1 = 17
y_amp_2 = 0.005
y_freq_2 = 29
y_amp_3 = 0.003
y_freq_3 = 43
# Coupled perturbation
coupled_amp = 0.004
coupled_freq = 19
# Generate points
points_list = []
for i in range(num_lines):
    base_y = i / (num_lines - 1)
    t = np.linspace(0, 1, N // num_lines + 1)
    x = t.copy()
    y = np.full_like(t, base_y)
    # Apply six-frequency perturbations
    x += x_amp_1 * np.sin(2 * np.pi * x_freq_1 * t)
    x += x_amp_2 * np.sin(2 * np.pi * x_freq_2 * t)
    x += x_amp_3 * np.sin(2 * np.pi * x_freq_3 * t)
    y += y_amp_1 * np.sin(2 * np.pi * y_freq_1 * t)
    y += y_amp_2 * np.sin(2 * np.pi * y_freq_2 * t)
    y += y_amp_3 * np.sin(2 * np.pi * y_freq_3 * t)
    # Coupled term
    y += coupled_amp * np.sin(2 * np.pi * coupled_freq * (x + y))
    points_list.append(np.column_stack([x, y]))
points = np.vstack(points_list)
points[:, 0] = np.clip(points[:, 0], 0, 1)
points[:, 1] = np.clip(points[:, 1], 0, 1)