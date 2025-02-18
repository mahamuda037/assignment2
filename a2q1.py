import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, ln, exp, cos, sin, pi, sqrt, Matrix
t = symbols('t')

# (a) Finding tangent line parametric equations
# (i) r(t) = (ln(t), exp(-t), t^3)
x1, y1, z1 = ln(2) + (t - 2) * (1/2), exp(-2) + (t - 2) * (-exp(-2)), 8 + (t - 2) * 12
print("(a) Tangent Line Parametric Equations:")
print("(i)")
print(f"x = {x1}, y = {y1}, z = {z1}")

# (ii) r(t) = (2cos(pi*t), 2sin(pi*t), 3t)
x2, y2, z2 = 1 + (t - 1/3) * (-pi * sqrt(3)), sqrt(3) + (t - 1/3) * pi, 1 + (t - 1/3) * 3
print("(ii)")
print(f"x = {x2}, y = {y2}, z = {z2}")

# (b) Vector parallel to intersection of planes
print("(b) Vector parallel to intersection of planes:")
n1 = Matrix([3, -6, -2])
n2 = Matrix([2, 1, -2])
direction_vector = n1.cross(n2)
print(direction_vector)

# (c) Velocity, Acceleration, and Theta(t)
print("(c) Velocity and Acceleration:")
r = Matrix([3*t, sin(pi*t), t**2])
velocity = r.diff(t)
acceleration = velocity.diff(t)
print(f"Velocity = {velocity[0]} i^ + {velocity[1]} j^ + {velocity[2]} k^")
print(f"Acceleration = {acceleration[0]} i^ + {acceleration[1]} j^ + {acceleration[2]} k^")

# Plot theta(t) vs t
theta_expr = velocity.norm()
t_vals = np.linspace(0, 2, 100)
theta_values = [theta_expr.subs(t, val).evalf() for val in t_vals]

plt.plot(t_vals, theta_values, label=r'$	heta(t)$')
plt.xlabel('t')
plt.ylabel(r'$	heta(t)$')
plt.title('Velocity Magnitude vs. Time')
plt.legend()
plt.grid()
plt.show()