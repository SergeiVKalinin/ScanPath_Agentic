# curve_type: triple_density_serpentine
# description: Ultra-dense serpentine with 300 lines and 2D sinusoidal perturbation
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
perturbation_amplitude_x = 0.012
perturbation_amplitude_y = 0.008
perturbation_frequency_x = 18
perturbation_frequency_y = 22
# --- curve generation ---
t = np.linspace(0, 1, N)
line_index = t * num_lines
y = line_index / num_lines
line_direction = (np.floor(line_index) % 2) * 2 - 1
position_in_line = line_index - np.floor(line_index)
x = np.where(line_direction > 0, position_in_line, 1 - position_in_line)
x = x + perturbation_amplitude_x * np.sin(perturbation_frequency_x * np.pi * y)
y = y + perturbation_amplitude_y * np.sin(perturbation_frequency_y * np.pi * x)
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])