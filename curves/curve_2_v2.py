# curve_type: variable_density_serpentine
# description: bidirectional serpentine with denser spacing at edges
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100
edge_density_factor = 1.5

# create non-uniform line spacing (denser at edges)
line_indices = np.arange(num_lines)
normalized = line_indices / (num_lines - 1)
# quadratic spacing: denser at 0 and 1
spacing_weights = 1 + edge_density_factor * (4 * (normalized - 0.5)**2)
cumulative = np.cumsum(spacing_weights)
y_positions = (cumulative - cumulative[0]) / (cumulative[-1] - cumulative[0])

x = np.zeros(N)
y = np.zeros(N)
points_per_line = N // num_lines

for i in range(num_lines):
    start_idx = i * points_per_line
    end_idx = start_idx + points_per_line
    
    if i % 2 == 0:
        x[start_idx:end_idx] = np.linspace(0, 1, points_per_line)
    else:
        x[start_idx:end_idx] = np.linspace(1, 0, points_per_line)
    
    y[start_idx:end_idx] = y_positions[i]

points = np.column_stack([x, y])