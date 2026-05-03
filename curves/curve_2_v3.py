# curve_type: optimized_fermat_spiral
# description: Fermat spiral with refined exponent for better time uniformity
import numpy as np
N = 10000
# --- parameters ---
num_turns = 42  # slightly reduced from 50
spacing_exponent = 0.57  # between 0.5 and 0.6 for optimization

theta = np.linspace(0, num_turns * 2 * np.pi, N)
r = theta ** spacing_exponent

# normalize radius to fit in unit circle
r_max = (num_turns * 2 * np.pi) ** spacing_exponent
r = r / r_max * 0.5  # scale to radius 0.5

# convert to Cartesian coordinates centered at (0.5, 0.5)
x = 0.5 + r * np.cos(theta)
y = 0.5 + r * np.sin(theta)

# ensure bounds [0, 1]
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)

points = np.column_stack([x, y])