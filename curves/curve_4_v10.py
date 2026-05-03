# curve_type: serpentine_sinusoidal
# description: Frequency gap optimization with 7-unit separation
import numpy as np
N = 1000
# --- parameters ---
num_lines = 350
x_amp = 0.0045
y_amp = 0.0028
x_freq = 18
y_freq = 25
# --- curve generation ---
t = np.linspace(0, 1, N)
line_progress = t * num_lines
line_index = np.floor(line_progress)
within_line = line_progress - line_index
x = np.where(line_index % 2 == 0, within_line, 1 - within_line)
y = line_index / num_lines
x += x_amp * np.sin(2 * np.pi * x_freq * t)
y += y_amp * np.sin(2 * np.pi * y_freq * t)
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])