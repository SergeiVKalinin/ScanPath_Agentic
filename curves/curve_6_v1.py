# curve_type: lissajous
# description: Lissajous 101:100 ratio, phase=0
import numpy as np
N = 30000
# --- parameters ---
fx = 101  # x frequency
fy = 100  # y frequency
phase = 0  # phase offset in radians

t = np.linspace(0, 2 * np.pi * fy, N)
x = np.sin(fx * t / fy)
y = np.sin(t + phase)

# Normalize to [0, 1]
x = (x + 1) / 2
y = (y + 1) / 2

points = np.column_stack([x, y])