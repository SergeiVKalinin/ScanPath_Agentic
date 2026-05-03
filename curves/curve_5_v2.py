# curve_type: adaptive_center_weighted_serpentine
# description: serpentine with more points per line in center, fewer at edges
import numpy as np
N = 10000
# --- parameters ---
num_lines = 100
center_weight = 2.0

# calculate points per line with quadratic weighting toward center
line_indices = np.arange(num_lines)
normalized = line_indices / (num_lines - 1)
# quadratic weight: peaks at center (0.5)
weights = 1 + center_weight * (1 - 4 * (normalized - 0.5)**2)
weights = weights / weights.sum() * N
points_per_line = np.round(weights).astype(int)

# adjust to ensure sum equals N
diff = N - points_per_line.sum()
if diff > 0:
    points_per_line[num_lines // 2:num_lines // 2 + diff] += 1
elif diff < 0:
    points_per_line[0:-diff] -= 1

x = []
y = []

for i in range(num_lines):
    y_pos = i / (num_lines - 1)
    n_points = points_per_line[i]
    
    if n_points > 0:
        if i % 2 == 0:
            x_line = np.linspace(0, 1, n_points)
        else:
            x_line = np.linspace(1, 0, n_points)
        
        x.extend(x_line)
        y.extend([y_pos] * n_points)

x = np.array(x)
y = np.array(y)
points = np.column_stack([x, y])