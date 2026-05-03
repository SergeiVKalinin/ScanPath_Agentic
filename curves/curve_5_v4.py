# curve_type: serpentine
# description: Double-frequency serpentine with 125 lines alternating point density for optimal time uniformity
import numpy as np
N = 10000
# --- parameters ---
num_lines = 125
points_per_line_low = 90
points_per_line_high = 110

x = []
y = []
points_added = 0
for i in range(num_lines):
    y_val = i / (num_lines - 1)
    
    if i % 2 == 0:
        points_this_line = points_per_line_high
    else:
        points_this_line = points_per_line_low
    
    if points_added + points_this_line > N:
        points_this_line = N - points_added
    
    if i % 2 == 0:
        x_line = np.linspace(0, 1, points_this_line)
    else:
        x_line = np.linspace(1, 0, points_this_line)
    
    y_line = np.full(points_this_line, y_val)
    x.extend(x_line)
    y.extend(y_line)
    
    points_added += points_this_line
    if points_added >= N:
        break

x = np.array(x[:N])
y = np.array(y[:N])
points = np.column_stack([x, y])