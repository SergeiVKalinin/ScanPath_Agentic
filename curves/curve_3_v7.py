# curve_type: serpentine
# description: Optimized variable density with enhanced dual-axis perturbation
import numpy as np
N = 1000
# --- parameters ---
num_lines = 250
density_exponent = 1.3
perturbation_x_amp = 0.011
perturbation_x_freq = 19
perturbation_y_amp = 0.008
perturbation_y_freq = 23

t = np.linspace(0, 1, N)
t_adjusted = t ** density_exponent
t_adjusted = t_adjusted / t_adjusted[-1]

line_indices = np.floor(t_adjusted * num_lines).astype(int)
line_indices = np.clip(line_indices, 0, num_lines - 1)
progress_in_line = (t_adjusted * num_lines) % 1

y = line_indices / (num_lines - 1)
x = np.where(line_indices % 2 == 0, progress_in_line, 1 - progress_in_line)

# Dual-axis perturbations
x += perturbation_x_amp * np.sin(2 * np.pi * perturbation_x_freq * t)
y += perturbation_y_amp * np.sin(2 * np.pi * perturbation_y_freq * t)

x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])