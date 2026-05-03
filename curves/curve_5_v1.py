# curve_type: rose
# description: rose curve with petals
import numpy as np
N = 1000
# --- parameters ---
n = 5  # number of petals (if odd) or 2*n (if even)
d = 1  # denominator for n/d ratio
# --- generation ---
t = np.linspace(0, 2 * np.pi, N)
k = n / d
r = 0.4 * np.cos(k * t)
x = 0.5 + r * np.cos(t)
y = 0.5 + r * np.sin(t)
points = np.column_stack([x, y])