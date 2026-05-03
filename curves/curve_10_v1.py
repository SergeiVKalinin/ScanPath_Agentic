# curve_type: lissajous
# description: Lissajous curve with frequency ratio 51:50, phase 0
import numpy as np
N = 25000
# --- parameters ---
fx = 51  # x frequency
fy = 50  # y frequency
phase = 0  # phase offset in radians
# --- generate curve ---
t = np.linspace(0, 2 * np.pi * fy, N)
x = 0.5 + 0.5 * np.sin(fx * t / fy + phase)
y = 0.5 + 0.5 * np.sin(t)
points = np.column_stack([x, y])