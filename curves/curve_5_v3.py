# curve_type: logarithmic_spiral
# description: Exponential spacing spiral as alternative to Fermat parabolic
import numpy as np
N = 10000
# --- parameters ---
num_turns = 10
b = 0.17  # exponential growth rate
center_x = 0.5
center_y = 0.5

theta = np.linspace(0, num_turns * 2 * np.pi, N)
r = np.exp(b * theta)

# normalize to fit within unit circle
r_max = np.exp(b * num_turns * 2 * np.pi)
r = r / r_max * 0.5  # scale to radius 0.5

# convert to Cartesian
x = center_x + r * np.cos(theta)
y = center_y + r * np.sin(theta)

# ensure [0, 1] bounds
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)

points = np.column_stack([x, y])