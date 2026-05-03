# curve_type: lissajous
# description: Lissajous 99:98 ratio, phase=0
import numpy as np
N = 30000
# --- parameters ---
fx = 99  # x frequency
fy = 98  # y frequency
phase = 0  # phase offset in radians

t = np.linspace(0, 2 * np.pi * fy, N)
x = np.sin(fx * t / fy)
y = np.sin(t + phase)

# Normalize to [0, 1]
x = (x + 1) / 2
y = (y + 1) / 2

points = np.column_stack([x, y])