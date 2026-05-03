# curve_type: serpentine_asymmetric_frequency
# description: 320 lines with large frequency differential between x and y
import numpy as np
N = 1000
# --- parameters ---
num_lines = 320
x_amp = 0.009
y_amp = 0.007
x_freq = 13
y_freq = 37

t = np.linspace(0, 1, N)
x = np.zeros(N)
y = np.zeros(N)

for i in range(N):
    line_idx = int(t[i] * num_lines)
    pos_in_line = (t[i] * num_lines) % 1.0
    
    if line_idx % 2 == 0:
        x[i] = pos_in_line
    else:
        x[i] = 1.0 - pos_in_line
    
    y[i] = line_idx / num_lines
    
    x[i] += x_amp * np.sin(2 * np.pi * x_freq * t[i])
    y[i] += y_amp * np.sin(2 * np.pi * y_freq * t[i])

x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])