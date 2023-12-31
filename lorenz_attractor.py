import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk

# Defining the Lorenz attractor differential equations
def lorenz(t, y, sigma, rho, beta):
    dydt = [
        sigma * (y[1] - y[0]),
        y[0] * (rho - y[2]) - y[1],
        y[0] * y[1] - beta * y[2]
    ]
    return dydt

# Parameters for the Lorenz attractor
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Initial conditions
y0 = [1.0, 0.0, 20.0]

# Time integration
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 100000)

# Solving the differential equations using solve_ivp
sol = solve_ivp(lorenz, t_span, y0, args=(sigma, rho, beta), t_eval=t_eval)

# Creating the figure and axes separately
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

# Visualizing the Lorenz attractor in 3D
ax.plot(sol.y[0], sol.y[1], sol.y[2], label='Lorenz Attractor', color='b', linewidth=0.2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Setting the title of the figure
fig.suptitle('Lorenz Attractor in 3D')

ax.legend()

# Attempting to set the title of the window for Windows systems
root = tk.Tk()
root.title('Lorenz Attractor in 3D')

# Hiding the extra window generated by matplotlib
manager = plt.get_current_fig_manager()
manager.window.after(100, root.withdraw)
manager.set_window_title('Lorenz Atractor')
# Displaying the figure
plt.show()
