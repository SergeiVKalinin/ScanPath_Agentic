# curve_type: circular
# description: Concentric circles with perpendicular sinusoidal wobble
import numpy as np
N = 12000
# --- parameters ---
num_circles = 8
wobble_amplitude = 0.08  # 8% perpendicular wobble
wobble_frequency = 40  # wobble cycles

t = np.linspace(0, 1, N)
# Main concentric circles (spiral inward)
circle_idx = np.floor(t * num_circles)
radius = 0.5 * (1 - circle_idx / num_circles)
theta = 2 * np.pi * (t * num_circles - circle_idx)
# Base circular path
x = 0.5 + radius * np.cos(theta)
y = 0.5 + radius * np.sin(theta)
# Add perpendicular wobble (tangent direction)
wobble = wobble_amplitude * np.sin(2 * np.pi * wobble_frequency * t)
x += wobble * (-np.sin(theta))
y += wobble * np.cos(theta)
# Normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])