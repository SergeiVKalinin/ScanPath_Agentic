# curve_type: serpentine_triple_frequency
# description: 350 lines with triple frequency layering per axis plus coupling
import numpy as np
N = 1000
# --- parameters ---
num_lines = 350
x_amp1 = 0.007
x_freq1 = 17
x_amp2 = 0.0025
x_freq2 = 31
x_amp3 = 0.002
x_freq3 = 41
y_amp1 = 0.006
y_freq1 = 23
y_amp2 = 0.0025
y_freq2 = 29
y_amp3 = 0.002
y_freq3 = 37
coupled_amp = 0.003
coupled_freq = 13

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
    
    x[i] += x_amp1 * np.sin(2 * np.pi * x_freq1 * t[i])
    x[i] += x_amp2 * np.sin(2 * np.pi * x_freq2 * t[i])
    x[i] += x_amp3 * np.sin(2 * np.pi * x_freq3 * t[i])
    
    y[i] += y_amp1 * np.sin(2 * np.pi * y_freq1 * t[i])
    y[i] += y_amp2 * np.sin(2 * np.pi * y_freq2 * t[i])
    y[i] += y_amp3 * np.sin(2 * np.pi * y_freq3 * t[i])
    
    coupled_offset = coupled_amp * np.sin(2 * np.pi * coupled_freq * t[i])
    x[i] += coupled_offset
    y[i] += coupled_offset

x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])