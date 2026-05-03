# curve_type: lissajous
# description: Lissajous curve with frequency ratio 99:98, phase 0
import numpy as np
N = 30000
# --- parameters ---
fx = 99  # x frequency
fy = 98  # y frequency
phase = 0  # phase offset in radians
# --- generate curve ---
t = np.linspace(0, 2 * np.pi * fy, N)
x = 0.5 + 0.5 * np.sin(fx * t / fy + phase)
y = 0.5 + 0.5 * np.sin(t)
points = np.column_stack([x, y])