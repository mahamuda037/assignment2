import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

R, H, r, theta, z = sp.symbols('R H r theta z')

# The density function in cylindrical coordinates is rho = r^2
rho = r**2

# Set up the integral to calculate mass symbolically
mass_integral = sp.integrate(rho * r, (z, -H/2, H/2), (r, 0, R), (theta, 0, 2*sp.pi))

print(f"Symbolic mass of the cylinder: {mass_integral}")

# Visualization
# Now calculate it for R = 2 and H = 4
R_value = 2
H_value = 4
mass_numeric = mass_integral.subs({R: R_value, H: H_value})

# Create a grid for the cylinder
theta_vals = np.linspace(0, 2 * np.pi, 100)
r_vals = np.linspace(0, R_value, 100)
z_vals = np.linspace(-H_value/2, H_value/2, 100)

# Create a meshgrid for the 3D plot
theta_vals, r_vals = np.meshgrid(theta_vals, r_vals)
x_vals = r_vals * np.cos(theta_vals)
y_vals = r_vals * np.sin(theta_vals)
z_vals = np.tile(z_vals, (len(r_vals), 1))

# Calculate the density at each point (x, y) in cylindrical coordinates
rho_vals = x_vals**2 + y_vals**2

# Plot the cylinder with the density coloring
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x_vals, y_vals, z_vals, facecolors=plt.cm.viridis(rho_vals / np.max(rho_vals)),
                       rstride=5, cstride=5, alpha=0.8)

# Add color bar
cbar = fig.colorbar(surf)
cbar.set_label('Density (rho(x, y))')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Cylinder with Density Distribution (R={R_value}, H={H_value})')

plt.show()