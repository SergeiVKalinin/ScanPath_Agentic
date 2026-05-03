# curve_type: parallel_lines_with_perturbations
# description: Ultra-prime frequency set with higher primes to reduce periodic artifacts
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
x_amp_1 = 0.012
x_freq_1 = 53
x_amp_2 = 0.004
x_freq_2 = 59
y_amp_1 = 0.010
y_freq_1 = 61
y_amp_2 = 0.003
y_freq_2 = 67
# --- generation ---
x = np.linspace(0, 1, num_lines)
y = np.linspace(0, 1, num_lines)
x += x_amp_1 * np.sin(2 * np.pi * x_freq_1 * x)
x += x_amp_2 * np.sin(2 * np.pi * x_freq_2 * x)
y += y_amp_1 * np.sin(2 * np.pi * y_freq_1 * y)
y += y_amp_2 * np.sin(2 * np.pi * y_freq_2 * y)
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])