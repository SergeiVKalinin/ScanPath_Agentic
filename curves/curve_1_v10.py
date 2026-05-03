# curve_type: parallel_lines_with_perturbations
# description: Extended multi-frequency system with 7 total perturbations (3 per axis + coupling)
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
x_amp_1 = 0.010
x_freq_1 = 19
x_amp_2 = 0.004
x_freq_2 = 37
x_amp_3 = 0.002
x_freq_3 = 43
y_amp_1 = 0.009
y_freq_1 = 23
y_amp_2 = 0.003
y_freq_2 = 41
y_amp_3 = 0.002
y_freq_3 = 47
coupled_amp = 0.004
coupled_freq = 13
# --- generation ---
x = np.linspace(0, 1, num_lines)
y = np.linspace(0, 1, num_lines)
x += x_amp_1 * np.sin(2 * np.pi * x_freq_1 * x)
x += x_amp_2 * np.sin(2 * np.pi * x_freq_2 * x)
x += x_amp_3 * np.sin(2 * np.pi * x_freq_3 * x)
y += y_amp_1 * np.sin(2 * np.pi * y_freq_1 * y)
y += y_amp_2 * np.sin(2 * np.pi * y_freq_2 * y)
y += y_amp_3 * np.sin(2 * np.pi * y_freq_3 * y)
x += coupled_amp * np.sin(2 * np.pi * coupled_freq * (x + y))
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])