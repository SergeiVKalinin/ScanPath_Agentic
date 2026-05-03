# curve_type: serpentine_sinusoidal
# description: Asymmetric frequency ratio 1:1.56 testing larger frequency separation
import numpy as np
N = 1000
# --- parameters ---
num_lines = 350
x_amp = 0.008
y_amp = 0.006
x_freq = 18
y_freq = 28
t = np.linspace(0, 1, N)
line_indices = np.floor(t * num_lines).astype(int)
line_progress = (t * num_lines) % 1
x = np.where(line_indices % 2 == 0, line_progress, 1 - line_progress)
y = line_indices / num_lines
x += x_amp * np.sin(2 * np.pi * x_freq * t)
y += y_amp * np.sin(2 * np.pi * y_freq * t)
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])