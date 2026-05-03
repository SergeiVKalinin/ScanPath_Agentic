# curve_type: circle
# description: simple circular path
import numpy as np
N = 1000
# --- parameters ---
radius = 0.4  # circle radius
center_x = 0.5  # center x coordinate
center_y = 0.5  # center y coordinate
# --- curve generation ---
t = np.linspace(0, 2 * np.pi, N)
x = center_x + radius * np.cos(t)
y = center_y + radius * np.sin(t)
points = np.column_stack([x, y])