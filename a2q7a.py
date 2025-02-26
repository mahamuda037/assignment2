import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define variables
x, y = sp.symbols('x y')

# Temperature function T(x, y)
T = 10 - 8*x**2 - 2*y**2

# Double integral for average temperature
area = (1 - 0) * (2 - 0)
T_avg = (1 / area) * sp.integrate(sp.integrate(T, (y, 0, 2)), (x, 0, 1))

print(f"The average temperature is: {T_avg} degrees Celsius")

# Visualization
x_vals = np.linspace(0, 1, 100)
y_vals = np.linspace(0, 2, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = 10 - 8*X**2 - 2*Y**2

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

ax.set_xlabel('x (meters)')
ax.set_ylabel('y (meters)')
ax.set_zlabel('Temperature (°C)')
plt.title('Temperature Distribution on the Plate')
plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
plt.show()
