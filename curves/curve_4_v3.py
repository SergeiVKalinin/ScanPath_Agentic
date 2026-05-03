# curve_type: serpentine_with_higher_density
# description: Increased line density to 350 with proportionally reduced perturbation amplitudes
import numpy as np
N = 1000
# --- parameters ---
num_lines = 350
t = np.linspace(0, 1, N)
# Base serpentine pattern
line_idx = np.floor(t * num_lines)
x = (t * num_lines) % 1
y = line_idx / num_lines
# Reverse every other line
reverse_mask = (line_idx % 2 == 1)
x[reverse_mask] = 1 - x[reverse_mask]
# Reduced perturbations for higher density
perturbation_amplitude_x = 0.0102
perturbation_frequency_x = 18
perturbation_amplitude_y = 0.0068
perturbation_frequency_y = 22
# Apply perturbations
x = x + perturbation_amplitude_x * np.sin(2 * np.pi * perturbation_frequency_x * t)
y = y + perturbation_amplitude_y * np.sin(2 * np.pi * perturbation_frequency_y * t)
# Normalize to [0, 1]
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])