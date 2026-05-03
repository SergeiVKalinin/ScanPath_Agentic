# curve_type: hybrid_raster_spiral
# description: Serpentine with radial modulation for smooth spiral-like transitions
import numpy as np
N = 10000
# --- parameters ---
num_lines = 125  # optimal range for density
radial_amplitude = 0.035  # modulation strength
radial_frequency = 3.0  # spiral-like cycles

t = np.linspace(0, 1, N)
line_indices = np.floor(t * num_lines).astype(int)
within_line = (t * num_lines) - line_indices

# base serpentine pattern
y = line_indices / num_lines
x = np.where(line_indices % 2 == 0, within_line, 1 - within_line)

# add radial modulation for smoothness
center_x, center_y = 0.5, 0.5
dx = x - center_x
dy = y - center_y
radius = np.sqrt(dx**2 + dy**2)
angle = np.arctan2(dy, dx)

# apply smooth radial perturbation
modulation = radial_amplitude * np.sin(radial_frequency * angle) * radius
x = x + modulation * np.cos(angle)
y = y + modulation * np.sin(angle)

# normalize to [0, 1]
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)

points = np.column_stack([x, y])