# curve_type: serpentine
# description: Adaptive density serpentine with 2D perturbation
import numpy as np
N = 1000
# --- parameters ---
num_lines = 200
density_exponent = 1.8
x_perturb_amp = 0.010
x_perturb_freq = 16
y_perturb_amp = 0.008
y_perturb_freq = 20
# --- generation ---
t = np.linspace(0, 1, N)
# apply power-law spacing for adaptive density
t_warped = np.power(t, density_exponent)
line_idx = np.floor(t_warped * num_lines).astype(int)
progress_in_line = (t_warped * num_lines) - line_idx
x = np.where(line_idx % 2 == 0, progress_in_line, 1 - progress_in_line)
y = line_idx / num_lines
# apply 2D perturbation
x += x_perturb_amp * np.sin(2 * np.pi * x_perturb_freq * t)
y += y_perturb_amp * np.sin(2 * np.pi * y_perturb_freq * t)
# boundary clipping
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])