# curve_type: smooth_raster_bezier
# description: Bidirectional raster with cubic Bezier curve transitions at turns
import numpy as np
N = 10000
# --- parameters ---
num_lines = 118
bezier_control_offset = 0.04  # smoothing strength
points_per_transition = 50  # points allocated to each turn

points_per_line = (N - (num_lines - 1) * points_per_transition) // num_lines
all_x = []
all_y = []

for i in range(num_lines):
    y_val = i / (num_lines - 1)
    
    # straight line portion
    if i % 2 == 0:
        line_x = np.linspace(0, 1 - bezier_control_offset, points_per_line)
    else:
        line_x = np.linspace(1, bezier_control_offset, points_per_line)
    
    line_y = np.full(points_per_line, y_val)
    all_x.extend(line_x)
    all_y.extend(line_y)
    
    # Bezier transition to next line
    if i < num_lines - 1:
        y_next = (i + 1) / (num_lines - 1)
        t_bez = np.linspace(0, 1, points_per_transition)
        
        if i % 2 == 0:
            # transition from right to left
            p0 = np.array([1 - bezier_control_offset, y_val])
            p1 = np.array([1, y_val + bezier_control_offset])
            p2 = np.array([1, y_next - bezier_control_offset])
            p3 = np.array([1, y_next])
        else:
            # transition from left to right
            p0 = np.array([bezier_control_offset, y_val])
            p1 = np.array([0, y_val + bezier_control_offset])
            p2 = np.array([0, y_next - bezier_control_offset])
            p3 = np.array([0, y_next])
        
        # cubic Bezier formula
        bez_points = (1-t_bez)[:, None]**3 * p0 + 3*(1-t_bez)[:, None]**2*t_bez[:, None] * p1 + 3*(1-t_bez)[:, None]*t_bez[:, None]**2 * p2 + t_bez[:, None]**3 * p3
        all_x.extend(bez_points[:, 0])
        all_y.extend(bez_points[:, 1])

# trim or pad to exact N points
x = np.array(all_x[:N])
y = np.array(all_y[:N])

# ensure [0, 1] bounds
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)

points = np.column_stack([x, y])