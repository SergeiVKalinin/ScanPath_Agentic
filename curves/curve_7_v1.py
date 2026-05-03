# curve_type: lissajous
# description: Lissajous curve with frequency ratio 100:99, phase 0
import numpy as np
N = 30000
# --- parameters ---
fx = 100  # x frequency
fy = 99  # y frequency
phase = 0  # phase offset in radians
# --- generate curve ---
t = np.linspace(0, 2 * np.pi * fy, N)
x = 0.5 + 0.5 * np.sin(fx * t / fy + phase)
y = 0.5 + 0.5 * np.sin(t)
points = np.column_stack([x, y])