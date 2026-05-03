# curve_type: spiral
# description: Fermat spiral (parabolic spacing)
import numpy as np
N = 10000
# --- parameters ---
num_turns = 50  # number of complete rotations
# --- generate curve ---
theta = np.linspace(0, num_turns * 2 * np.pi, N)
r = np.sqrt(theta / (num_turns * 2 * np.pi))
x = 0.5 + 0.5 * r * np.cos(theta)
y = 0.5 + 0.5 * r * np.sin(theta)
points = np.column_stack([x, y])