# curve_type: spiral
# description: Archimedean spiral with sinusoidal radial wobble
import numpy as np
N = 15000
# --- parameters ---
spiral_turns = 5
wobble_amplitude = 0.05  # 5% radial wobble
wobble_frequency = 30  # wobble cycles

t = np.linspace(0, 1, N)
# Main Archimedean spiral
theta = 2 * np.pi * spiral_turns * t
r = 0.5 * t
# Add sinusoidal radial wobble
r += wobble_amplitude * np.sin(2 * np.pi * wobble_frequency * t)
# Convert to Cartesian
x = 0.5 + r * np.cos(theta)
y = 0.5 + r * np.sin(theta)
# Normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])