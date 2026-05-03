# curve_type: parallel_lines_with_perturbations
# description: Optimized coupling exploration with symmetric coupling term
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
x_amp_1 = 0.012
x_freq_1 = 17
x_amp_2 = 0.004
x_freq_2 = 31
y_amp_1 = 0.010
y_freq_1 = 23
y_amp_2 = 0.003
y_freq_2 = 29
coupling_amp = 0.005
coupling_freq = 11
# --- generation ---
x = np.linspace(0, 1, num_lines)
y = np.linspace(0, 1, num_lines)
x += x_amp_1 * np.sin(2 * np.pi * x_freq_1 * x)
x += x_amp_2 * np.sin(2 * np.pi * x_freq_2 * x)
y += y_amp_1 * np.sin(2 * np.pi * y_freq_1 * y)
y += y_amp_2 * np.sin(2 * np.pi * y_freq_2 * y)
x += coupling_amp * np.sin(2 * np.pi * coupling_freq * (x + y))
y += coupling_amp * np.sin(2 * np.pi * coupling_freq * (x + y))
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])