# curve_type: spiral
# description: archimedean spiral from center outward
import numpy as np
N = 1000
# --- parameters ---
num_turns = 5  # number of complete rotations
# --- generation ---
t = np.linspace(0, 1, N)
theta = t * num_turns * 2 * np.pi
r = t * 0.5
x = 0.5 + r * np.cos(theta)
y = 0.5 + r * np.sin(theta)
points = np.column_stack([x, y])