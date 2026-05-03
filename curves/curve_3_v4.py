# curve_type: hybrid_spiral_raster
# description: Fermat spiral with quantized angles combining spiral smoothness and raster uniformity
import numpy as np
N = 10000
# --- parameters ---
num_turns = 60
num_discrete_angles = 120
max_theta = num_turns * 2 * np.pi

theta_continuous = np.linspace(0, max_theta, N)
angle_step = 2 * np.pi / num_discrete_angles
theta = np.round(theta_continuous / angle_step) * angle_step

r = np.sqrt(theta / max_theta)

x = 0.5 + 0.5 * r * np.cos(theta)
y = 0.5 + 0.5 * r * np.sin(theta)
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])