# curve_type: quantized_archimedean_spiral
# description: Archimedean spiral with angle quantization for improved uniformity
import numpy as np
N = 1000
# --- parameters ---
num_turns = 65
num_discrete_angles = 120
# --- curve generation ---
max_theta = num_turns * 2 * np.pi
theta_continuous = np.linspace(0, max_theta, N)
angle_step = 2 * np.pi / num_discrete_angles
theta = np.round(theta_continuous / angle_step) * angle_step
r = theta / max_theta
x = 0.5 + 0.5 * r * np.cos(theta)
y = 0.5 + 0.5 * r * np.sin(theta)
points = np.column_stack([x, y])