# curve_type: lissajous
# description: lissajous figure with 3:2 frequency ratio
import numpy as np
N = 1000
# --- parameters ---
freq_x = 3  # frequency in x direction
freq_y = 2  # frequency in y direction
phase = np.pi / 2  # phase offset
amplitude = 0.4  # size of pattern
# --- curve generation ---
t = np.linspace(0, 2 * np.pi, N)
x = 0.5 + amplitude * np.sin(freq_x * t)
y = 0.5 + amplitude * np.sin(freq_y * t + phase)
points = np.column_stack([x, y])