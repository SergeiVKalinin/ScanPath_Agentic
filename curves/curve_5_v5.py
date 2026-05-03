# curve_type: variable_density_serpentine
# description: Serpentine with increasing density toward top, weak perturbation
import numpy as np
N = 1000
# --- parameters ---
num_lines = 150
perturbation_amplitude = 0.008
perturbation_frequency = 15
density_exponent = 1.5
# --- curve generation ---
t = np.linspace(0, 1, N)
cumulative_spacing = np.power(t, density_exponent)
cumulative_spacing = cumulative_spacing / cumulative_spacing[-1]
line_index = cumulative_spacing * num_lines
y = line_index / num_lines
line_direction = (np.floor(line_index) % 2) * 2 - 1
position_in_line = line_index - np.floor(line_index)
x = np.where(line_direction > 0, position_in_line, 1 - position_in_line)
x = x + perturbation_amplitude * np.sin(perturbation_frequency * np.pi * y)
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])