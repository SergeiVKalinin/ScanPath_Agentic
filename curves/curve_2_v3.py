# curve_type: serpentine_with_extended_spectrum
# description: Extended frequency spectrum with tertiary perturbation layers on both axes
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
t = np.linspace(0, 1, N)
# Base serpentine pattern
line_idx = np.floor(t * num_lines)
x = (t * num_lines) % 1
y = line_idx / num_lines
# Reverse every other line
reverse_mask = (line_idx % 2 == 1)
x[reverse_mask] = 1 - x[reverse_mask]
# Primary perturbations
perturbation_amplitude_x = 0.012
perturbation_frequency_x = 18
perturbation_amplitude_y = 0.008
perturbation_frequency_y = 22
# Secondary perturbations
secondary_amplitude_x = 0.004
secondary_frequency_x = 37
secondary_amplitude_y = 0.003
secondary_frequency_y = 41
# Tertiary perturbations
tertiary_amplitude_x = 0.002
tertiary_frequency_x = 43
tertiary_amplitude_y = 0.002
tertiary_frequency_y = 47
# Apply all perturbations
x = x + perturbation_amplitude_x * np.sin(2 * np.pi * perturbation_frequency_x * t)
x = x + secondary_amplitude_x * np.sin(2 * np.pi * secondary_frequency_x * t)
x = x + tertiary_amplitude_x * np.sin(2 * np.pi * tertiary_frequency_x * t)
y = y + perturbation_amplitude_y * np.sin(2 * np.pi * perturbation_frequency_y * t)
y = y + secondary_amplitude_y * np.sin(2 * np.pi * secondary_frequency_y * t)
y = y + tertiary_amplitude_y * np.sin(2 * np.pi * tertiary_frequency_y * t)
# Normalize to [0, 1]
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])