# curve_type: enhanced_cross_coupling
# description: dual coupled terms exploring constructive interference
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
t = np.linspace(0, 1, N)
# base grid
x = np.repeat(np.linspace(0, 1, num_lines), N // num_lines + 1)[:N]
y = np.tile(np.linspace(0, 1, num_lines), N // num_lines + 1)[:N]
# five prime frequencies
freq_x1 = 13
freq_x2 = 17
freq_y1 = 23
freq_y2 = 29
freq_y3 = 31
freq_coupled_1 = 13
freq_coupled_2 = 19
# amplitudes
x_amp_1 = 0.008
x_amp_2 = 0.003
y_amp_1 = 0.007
y_amp_2 = 0.003
y_amp_3 = 0.003
coupled_amp_1 = 0.004
coupled_amp_2 = 0.003
# apply perturbations
x = x + x_amp_1 * np.sin(2 * np.pi * freq_x1 * y)
x = x + x_amp_2 * np.sin(2 * np.pi * freq_x2 * y)
y = y + y_amp_1 * np.sin(2 * np.pi * freq_y1 * x)
y = y + y_amp_2 * np.sin(2 * np.pi * freq_y2 * x)
y = y + y_amp_3 * np.sin(2 * np.pi * freq_y3 * x)
# dual coupled perturbations
coupled_1 = coupled_amp_1 * np.sin(2 * np.pi * freq_coupled_1 * (x + y))
coupled_2 = coupled_amp_2 * np.sin(2 * np.pi * freq_coupled_2 * (x - y))
x = x + coupled_1 + coupled_2
y = y + coupled_1 - coupled_2
# normalize
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)
points = np.column_stack([x, y])