# curve_type: lissajous
# description: Lissajous pattern with circular wobble
import numpy as np
N = 20000
# --- parameters ---
freq_x = 3  # x frequency
freq_y = 4  # y frequency
phase = np.pi / 2  # phase offset
wobble_amplitude = 0.03  # 3% circular wobble
wobble_frequency = 50  # wobble cycles

t = np.linspace(0, 1, N)
# Main Lissajous curve
x = 0.5 + 0.4 * np.sin(2 * np.pi * freq_x * t)
y = 0.5 + 0.4 * np.sin(2 * np.pi * freq_y * t + phase)
# Add circular wobble
wobble_theta = 2 * np.pi * wobble_frequency * t
x += wobble_amplitude * np.cos(wobble_theta)
y += wobble_amplitude * np.sin(wobble_theta)
# Normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])