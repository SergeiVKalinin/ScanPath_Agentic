# curve_type: serpentine
# description: Phase-shifted perturbations for decorrelated oscillations
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
perturbation_x_amp = 0.011
perturbation_x_freq = 18
phase_x = 0.0
perturbation_y_amp = 0.008
perturbation_y_freq = 22
phase_y = np.pi / 3
coupled_amp = 0.005
coupled_freq = 13
phase_coupled = np.pi / 2

t = np.linspace(0, 1, N)
line_indices = np.floor(t * num_lines).astype(int)
line_indices = np.clip(line_indices, 0, num_lines - 1)
progress_in_line = (t * num_lines) % 1

y = line_indices / (num_lines - 1)
x = np.where(line_indices % 2 == 0, progress_in_line, 1 - progress_in_line)

# Phase-shifted independent perturbations
x += perturbation_x_amp * np.sin(2 * np.pi * perturbation_x_freq * t + phase_x)
y += perturbation_y_amp * np.sin(2 * np.pi * perturbation_y_freq * t + phase_y)

# Phase-shifted coupled perturbation
x += coupled_amp * np.sin(2 * np.pi * coupled_freq * (x + y) + phase_coupled)

x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])