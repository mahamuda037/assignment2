import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import tplquad, dblquad

# Define variables
x, y, z = sp.symbols('x y z')

# First integral
f1 = lambda z, y, x: x * np.exp(-y) * np.cos(z)
sol1 = tplquad(f1, 0, 1, lambda x: 0, lambda x: 1 - x**2, lambda x, y: 3, lambda x, y: 4 - x**2 - y**2)[0]
print("Value of the first integral (numerical):", sol1)

# Second integral
f2 = lambda y, x: (x * y) / np.sqrt(x**2 + y**2 + 1)
sol2 = dblquad(f2, 0, 1, lambda x: 0, lambda x: 1)[0]
print("Value of the second integral (numerical):", sol2)

# Visualization for the first integral
X = np.linspace(0, 1, 100)
Y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(X, Y)
Z1 = np.array([[tplquad(f1, 3, 4 - x**2 - y**2, lambda z: y, lambda z: y, lambda z, y: x, lambda z, y: x)[0] for y in np.linspace(0, 1 - x**2, 50)] for x in np.linspace(0, 1, 50)])

fig1 = plt.figure(figsize=(10, 7))
ax1 = fig1.add_subplot(111, projection='3d')
surf1 = ax1.plot_surface(X[:50, :50], Y[:50, :50], Z1, cmap='plasma')
plt.title('Surface plot of first integral')
fig1.colorbar(surf1)

# Visualization for the second integral
Z2 = (X * Y) / np.sqrt(X**2 + Y**2 + 1)

fig2 = plt.figure(figsize=(10, 7))
ax2 = fig2.add_subplot(111, projection='3d')
surf2 = ax2.plot_surface(X, Y, Z2, cmap='viridis')
plt.title('Surface plot of (xy / sqrt(x^2 + y^2 + 1))')
fig2.colorbar(surf2)

# Show both plots
plt.show()