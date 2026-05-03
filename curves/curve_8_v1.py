# curve_type: square_spiral
# description: square spiral from center outward
import numpy as np
N = 1000
# --- parameters ---
turns = 8  # number of turns
# --- curve generation ---
segments = turns * 4
points_list = []
x, y = 0.5, 0.5
direction = 0  # 0: right, 1: up, 2: left, 3: down
step_size = 0.5 / turns
for i in range(segments):
    steps = (i // 2) + 1
    for _ in range(max(1, int(N / segments))):
        points_list.append([x, y])
        if direction == 0:
            x += step_size / (N / segments)
        elif direction == 1:
            y += step_size / (N / segments)
        elif direction == 2:
            x -= step_size / (N / segments)
        else:
            y -= step_size / (N / segments)
    direction = (direction + 1) % 4

points_list = np.array(points_list)
t_original = np.linspace(0, 1, len(points_list))
t_new = np.linspace(0, 1, N)
x = np.interp(t_new, t_original, points_list[:, 0])
y = np.interp(t_new, t_original, points_list[:, 1])
points = np.column_stack([x, y])