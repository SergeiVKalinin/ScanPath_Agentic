# curve_type: serpentine_strong_coupling
# description: 350 lines with strong coupled dynamics to boost time uniformity
import numpy as np
N = 1000
# --- parameters ---
num_lines = 350
x_amp = 0.0095
y_amp = 0.0065
x_freq = 17
y_freq = 23
coupled_amp = 0.006
coupled_freq = 11

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
    
    coupled_offset = coupled_amp * np.sin(2 * np.pi * coupled_freq * (x[i] + y[i]))
    x[i] += coupled_offset
    y[i] += coupled_offset

x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])