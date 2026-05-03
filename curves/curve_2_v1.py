# curve_type: spiral
# description: archimedean spiral from center outward
import numpy as np
N = 1000
# --- parameters ---
turns = 5  # number of complete rotations
a = 0.0  # starting radius
b = 0.5 / (2 * np.pi * turns)  # radius growth per radian
# --- curve generation ---
theta = np.linspace(0, 2 * np.pi * turns, N)
r = a + b * theta
x = 0.5 + r * np.cos(theta)
y = 0.5 + r * np.sin(theta)
points = np.column_stack([x, y])