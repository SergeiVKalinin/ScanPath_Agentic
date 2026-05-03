# curve_type: hilbert
# description: hilbert space-filling curve
import numpy as np
N = 1000
# --- parameters ---
order = 4  # recursion depth
# --- curve generation ---
def hilbert_curve(order):
    if order == 0:
        return np.array([[0, 0]])
    
    # get previous order curve
    prev = hilbert_curve(order - 1)
    n = len(prev)
    
    # create four quadrants
    # bottom-left: rotated -90
    bl = np.column_stack([-prev[:, 1], prev[:, 0]])
    # bottom-right: original + offset
    br = prev + np.array([0, 1])
    # top-right: original + offset
    tr = prev + np.array([1, 1])
    # top-left: rotated 90 + offset
    tl = np.column_stack([prev[:, 1], -prev[:, 0]]) + np.array([1, 0])
    
    # connect quadrants
    curve = np.vstack([bl, br, tr, tl])
    return curve

coords = hilbert_curve(order)
# normalize to [0, 1]
coords = coords - coords.min()
coords = coords / coords.max()
# resample to N points
t_original = np.linspace(0, 1, len(coords))
t_new = np.linspace(0, 1, N)
x = np.interp(t_new, t_original, coords[:, 0])
y = np.interp(t_new, t_original, coords[:, 1])
points = np.column_stack([x, y])