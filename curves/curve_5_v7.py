# curve_type: serpentine
# description: Ultra-high frequency diversity with five prime frequencies
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
x_amp_1 = 0.008
x_freq_1 = 17
x_amp_2 = 0.003
x_freq_2 = 31
y_amp_1 = 0.007
y_freq_1 = 23
y_amp_2 = 0.003
y_freq_2 = 29
coupled_amp = 0.004
coupled_freq = 13

t = np.linspace(0, 1, N)
line_indices = np.floor(t * num_lines).astype(int)
line_indices = np.clip(line_indices, 0, num_lines - 1)
progress_in_line = (t * num_lines) % 1

y = line_indices / (num_lines - 1)
x = np.where(line_indices % 2 == 0, progress_in_line, 1 - progress_in_line)

# Multiple frequency perturbations with all prime numbers
x += x_amp_1 * np.sin(2 * np.pi * x_freq_1 * t)
x += x_amp_2 * np.sin(2 * np.pi * x_freq_2 * t)
y += y_amp_1 * np.sin(2 * np.pi * y_freq_1 * t)
y += y_amp_2 * np.sin(2 * np.pi * y_freq_2 * t)

# Coupled perturbation
x += coupled_amp * np.sin(2 * np.pi * coupled_freq * (x + y))

x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])