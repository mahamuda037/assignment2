import numpy as np
import matplotlib.pyplot as plt

# Define the force field F(x, y) = [e^y, x*e^y]
def F(x, y):
    Fx = np.exp(y)  # e^y
    Fy = x * np.exp(y)  # x * e^y
    return Fx, Fy

# Verify if the field is conservative
def is_conservative():
    # Partial derivatives
    dFydx = lambda x, y: np.exp(y)  # ∂(x*e^y)/∂x
    dFxdy = lambda x, y: np.exp(y)  # ∂(e^y)/∂y
    
    # Check if curl = 0 (∂Fy/∂x - ∂Fx/∂y = 0)
    return dFydx(0, 0) - dFxdy(0, 0) == 0

print("Is the field conservative?", is_conservative())

# Find the potential function φ(x, y)
def potential(x, y):
    return x * np.exp(y)  # φ(x, y) = xe^y

# Calculate work using potential function φ
def work_done(start, end):
    return potential(*end) - potential(*start)

# Define the semicircular path from (1,0) to (-1,0)
theta = np.linspace(0, np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

# Add arrows for direction along the curve
arrow_idx = np.linspace(0, len(x)-2, 8).astype(int)  # Ensure i+1 stays in bounds

# Plot the force field
X, Y = np.meshgrid(np.linspace(-1.5, 1.5, 20), np.linspace(-1, 1, 20))
Fx, Fy = F(X, Y)
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, Fx, Fy, color='blue', alpha=0.5, label='Force Field F(x, y)')

# Plot the semicircular path
plt.plot(x, y, 'r--', label='Path C (semicircle)')

# Add arrows to indicate direction of the path
for i in arrow_idx:
    plt.annotate('', xy=(x[i+1], y[i+1]), xytext=(x[i], y[i]),
                 arrowprops=dict(arrowstyle='->', color='black'))

# Mark start and end points
plt.scatter([1, -1], [0, 0], color='black')
plt.text(1, 0, '(1,0)', fontsize=12, verticalalignment='bottom')
plt.text(-1, 0, '(-1,0)', fontsize=12, verticalalignment='bottom')

plt.title('Force Field and Semicircular Path with Direction')
plt.legend()
plt.grid(True)
plt.show()

# Calculate and display work
start = (1, 0)
end = (-1, 0)
W = work_done(start, end)
print(f"Work done along path C: {W}")