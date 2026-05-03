# curve_type: hilbert
# description: hilbert space-filling curve
import numpy as np
N = 1000
# --- parameters ---
order = 4  # hilbert curve order
# --- generation ---
def hilbert_curve(order):
    if order == 0:
        return np.array([[0, 0]])
    prev = hilbert_curve(order - 1)
    n = len(prev)
    # rotate and arrange in 4 quadrants
    quad1 = np.column_stack([prev[:, 1], prev[:, 0]])
    quad2 = prev + np.array([0, n])
    quad3 = prev + np.array([n, n])
    quad4 = np.column_stack([n - 1 - prev[:, 1], 2 * n - 1 - prev[:, 0]])
    return np.vstack([quad1, quad2, quad3, quad4])
coords = hilbert_curve(order)
coords = coords.astype(float)
coords = coords / coords.max()
indices = np.linspace(0, len(coords) - 1, N).astype(int)
x = coords[indices, 0]
y = coords[indices, 1]
points = np.column_stack([x, y])