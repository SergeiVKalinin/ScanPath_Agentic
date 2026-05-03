# curve_type: parallel_lines_with_perturbations
# description: Amplitude gradient variation with evenly graduated amplitudes
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
x_amp_1 = 0.010
x_freq_1 = 19
x_amp_2 = 0.005
x_freq_2 = 37
y_amp_1 = 0.008
y_freq_1 = 23
y_amp_2 = 0.004
y_freq_2 = 41
coupled_amp = 0.003
coupled_freq = 13
# --- generation ---
x = np.linspace(0, 1, num_lines)
y = np.linspace(0, 1, num_lines)
x += x_amp_1 * np.sin(2 * np.pi * x_freq_1 * x)
x += x_amp_2 * np.sin(2 * np.pi * x_freq_2 * x)
y += y_amp_1 * np.sin(2 * np.pi * y_freq_1 * y)
y += y_amp_2 * np.sin(2 * np.pi * y_freq_2 * y)
x += coupled_amp * np.sin(2 * np.pi * coupled_freq * (x + y))
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])