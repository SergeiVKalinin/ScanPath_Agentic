# curve_type: serpentine_sinusoidal
# description: Conservative enhancement - asymmetric x-amplitude reduction
import numpy as np
N = 1000
# --- parameters ---
num_lines = 350
x_amp = 0.0045  # further reduction targeting x-axis stability
y_amp = 0.003  # keep y_amp at optimal value
x_freq = 20
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