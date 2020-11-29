import numpy as np
import matplotlib.pyplot as plt

# Mass, Spring constant, Velocity, displacement

m = 1
k = 1
x = 0
v = 1


# simulation time and step time
t_max = 100
dt = 0.1
t_array = np.arange(0, t_max, dt)
x_prev = - dt * v
# initialize the trajectory list

x_list = []
v_list = []

# Verlet integration

for t in t_array:
    # append current state in trajectory
    x_list.append(x)
    v_list.append(v)
    # change the state of the trajectory
    a = -k * x / m
    x_now = x
    x = 2 * x - x_prev + (dt**2) * a
    print(x)
    v = (1 / dt) * (x - x_now)
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
