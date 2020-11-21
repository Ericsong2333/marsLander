import numpy as np
import matplotlib.pyplot as plt

# simulation time and step time
t_max = 1000
dt = 0.1
t_array = np.arange(0, t_max, dt)

# Mass, Spring constant, Velocity, displacement

m = 1
k = 1
x0 = 0
v0 = 1
x1 = x0 + dt * v0
v1 = (x1 - x0) / dt

# initialize the trajectory list

x_list = []
v_list = []

# Verlet integration

for t in t_array:
    # append current state in trajectory
    x_list.append(x0)
    v_list.append(v0)
    # store values of x1, v1
    xStore = x1
    vStore = v1

    # calculate new position and velocity
    a = -k * x1 / m
    x1 = 2 * x1 - x0 + dt**2 * a
    v1 = (x1 - xStore)/dt

    # iterate values
    x0 = xStore
    v0 = vStore

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)

# plot the position-time graph
plt.figure(2)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()
