# curve_type: raster
# description: Horizontal raster scan with small spiral wobble
import numpy as np
N = 10000
# --- parameters ---
lines = 50  # number of horizontal lines
wobble_amplitude = 0.01  # 1% wobble
wobble_frequency = 20  # wobble cycles per line

t = np.linspace(0, 1, N)
# Main raster scan
line_idx = np.floor(t * lines)
y = line_idx / lines
# Alternate direction for each line
x = np.where(line_idx % 2 == 0, t * lines - line_idx, 1 - (t * lines - line_idx))
# Add spiral wobble
theta = 2 * np.pi * wobble_frequency * t * lines
r = wobble_amplitude * t
x += r * np.cos(theta)
y += r * np.sin(theta)
# Normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])