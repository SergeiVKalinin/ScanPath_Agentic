# curve_type: perturbed_fermat_spiral
# description: fermat spiral with sinusoidal radius perturbation
import numpy as np
N = 10000
# --- parameters ---
num_turns = 48
perturbation_amplitude = 0.05
perturbation_frequency = 5

theta = np.linspace(0, num_turns * 2 * np.pi, N)
# fermat spiral base radius
r = np.sqrt(theta / (num_turns * 2 * np.pi))
# add sinusoidal perturbation
r = r * (1 + perturbation_amplitude * np.sin(perturbation_frequency * theta))

x = 0.5 + 0.5 * r * np.cos(theta)
y = 0.5 + 0.5 * r * np.sin(theta)

# normalize to [0,1]
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])