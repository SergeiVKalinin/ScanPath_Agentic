# curve_type: serpentine
# description: Quad-frequency system with harmonic exploration on both axes
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
x_primary_amp = 0.009
x_primary_freq = 19
x_secondary_amp = 0.004
x_secondary_freq = 37
y_primary_amp = 0.007
y_primary_freq = 23
y_secondary_amp = 0.003
y_secondary_freq = 41

t = np.linspace(0, 1, N)
line_indices = np.floor(t * num_lines).astype(int)
line_indices = np.clip(line_indices, 0, num_lines - 1)
progress_in_line = (t * num_lines) % 1

y = line_indices / (num_lines - 1)
x = np.where(line_indices % 2 == 0, progress_in_line, 1 - progress_in_line)

# Dual X-axis perturbations
x += x_primary_amp * np.sin(2 * np.pi * x_primary_freq * t)
x += x_secondary_amp * np.sin(2 * np.pi * x_secondary_freq * t)

# Dual Y-axis perturbations
y += y_primary_amp * np.sin(2 * np.pi * y_primary_freq * t)
y += y_secondary_amp * np.sin(2 * np.pi * y_secondary_freq * t)

x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])