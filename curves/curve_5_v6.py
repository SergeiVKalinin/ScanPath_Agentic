# curve_type: serpentine
# description: Ultra-dense low-perturbation serpentine
import numpy as np
N = 1000
# --- parameters ---
num_lines = 400
x_perturb_amp = 0.006
x_perturb_freq = 21
y_perturb_amp = 0.005
y_perturb_freq = 19
# --- generation ---
t = np.linspace(0, 1, N)
line_idx = np.floor(t * num_lines).astype(int)
progress_in_line = (t * num_lines) - line_idx
x = np.where(line_idx % 2 == 0, progress_in_line, 1 - progress_in_line)
y = line_idx / num_lines
# apply minimal 2D perturbation
x += x_perturb_amp * np.sin(2 * np.pi * x_perturb_freq * t)
y += y_perturb_amp * np.sin(2 * np.pi * y_perturb_freq * t)
# boundary clipping
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])