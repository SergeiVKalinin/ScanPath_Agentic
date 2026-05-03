# curve_type: six_prime_maximum
# description: extends top performer to 6 prime frequencies with tertiary perturbations
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
t = np.linspace(0, 1, N)
# base grid
x = np.repeat(np.linspace(0, 1, num_lines), N // num_lines + 1)[:N]
y = np.tile(np.linspace(0, 1, num_lines), N // num_lines + 1)[:N]
# six prime frequencies
freq_x1 = 13
freq_x2 = 17
freq_x3 = 37
freq_y1 = 23
freq_y2 = 29
freq_y3 = 43
freq_coupled = 13
# primary perturbations
x_amp_1 = 0.008
x_amp_2 = 0.003
x_amp_3 = 0.002
y_amp_1 = 0.007
y_amp_2 = 0.003
y_amp_3 = 0.002
coupled_amp = 0.004
# apply perturbations
x = x + x_amp_1 * np.sin(2 * np.pi * freq_x1 * y)
x = x + x_amp_2 * np.sin(2 * np.pi * freq_x2 * y)
x = x + x_amp_3 * np.sin(2 * np.pi * freq_x3 * y)
y = y + y_amp_1 * np.sin(2 * np.pi * freq_y1 * x)
y = y + y_amp_2 * np.sin(2 * np.pi * freq_y2 * x)
y = y + y_amp_3 * np.sin(2 * np.pi * freq_y3 * x)
# coupled perturbation
coupled_perturbation = coupled_amp * np.sin(2 * np.pi * freq_coupled * (x + y))
x = x + coupled_perturbation
y = y + coupled_perturbation
# normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])