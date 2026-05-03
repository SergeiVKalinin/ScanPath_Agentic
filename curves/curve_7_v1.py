# curve_type: rose
# description: mathematical rose curve
import numpy as np
N = 1000
# --- parameters ---
n = 5  # number of petals (if n/d are coprime)
d = 2  # denominator
amplitude = 0.4  # size
# --- curve generation ---
t = np.linspace(0, 2 * np.pi * d, N)
r = amplitude * np.cos((n / d) * t)
x = 0.5 + r * np.cos(t)
y = 0.5 + r * np.sin(t)
points = np.column_stack([x, y])