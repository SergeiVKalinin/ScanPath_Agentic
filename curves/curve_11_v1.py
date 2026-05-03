# curve_type: spiral
# description: Archimedean spiral (constant spacing, outward)
import numpy as np
N = 10000
# --- parameters ---
num_turns = 50  # number of complete rotations
a = 0  # starting radius
b = 1 / (2 * np.pi * num_turns)  # spacing parameter

theta = np.linspace(0, 2 * np.pi * num_turns, N)
r = a + b * theta

x = r * np.cos(theta)
y = r * np.sin(theta)

# Normalize to [0, 1]
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())

points = np.column_stack([x, y])