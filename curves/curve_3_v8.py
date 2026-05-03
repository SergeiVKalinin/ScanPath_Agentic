# curve_type: serpentine_sinusoidal
# description: Amplitude ratio refinement - 1.67 ratio maintained between top performers
import numpy as np
N = 1000
# --- parameters ---
num_lines = 350
x_amp = 0.0055  # split difference between curve_1_v7 and curve_2_v7
y_amp = 0.0033  # maintain 1.67 amplitude ratio
x_freq = 19
y_freq = 24
# --- generation ---
x = np.zeros(N)
y = np.zeros(N)
for i in range(N):
    t = i / (N - 1)
    line_idx = t * num_lines
    line_progress = (line_idx % 1.0)
    if int(line_idx) % 2 == 0:
        x_base = line_progress
    else:
        x_base = 1.0 - line_progress
    y_base = int(line_idx) / num_lines
    x[i] = x_base + x_amp * np.sin(2 * np.pi * x_freq * t)
    y[i] = y_base + y_amp * np.sin(2 * np.pi * y_freq * t)
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])