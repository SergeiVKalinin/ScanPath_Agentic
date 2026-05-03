# curve_type: zigzag
# description: zigzag pattern moving horizontally
import numpy as np
N = 1000
# --- parameters ---
cycles = 10  # number of zigzags
amplitude = 0.4  # vertical amplitude
# --- curve generation ---
t = np.linspace(0, 1, N)
x = t
y = 0.5 + amplitude * np.abs(((t * cycles * 2) % 2) - 1) * np.sign(np.sin(np.pi * t * cycles))
points = np.column_stack([x, y])