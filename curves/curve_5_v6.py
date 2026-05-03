# curve_type: serpentine_sinusoidal
# description: Testing asymmetric amplitude reduction prioritizing x-stability with ratio 1.44
import numpy as np
N = 1000
# --- parameters ---
num_lines = 350
x_amp = 0.005  # Prioritized horizontal stability
y_amp = 0.006  # Slightly higher vertical perturbation
x_freq = 16    # Lower horizontal oscillation
y_freq = 23    # Ratio 1.44, balanced frequency separation
# --- curve generation ---
t = np.linspace(0, 1, N)
x = np.zeros(N)
y = np.zeros(N)
idx = 0
for line_idx in range(num_lines):
    y_base = line_idx / (num_lines - 1)
    line_t = np.linspace(0, 1, N // num_lines + (1 if line_idx < N % num_lines else 0))
    if line_idx % 2 == 0:
        x_line = line_t + x_amp * np.sin(2 * np.pi * x_freq * line_t)
        y_line = y_base + y_amp * np.sin(2 * np.pi * y_freq * line_t)
    else:
        x_line = (1 - line_t) + x_amp * np.sin(2 * np.pi * x_freq * line_t)
        y_line = y_base + y_amp * np.sin(2 * np.pi * y_freq * line_t)
    n_points = len(line_t)
    x[idx:idx+n_points] = x_line
    y[idx:idx+n_points] = y_line
    idx += n_points
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])