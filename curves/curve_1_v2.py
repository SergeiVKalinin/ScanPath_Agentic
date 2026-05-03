# curve_type: hybrid_serpentine_spiral
# description: serpentine raster transitioning to spiral in outer regions
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100
spiral_blend_factor = 0.3
transition_y = 0.6
points_per_line = N // num_lines

x = np.zeros(N)
y = np.zeros(N)

for i in range(num_lines):
    y_pos = i / (num_lines - 1)
    start_idx = i * points_per_line
    end_idx = start_idx + points_per_line
    
    # base serpentine x coordinates
    if i % 2 == 0:
        x_line = np.linspace(0, 1, points_per_line)
    else:
        x_line = np.linspace(1, 0, points_per_line)
    
    # blend with spiral in outer regions
    if y_pos > transition_y:
        blend = (y_pos - transition_y) / (1 - transition_y) * spiral_blend_factor
        theta = np.linspace(0, 2 * np.pi, points_per_line)
        radius = y_pos * 0.5
        spiral_x = 0.5 + radius * np.cos(theta + i * 0.2)
        spiral_y = 0.5 + radius * np.sin(theta + i * 0.2)
        x_line = (1 - blend) * x_line + blend * spiral_x
        y_pos = (1 - blend) * y_pos + blend * spiral_y
    
    x[start_idx:end_idx] = x_line
    y[start_idx:end_idx] = y_pos

# normalize to [0,1]
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])