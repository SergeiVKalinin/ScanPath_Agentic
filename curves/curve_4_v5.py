# curve_type: hybrid_serpentine_spiral
# description: Dense serpentine transitioning to quantized Fermat spiral
import numpy as np
N = 1000
# --- parameters ---
num_lines_serpentine = 150
num_turns_spiral = 30
num_discrete_angles = 100
# --- curve generation ---
N_half = N // 2
t1 = np.linspace(0, 1, N_half)
line_index = t1 * num_lines_serpentine
y1 = line_index / num_lines_serpentine
line_direction = (np.floor(line_index) % 2) * 2 - 1
position_in_line = line_index - np.floor(line_index)
x1 = np.where(line_direction > 0, position_in_line, 1 - position_in_line)
max_theta = num_turns_spiral * 2 * np.pi
theta_continuous = np.linspace(0, max_theta, N - N_half)
angle_step = 2 * np.pi / num_discrete_angles
theta = np.round(theta_continuous / angle_step) * angle_step
r = np.sqrt(theta / max_theta)
x2 = 0.5 + 0.5 * r * np.cos(theta)
y2 = 0.5 + 0.5 * r * np.sin(theta)
x = np.concatenate([x1, x2])
y = np.concatenate([y1, y2])
points = np.column_stack([x, y])