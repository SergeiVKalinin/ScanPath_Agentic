# curve_type: lissajous
# description: Lissajous with dual-frequency spiral wobble
import numpy as np
N = 25000
# --- parameters ---
freq_x = 5  # x frequency
freq_y = 6  # y frequency
phase = 0  # phase offset
wobble_amplitude = 0.04  # 4% wobble
wobble_freq_fast = 60  # fast wobble frequency
wobble_freq_slow = 10  # slow modulation

t = np.linspace(0, 1, N)
# Main Lissajous curve
x = 0.5 + 0.45 * np.sin(2 * np.pi * freq_x * t)
y = 0.5 + 0.45 * np.sin(2 * np.pi * freq_y * t + phase)
# Add dual-frequency spiral wobble
theta = 2 * np.pi * wobble_freq_fast * t
r_mod = wobble_amplitude * (1 + 0.5 * np.sin(2 * np.pi * wobble_freq_slow * t))
x += r_mod * np.cos(theta)
y += r_mod * np.sin(theta)
# Normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])