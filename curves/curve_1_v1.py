# curve_type: raster
# description: basic raster scan pattern
import numpy as np
N = 1000
# --- parameters ---
rows = 20  # number of horizontal lines
# --- curve generation ---
t = np.linspace(0, rows, N)
row = np.floor(t)
x = t - row
y = row / rows
# reverse direction on odd rows for continuous path
mask = (row % 2) == 1
x[mask] = 1 - x[mask]
points = np.column_stack([x, y])