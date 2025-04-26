import matplotlib.pyplot as plt
import numpy as np

# Data from calculations
angles = [0, 15, 30, 45]  # Slope angles in degrees
hiking_energy = [14.64, 33.95, 50.73, 62.15]  # Metabolic energy in kJ
running_energy = [29.29, 42.43, 50.71, 51.76]  # Metabolic energy in kJ
biking_energy = [4.39, 91.64, 176.13, 248.4]  # Metabolic energy in kJ
biking_hiking_ratio = [b / h for b, h in zip(biking_energy, hiking_energy)]  # Biking vs. Hiking ratio
biking_running_ratio = [b / r for b, r in zip(biking_energy, running_energy)]  # Biking vs. Running ratio

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Subplot 1: Energy for Hiking, Running, and Biking
ax1.plot(angles, hiking_energy, marker='d', linestyle='-', color='green', label='Hiking', linewidth=2)
ax1.plot(angles, running_energy, marker='o', linestyle='-', color='blue', label='Running', linewidth=2)
ax1.plot(angles, biking_energy, marker='s', linestyle='-', color='red', label='Biking', linewidth=2)
ax1.set_ylabel('Metabolic Energy (kJ)', fontsize=12)
ax1.set_title('Energy Required for Hiking, Running, and Biking over 100 m', fontsize=14, pad=15)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(fontsize=10)

# Subplot 2: Biking vs. Hiking and Biking vs. Running Ratios
ax2.plot(angles, biking_hiking_ratio, marker='^', linestyle='-', color='purple', label='Biking/Hiking Ratio', linewidth=2)
ax2.plot(angles, biking_running_ratio, marker='v', linestyle='-', color='orange', label='Biking/Running Ratio', linewidth=2)
ax2.set_xlabel('Slope Angle (°)', fontsize=12)
ax2.set_ylabel('Energy Ratio', fontsize=12)
ax2.set_title('Biking vs. Hiking and Running Energy Ratios by Slope Angle', fontsize=14, pad=15)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(fontsize=10)

# Set x-axis ticks to 15-degree intervals
ax1.set_xticks(np.arange(0, 46, 15))  # Ticks at 0, 15, 30, 45
ax2.set_xticks(np.arange(0, 46, 15))  # Shared x-axis

# Adjust layout to prevent clipping
plt.tight_layout()

# Save the plot as an image
plt.savefig('energy_trends_with_hiking.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
