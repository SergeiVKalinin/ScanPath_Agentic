# curve_type: serpentine_sinusoidal
# description: Y-Amplitude Boost - testing symmetric amplitudes with safe mid-range frequencies
import numpy as np
N = 1000
# --- parameters ---
num_lines = 350
x_amp = 0.007
y_amp = 0.007
x_freq = 18
y_freq = 23
# --- curve generation ---
t = np.linspace(0, 1, N)
x = np.zeros(N)
y = np.zeros(N)
for i in range(N):
    line_idx = int(t[i] * num_lines)
    local_t = (t[i] * num_lines) - line_idx
    if line_idx % 2 == 0:
        x[i] = local_t
    else:
        x[i] = 1.0 - local_t
    y[i] = line_idx / num_lines
    x[i] += x_amp * np.sin(2 * np.pi * x_freq * t[i])
    y[i] += y_amp * np.sin(2 * np.pi * y_freq * t[i])
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])