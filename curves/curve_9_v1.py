# curve_type: lissajous
# description: Lissajous curve with frequency ratio 101:100, phase pi/2
import numpy as np
N = 30000
# --- parameters ---
fx = 101  # x frequency
fy = 100  # y frequency
phase = np.pi / 2  # phase offset in radians
# --- generate curve ---
t = np.linspace(0, 2 * np.pi * fy, N)
x = 0.5 + 0.5 * np.sin(fx * t / fy + phase)
y = 0.5 + 0.5 * np.sin(t)
points = np.column_stack([x, y])