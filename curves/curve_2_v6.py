# curve_type: serpentine
# description: Triple-axis perturbation with coupled XY term
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
x_perturb_amp = 0.011
x_perturb_freq = 19
y_perturb_amp = 0.007
y_perturb_freq = 29
coupled_amp = 0.004
coupled_freq = 13
# --- generation ---
t = np.linspace(0, 1, N)
line_idx = np.floor(t * num_lines).astype(int)
progress_in_line = (t * num_lines) - line_idx
x = np.where(line_idx % 2 == 0, progress_in_line, 1 - progress_in_line)
y = line_idx / num_lines
# apply independent perturbations
x += x_perturb_amp * np.sin(2 * np.pi * x_perturb_freq * t)
y += y_perturb_amp * np.sin(2 * np.pi * y_perturb_freq * t)
# add coupled XY perturbation term
x += coupled_amp * np.sin(coupled_freq * np.pi * (x + y))
# boundary clipping
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])