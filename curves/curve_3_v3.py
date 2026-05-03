# curve_type: serpentine_with_amplitude_optimization
# description: Optimized amplitude ratios with enhanced coupling strength
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
# Primary perturbations - optimized amplitudes
x_amp_1 = 0.007
x_freq_1 = 17
x_amp_2 = 0.003
x_freq_2 = 31
y_amp_1 = 0.008
y_freq_1 = 23
y_amp_2 = 0.003
y_freq_2 = 29
# Enhanced coupled perturbation
coupled_amp = 0.005
coupled_freq = 13
# Apply perturbations
x = x + x_amp_1 * np.sin(2 * np.pi * x_freq_1 * t)
x = x + x_amp_2 * np.sin(2 * np.pi * x_freq_2 * t)
y = y + y_amp_1 * np.sin(2 * np.pi * y_freq_1 * t)
y = y + y_amp_2 * np.sin(2 * np.pi * y_freq_2 * t)
x = x + coupled_amp * np.sin(2 * np.pi * coupled_freq * (x + y))
# Normalize to [0, 1]
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])