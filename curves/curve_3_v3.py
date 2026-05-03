# curve_type: variable_density_serpentine
# description: Serpentine with adaptive line spacing for regional density control
import numpy as np
N = 10000
# --- parameters ---
total_lines = 120
dense_spacing_factor = 1.5  # increase density in first/last 30%
transition_smoothness = 0.05  # smooth blending

t = np.linspace(0, 1, N)

# define variable line spacing function
def line_position(t_val):
    if t_val < 0.3:
        # denser in first 30%
        return t_val * 0.3 * dense_spacing_factor
    elif t_val < 0.7:
        # normal spacing in middle 40%
        return 0.3 * dense_spacing_factor + (t_val - 0.3) * 0.4
    else:
        # denser in last 30%
        return 0.3 * dense_spacing_factor + 0.4 + (t_val - 0.7) * 0.3 * dense_spacing_factor

# vectorize and apply
line_pos = np.array([line_position(tv) for tv in t])
line_pos = line_pos / line_pos[-1]  # normalize to [0, 1]

line_indices = np.floor(line_pos * total_lines).astype(int)
within_line = (line_pos * total_lines) - line_indices

# bidirectional serpentine
y = line_indices / total_lines
x = np.where(line_indices % 2 == 0, within_line, 1 - within_line)

# normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)

points = np.column_stack([x, y])