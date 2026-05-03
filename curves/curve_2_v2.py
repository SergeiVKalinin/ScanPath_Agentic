# curve_type: serpentine_with_dual_coupled_perturbation
# description: Enhanced coupled system with second coupled term using x-y difference
import numpy as np
N = 1000
# --- parameters ---
num_lines = 300
x_primary_amp = 0.010
y_primary_amp = 0.006
x_secondary_amp = 0.008
y_secondary_amp = 0.005
x_tertiary_amp = 0.004
coupled_amp = 0.004
coupled_amp_2 = 0.003
x_primary_freq = 17
y_primary_freq = 23
x_secondary_freq = 29
y_secondary_freq = 31
x_tertiary_freq = 37
coupled_freq = 13
coupled_freq_2 = 19

points_list = []
for i in range(num_lines):
    y_base = i / (num_lines - 1)
    if i % 2 == 0:
        x_base = np.linspace(0, 1, N // num_lines)
    else:
        x_base = np.linspace(1, 0, N // num_lines)
    
    t = np.linspace(0, 1, len(x_base))
    
    x_pert = (x_primary_amp * np.sin(2 * np.pi * x_primary_freq * t) +
              x_secondary_amp * np.sin(2 * np.pi * x_secondary_freq * t) +
              x_tertiary_amp * np.sin(2 * np.pi * x_tertiary_freq * t))
    
    y_pert = (y_primary_amp * np.sin(2 * np.pi * y_primary_freq * t) +
              y_secondary_amp * np.sin(2 * np.pi * y_secondary_freq * t))
    
    coupled_pert = coupled_amp * np.sin(2 * np.pi * coupled_freq * (x_base + y_base))
    coupled_pert_2 = coupled_amp_2 * np.sin(2 * np.pi * coupled_freq_2 * (x_base - y_base))
    
    x = np.clip(x_base + x_pert + coupled_pert + coupled_pert_2, 0, 1)
    y = np.clip(np.full_like(x_base, y_base) + y_pert + coupled_pert + coupled_pert_2, 0, 1)
    
    points_list.append(np.column_stack([x, y]))

points = np.vstack(points_list)