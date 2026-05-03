# curve_type: serpentine
# description: Phase-shifted dual serpentine with smooth transition
import numpy as np
N = 1000
# --- parameters ---
num_lines_per_half = 150
perturb_amp = 0.009
perturb_freq_1 = 17
perturb_freq_2 = 19
y_perturb_freq_1 = 23
y_perturb_freq_2 = 31
transition_width = 0.1
# --- generation ---
t = np.linspace(0, 1, N)
# sigmoid blending function for smooth transition
blend = 1 / (1 + np.exp(-(t - 0.5) / transition_width))
# first half: standard serpentine
t1 = t * 2
t1 = np.clip(t1, 0, 1)
line_idx_1 = np.floor(t1 * num_lines_per_half).astype(int)
progress_1 = (t1 * num_lines_per_half) - line_idx_1
x1 = np.where(line_idx_1 % 2 == 0, progress_1, 1 - progress_1)
y1 = line_idx_1 / num_lines_per_half
x1 += perturb_amp * np.sin(2 * np.pi * perturb_freq_1 * t)
y1 += perturb_amp * np.sin(2 * np.pi * y_perturb_freq_1 * t)
# second half: phase-shifted serpentine
t2 = (t - 0.5) * 2
t2 = np.clip(t2, 0, 1)
line_idx_2 = np.floor(t2 * num_lines_per_half).astype(int)
progress_2 = (t2 * num_lines_per_half) - line_idx_2
x2 = np.where(line_idx_2 % 2 == 1, progress_2, 1 - progress_2)
y2 = line_idx_2 / num_lines_per_half
x2 += perturb_amp * np.sin(2 * np.pi * perturb_freq_2 * t + np.pi)
y2 += perturb_amp * np.sin(2 * np.pi * y_perturb_freq_2 * t + np.pi)
# blend both halves
x = (1 - blend) * x1 + blend * x2
y = (1 - blend) * y1 + blend * y2
# boundary clipping
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])