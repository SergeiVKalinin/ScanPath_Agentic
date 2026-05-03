# curve_type: large_prime_exploration
# description: high frequency primes 41-61 with reduced amplitudes
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
t = np.linspace(0, 1, N)
# base grid
x = np.repeat(np.linspace(0, 1, num_lines), N // num_lines + 1)[:N]
y = np.tile(np.linspace(0, 1, num_lines), N // num_lines + 1)[:N]
# large prime frequencies
freq_x1 = 41
freq_x2 = 43
freq_y1 = 47
freq_y2 = 53
freq_coupled = 41
# reduced amplitudes for high frequencies
x_amp_1 = 0.006
x_amp_2 = 0.0025
y_amp_1 = 0.006
y_amp_2 = 0.0025
coupled_amp = 0.003
# apply perturbations
x = x + x_amp_1 * np.sin(2 * np.pi * freq_x1 * y)
x = x + x_amp_2 * np.sin(2 * np.pi * freq_x2 * y)
y = y + y_amp_1 * np.sin(2 * np.pi * freq_y1 * x)
y = y + y_amp_2 * np.sin(2 * np.pi * freq_y2 * x)
# coupled perturbation
coupled_perturbation = coupled_amp * np.sin(2 * np.pi * freq_coupled * (x + y))
x = x + coupled_perturbation
y = y + coupled_perturbation
# normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])