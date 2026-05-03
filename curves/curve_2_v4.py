# curve_type: fermat_spiral
# description: Optimized Fermat spiral with 75 turns for enhanced sample density uniformity
import numpy as np
N = 10000
# --- parameters ---
num_turns = 75
theta = np.linspace(0, num_turns * 2 * np.pi, N)
r = np.sqrt(theta / (num_turns * 2 * np.pi))

x = 0.5 + 0.5 * r * np.cos(theta)
y = 0.5 + 0.5 * r * np.sin(theta)
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])