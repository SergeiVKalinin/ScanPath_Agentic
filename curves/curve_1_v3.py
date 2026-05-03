# curve_type: optimized_fermat_spiral
# description: Fermat spiral with tuned power-law spacing (p=0.48) and 60 turns for improved smoothness
import numpy as np
N = 1000
# --- parameters ---
num_turns = 60
power = 0.48  # slightly below sqrt for smoother transitions
max_theta = num_turns * 2 * np.pi

theta = np.linspace(0, max_theta, N)
r = np.power(theta / max_theta, power)

x = 0.5 + 0.5 * r * np.cos(theta)
y = 0.5 + 0.5 * r * np.sin(theta)
points = np.column_stack([x, y])