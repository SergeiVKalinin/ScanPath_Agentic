# curve_type: square_spiral
# description: Square spiral with medium circular wobble
import numpy as np
N = 16000
# --- parameters ---
num_squares = 10
wobble_amplitude = 0.025  # 2.5% circular wobble
wobble_frequency = 45  # wobble cycles

t = np.linspace(0, 1, N)
# Main square spiral
square_idx = np.floor(t * num_squares)
size = 0.5 * (1 - square_idx / num_squares)
# Position along square perimeter
t_square = (t * num_squares - square_idx) * 4
side = np.floor(t_square)
t_side = t_square - side
# Generate square coordinates
x = np.where(side == 0, 0.5 - size + 2 * size * t_side,
    np.where(side == 1, 0.5 + size,
    np.where(side == 2, 0.5 + size - 2 * size * t_side, 0.5 - size)))
y = np.where(side == 0, 0.5 - size,
    np.where(side == 1, 0.5 - size + 2 * size * t_side,
    np.where(side == 2, 0.5 + size, 0.5 + size - 2 * size * t_side)))
# Add circular wobble
wobble_theta = 2 * np.pi * wobble_frequency * t
x += wobble_amplitude * np.cos(wobble_theta)
y += wobble_amplitude * np.sin(wobble_theta)
# Normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])