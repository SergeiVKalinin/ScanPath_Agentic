# curve_type: raster
# description: Variable line spacing raster (denser in center)
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100  # number of scan lines
points_per_line = N // num_lines

x = np.zeros(N)
y = np.zeros(N)

# Create non-uniform y spacing (denser in center)
line_positions = np.linspace(-1, 1, num_lines)
line_positions = np.sign(line_positions) * np.abs(line_positions) ** 1.5
line_positions = (line_positions - line_positions.min()) / (line_positions.max() - line_positions.min())

for i in range(num_lines):
    start_idx = i * points_per_line
    end_idx = start_idx + points_per_line
    x[start_idx:end_idx] = np.linspace(0, 1, points_per_line)
    y[start_idx:end_idx] = line_positions[i]

points = np.column_stack([x, y])