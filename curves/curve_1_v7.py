# curve_type: serpentine
# description: Enhanced coupled perturbation with multiplicative coupling term
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
perturbation_x_amp = 0.010
perturbation_x_freq = 17
perturbation_y_amp = 0.008
perturbation_y_freq = 23
coupled_add_amp = 0.005
coupled_add_freq = 11
coupled_mult_amp = 0.003
coupled_mult_freq = 13

t = np.linspace(0, 1, N)
line_indices = np.floor(t * num_lines).astype(int)
line_indices = np.clip(line_indices, 0, num_lines - 1)
progress_in_line = (t * num_lines) % 1

y = line_indices / (num_lines - 1)
x = np.where(line_indices % 2 == 0, progress_in_line, 1 - progress_in_line)

# Independent perturbations
x += perturbation_x_amp * np.sin(2 * np.pi * perturbation_x_freq * t)
y += perturbation_y_amp * np.sin(2 * np.pi * perturbation_y_freq * t)

# Additive coupled perturbation
x += coupled_add_amp * np.sin(2 * np.pi * coupled_add_freq * (x + y))

# Multiplicative coupled perturbation
y += coupled_mult_amp * np.sin(2 * np.pi * coupled_mult_freq * (x * y))

x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])