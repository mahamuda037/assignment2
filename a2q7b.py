import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

t = sp.symbols('t')
x = sp.cos(t)
y = sp.sin(t)
z = t

f = x * y + z**3

dx_dt = sp.diff(x, t)
dy_dt = sp.diff(y, t)
dz_dt = sp.diff(z, t)

# Arc length element ds = sqrt((dx/dt)^2 + (dy/dt)^2 + (dz/dt)^2) dt
ds = sp.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2)

# Line integral: ∫(f(x, y, z) * ds) from t=0 to t=pi
integrand = f * ds
result = sp.integrate(integrand, (t, 0, sp.pi))

# Convert symbolic expressions to numpy functions for plotting
t_vals = np.linspace(0, np.pi, 100)
x_vals = np.cos(t_vals)
y_vals = np.sin(t_vals)
z_vals = t_vals

# Calculate the midpoint of the curve (at t = pi/2)
t_mid = np.pi / 2
x_mid = np.cos(t_mid)
y_mid = np.sin(t_mid)
z_mid = t_mid

# Calculate the direction from the start to the end
arrow_dx = x_vals[2] - x_vals[0]
arrow_dy = y_vals[2] - y_vals[0]
arrow_dz = z_vals[2] - z_vals[0]

# Plot the helix
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_vals, y_vals, z_vals, label='Helix: x=cos(t), y=sin(t), z=t', color='b')

# Highlight start and end points
ax.scatter([1, -1], [0, 0], [0, np.pi], color='red', s=50, label='Start (1,0,0) and End (-1,0,pi)')

# Add a single arrow at the midpoint indicating the direction from start to end
ax.quiver(x_mid, y_mid, z_mid, 
          arrow_dx, arrow_dy, arrow_dz, 
          color='black', length=0.6, normalize=True)

# Labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('Helix Curve for Line Integral with Direction Arrow')

plt.legend()
plt.show()

# Display the result of the line integral
print(f"The value of the line integral is: {result}")