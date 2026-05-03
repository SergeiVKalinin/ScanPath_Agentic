# curve_type: serpentine
# description: Triple-density serpentine with aggressive center focus
import numpy as np
N = 10000
# --- parameters ---
total_lines = 150
# Distribution: 30 bottom, 90 middle, 30 top
lines_bottom = 30
lines_middle = 90
lines_top = 30
# Allocate points proportionally to line density
points_bottom = N // 6  # sparse region
points_middle = 4 * N // 6  # dense region (4x)
points_top = N // 6  # sparse region
# Adjust for exact N
points_middle += N - (points_bottom + points_middle + points_top)
# Bottom third (0 to 0.33)
points_list = []
ppl_bottom = points_bottom // lines_bottom
for i in range(lines_bottom):
    y_coord = 0.33 * i / (lines_bottom - 1)
    if i % 2 == 0:
        x_coords = np.linspace(0, 1, ppl_bottom)
    else:
        x_coords = np.linspace(1, 0, ppl_bottom)
    y_coords = np.full(ppl_bottom, y_coord)
    points_list.append(np.column_stack([x_coords, y_coords]))
# Middle third (0.33 to 0.67)
ppl_middle = points_middle // lines_middle
for i in range(lines_middle):
    y_coord = 0.33 + 0.34 * i / (lines_middle - 1)
    if (lines_bottom + i) % 2 == 0:
        x_coords = np.linspace(0, 1, ppl_middle)
    else:
        x_coords = np.linspace(1, 0, ppl_middle)
    y_coords = np.full(ppl_middle, y_coord)
    points_list.append(np.column_stack([x_coords, y_coords]))
# Top third (0.67 to 1.0)
ppl_top = points_top // lines_top
for i in range(lines_top):
    y_coord = 0.67 + 0.33 * i / (lines_top - 1)
    if (lines_bottom + lines_middle + i) % 2 == 0:
        x_coords = np.linspace(0, 1, ppl_top)
    else:
        x_coords = np.linspace(1, 0, ppl_top)
    y_coords = np.full(ppl_top, y_coord)
    points_list.append(np.column_stack([x_coords, y_coords]))
points = np.vstack(points_list)