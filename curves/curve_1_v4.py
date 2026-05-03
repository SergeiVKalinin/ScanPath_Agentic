# curve_type: serpentine
# description: Ultra-dense serpentine with 200 lines and subtle sinusoidal perturbation for smoothness
import numpy as np
N = 10000
# --- parameters ---
num_lines = 200
points_per_line = N // num_lines
perturbation_amplitude = 0.01
perturbation_frequency = 20

x = []
y = []
for i in range(num_lines):
    y_val = i / (num_lines - 1)
    if i % 2 == 0:
        x_line = np.linspace(0, 1, points_per_line)
    else:
        x_line = np.linspace(1, 0, points_per_line)
    
    y_line = np.full(points_per_line, y_val)
    x_perturbed = x_line + perturbation_amplitude * np.sin(perturbation_frequency * np.pi * y_line)
    x_perturbed = np.clip(x_perturbed, 0, 1)
    
    x.extend(x_perturbed)
    y.extend(y_line)

x = np.array(x[:N])
y = np.array(y[:N])
points = np.column_stack([x, y])