# curve_type: serpentine
# description: Variable-density serpentine with adaptive line spacing, denser in outer regions
import numpy as np
N = 10000
# --- parameters ---
base_num_lines = 120
density_threshold = 0.7
outer_density_multiplier = 1.2

y_positions = []
for i in range(base_num_lines):
    y_val = i / (base_num_lines - 1)
    y_positions.append(y_val)
    if y_val > density_threshold:
        extra_lines = int((base_num_lines * outer_density_multiplier - base_num_lines) * (i / base_num_lines))
        if extra_lines > 0 and i < base_num_lines - 1:
            for j in range(1, min(extra_lines + 1, 3)):
                y_positions.append(y_val + j * 0.001)

y_positions = sorted(set(y_positions))
num_lines = len(y_positions)
points_per_line = N // num_lines

x = []
y = []
for i, y_val in enumerate(y_positions):
    if i % 2 == 0:
        x_line = np.linspace(0, 1, points_per_line)
    else:
        x_line = np.linspace(1, 0, points_per_line)
    
    y_line = np.full(points_per_line, y_val)
    x.extend(x_line)
    y.extend(y_line)

x = np.array(x[:N])
y = np.array(y[:N])
points = np.column_stack([x, y])