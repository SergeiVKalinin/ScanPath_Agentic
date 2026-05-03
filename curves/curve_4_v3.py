# curve_type: elliptical_fermat_spiral
# description: Fermat spiral with elliptical aspect ratio a/b=0.9 to better fit unit square
import numpy as np
N = 1000
# --- parameters ---
num_turns = 52
aspect_ratio_a = 0.9
aspect_ratio_b = 1.0
max_theta = num_turns * 2 * np.pi

theta = np.linspace(0, max_theta, N)
r = np.sqrt(theta / max_theta)

x = 0.5 + 0.5 * aspect_ratio_a * r * np.cos(theta)
y = 0.5 + 0.5 * aspect_ratio_b * r * np.sin(theta)
points = np.column_stack([x, y])