# curve_type: quantized_logarithmic_spiral
# description: Logarithmic spiral with angle quantization for smooth space-filling
import numpy as np
N = 1000
# --- parameters ---
num_turns = 50
growth_rate = 0.20
num_discrete_angles = 140
# --- curve generation ---
max_theta = num_turns * 2 * np.pi
theta_continuous = np.linspace(0, max_theta, N)
angle_step = 2 * np.pi / num_discrete_angles
theta = np.round(theta_continuous / angle_step) * angle_step
r_raw = np.exp(theta * growth_rate / max_theta) - 1
r_max = np.exp(growth_rate) - 1
r = r_raw / r_max
x = 0.5 + 0.5 * r * np.cos(theta)
y = 0.5 + 0.5 * r * np.sin(theta)
points = np.column_stack([x, y])