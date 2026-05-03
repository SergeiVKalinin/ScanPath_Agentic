# curve_type: parallel_lines_perturbed
# description: Triple-coupled system with sum, difference, and product terms, inspired by curve_5_v7
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
# Base perturbation frequencies (primes)
x_freq_1 = 17
x_amp_1 = 0.008
x_freq_2 = 29
x_amp_2 = 0.005
y_freq_1 = 19
y_amp_1 = 0.007
y_freq_2 = 31
y_amp_2 = 0.004
# Triple-coupled system
coupled_amp_1 = 0.003
coupled_freq_1 = 11
coupled_amp_2 = 0.002
coupled_freq_2 = 13
coupled_amp_3 = 0.002
coupled_freq_3 = 17
# Generate points
points_list = []
for i in range(num_lines):
    base_y = i / (num_lines - 1)
    t = np.linspace(0, 1, N // num_lines + 1)
    x = t.copy()
    y = np.full_like(t, base_y)
    # Base perturbations
    x += x_amp_1 * np.sin(2 * np.pi * x_freq_1 * t)
    x += x_amp_2 * np.sin(2 * np.pi * x_freq_2 * t)
    y += y_amp_1 * np.sin(2 * np.pi * y_freq_1 * t)
    y += y_amp_2 * np.sin(2 * np.pi * y_freq_2 * t)
    # Triple-coupled terms
    y += coupled_amp_1 * np.sin(2 * np.pi * coupled_freq_1 * (x + y))
    y += coupled_amp_2 * np.sin(2 * np.pi * coupled_freq_2 * (x - y))
    x += coupled_amp_3 * np.sin(2 * np.pi * coupled_freq_3 * (x * y))
    points_list.append(np.column_stack([x, y]))
points = np.vstack(points_list)
points[:, 0] = np.clip(points[:, 0], 0, 1)
points[:, 1] = np.clip(points[:, 1], 0, 1)