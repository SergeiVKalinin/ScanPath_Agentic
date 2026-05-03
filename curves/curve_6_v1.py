# curve_type: spiral
# description: Logarithmic spiral with tangential sinusoidal wobble
import numpy as np
N = 22000
# --- parameters ---
spiral_growth = 0.2  # logarithmic growth factor
spiral_turns = 4
wobble_amplitude = 0.06  # 6% tangential wobble
wobble_frequency = 35  # wobble cycles

t = np.linspace(0, 1, N)
# Main logarithmic spiral
theta = 2 * np.pi * spiral_turns * t
r = 0.1 * np.exp(spiral_growth * theta)
r = r / np.max(r) * 0.45  # Normalize to fit in [0,1]
# Convert to Cartesian
x_base = 0.5 + r * np.cos(theta)
y_base = 0.5 + r * np.sin(theta)
# Add tangential wobble
wobble = wobble_amplitude * np.sin(2 * np.pi * wobble_frequency * t)
x = x_base + wobble * (-np.sin(theta))
y = y_base + wobble * np.cos(theta)
# Normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])