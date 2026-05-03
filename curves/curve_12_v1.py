# curve_type: spiral
# description: Fermat/parabolic spiral (sqrt spacing, outward)
import numpy as np
N = 10000
# --- parameters ---
num_turns = 50  # number of complete rotations
c = 1 / np.sqrt(2 * np.pi * num_turns)  # scaling parameter

theta = np.linspace(0, 2 * np.pi * num_turns, N)
r = c * np.sqrt(theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

# Normalize to [0, 1]
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())

points = np.column_stack([x, y])