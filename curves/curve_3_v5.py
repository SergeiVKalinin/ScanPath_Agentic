# curve_type: serpentine_sinusoidal_quadruple
# description: Quadruple frequency layering with 4 harmonic layers and coupling
import numpy as np
N = 1000
# --- parameters ---
num_lines = 350
x_amp1 = 0.006
x_freq1 = 18
y_amp1 = 0.005
y_freq1 = 24
x_amp2 = 0.002
x_freq2 = 32
y_amp2 = 0.002
y_freq2 = 30
x_amp3 = 0.001
x_freq3 = 42
y_amp3 = 0.001
y_freq3 = 38
x_amp4 = 0.0008
x_freq4 = 50
y_amp4 = 0.0008
y_freq4 = 46
coupled_amp = 0.002
coupled_freq = 14
t = np.linspace(0, 1, N)
line_indices = np.floor(t * num_lines).astype(int)
line_progress = (t * num_lines) % 1
x = np.where(line_indices % 2 == 0, line_progress, 1 - line_progress)
y = line_indices / num_lines
coupled_term = np.sin(2 * np.pi * coupled_freq * t)
x += x_amp1 * np.sin(2 * np.pi * x_freq1 * t)
x += x_amp2 * np.sin(2 * np.pi * x_freq2 * t)
x += x_amp3 * np.sin(2 * np.pi * x_freq3 * t)
x += x_amp4 * np.sin(2 * np.pi * x_freq4 * t)
x += coupled_amp * coupled_term
y += y_amp1 * np.sin(2 * np.pi * y_freq1 * t)
y += y_amp2 * np.sin(2 * np.pi * y_freq2 * t)
y += y_amp3 * np.sin(2 * np.pi * y_freq3 * t)
y += y_amp4 * np.sin(2 * np.pi * y_freq4 * t)
y += coupled_amp * coupled_term
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])