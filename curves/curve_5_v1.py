# curve_type: raster
# description: Vertical raster scan with large amplitude spiral wobble
import numpy as np
N = 18000
# --- parameters ---
lines = 40  # number of vertical lines
wobble_amplitude = 0.15  # 15% wobble (large)
wobble_frequency = 25  # wobble cycles

t = np.linspace(0, 1, N)
# Main vertical raster scan
line_idx = np.floor(t * lines)
x = line_idx / lines
# Alternate direction for each line
y = np.where(line_idx % 2 == 0, t * lines - line_idx, 1 - (t * lines - line_idx))
# Add large spiral wobble
theta = 2 * np.pi * wobble_frequency * t * lines
r = wobble_amplitude * (t ** 0.5)  # Growing wobble radius
x += r * np.cos(theta)
y += r * np.sin(theta)
# Normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])