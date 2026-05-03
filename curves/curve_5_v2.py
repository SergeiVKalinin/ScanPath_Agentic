# curve_type: spiral
# description: Archimedean spiral with 70 turns and density perturbation
import numpy as np
N = 10000
# --- parameters ---
num_turns = 70  # optimized between Fermat's 50 and higher values
perturbation_amplitude = 0.02  # slight density variation
perturbation_frequency = 10  # oscillation count
# Generate Archimedean spiral with linear spacing
theta = np.linspace(0, num_turns * 2 * np.pi, N)
r = theta / (num_turns * 2 * np.pi)  # linear radial growth
# Add perturbation for density variation
r = r * (1.0 + perturbation_amplitude * np.sin(perturbation_frequency * theta))
# Scale to unit square centered at (0.5, 0.5)
r = r * 0.5  # max radius = 0.5
x = 0.5 + r * np.cos(theta)
y = 0.5 + r * np.sin(theta)
# Ensure bounds [0, 1]
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])