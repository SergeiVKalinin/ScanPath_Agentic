# curve_type: serpentine_sinusoidal
# description: Micro-optimized amplitude with 7-unit frequency gap
import numpy as np
N = 1000
# --- parameters ---
x_amp = 0.0048
y_amp = 0.0029
x_freq = 19
y_freq = 26
num_lines = 350
# --- curve generation ---
t = np.linspace(0, 1, N)
x = np.zeros(N)
y = np.zeros(N)
for i in range(num_lines):
    line_progress = i / num_lines
    x += x_amp * np.sin(2 * np.pi * x_freq * t + line_progress * 2 * np.pi)
    y += line_progress / num_lines + y_amp * np.sin(2 * np.pi * y_freq * t + line_progress * 2 * np.pi)
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())
points = np.column_stack([x, y])