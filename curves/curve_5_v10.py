# curve_type: parallel_lines_with_perturbations
# description: Hybrid coupling system with asymmetric bidirectional coupling
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
x_amp_1 = 0.010
x_freq_1 = 19
x_amp_2 = 0.004
x_freq_2 = 37
y_amp_1 = 0.009
y_freq_1 = 23
y_amp_2 = 0.003
y_freq_2 = 41
coupling_amp = 0.004
coupling_freq = 13
coupling_amp_2 = 0.003
coupling_freq_2 = 19
# --- generation ---
x = np.linspace(0, 1, num_lines)
y = np.linspace(0, 1, num_lines)
x += x_amp_1 * np.sin(2 * np.pi * x_freq_1 * x)
x += x_amp_2 * np.sin(2 * np.pi * x_freq_2 * x)
y += y_amp_1 * np.sin(2 * np.pi * y_freq_1 * y)
y += y_amp_2 * np.sin(2 * np.pi * y_freq_2 * y)
x += coupling_amp * np.sin(2 * np.pi * coupling_freq * (x + y))
y += coupling_amp_2 * np.sin(2 * np.pi * coupling_freq_2 * (x - y))
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])