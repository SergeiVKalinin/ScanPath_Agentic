# curve_type: serpentine_hybrid_optimal
# description: Hybrid combining 300 lines, 6 perturbations, and coupling for maximum uniformity
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
t = np.linspace(0, 1, N)
# Base serpentine pattern
line_idx = np.floor(t * num_lines)
x = (t * num_lines) % 1
y = line_idx / num_lines
# Reverse every other line
reverse_mask = (line_idx % 2 == 1)
x[reverse_mask] = 1 - x[reverse_mask]
# Triple-layer perturbations on x-axis
x_amp_1 = 0.008
x_freq_1 = 17
x_amp_2 = 0.003
x_freq_2 = 31
x_amp_3 = 0.002
x_freq_3 = 43
# Triple-layer perturbations on y-axis
y_amp_1 = 0.007
y_freq_1 = 23
y_amp_2 = 0.003
y_freq_2 = 29
y_amp_3 = 0.002
y_freq_3 = 47
# Coupled perturbation
coupled_amp = 0.004
coupled_freq = 13
# Apply all perturbations
x = x + x_amp_1 * np.sin(2 * np.pi * x_freq_1 * t)
x = x + x_amp_2 * np.sin(2 * np.pi * x_freq_2 * t)
x = x + x_amp_3 * np.sin(2 * np.pi * x_freq_3 * t)
y = y + y_amp_1 * np.sin(2 * np.pi * y_freq_1 * t)
y = y + y_amp_2 * np.sin(2 * np.pi * y_freq_2 * t)
y = y + y_amp_3 * np.sin(2 * np.pi * y_freq_3 * t)
x = x + coupled_amp * np.sin(2 * np.pi * coupled_freq * (x + y))
# Normalize to [0, 1]
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])