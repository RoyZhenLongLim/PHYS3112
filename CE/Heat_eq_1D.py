#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:35:35 2024

@author: z3407853
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

length = 0.1
total_time = 60

alpha = 0.0001
delta_x = 0.01

delta_t = 0.1

#delta_t = (delta_x ** 2)/(20 * alpha)
gamma = (alpha * delta_t) / (delta_x ** 2)
print("gamma: ", gamma)

num_points = int(length / delta_x)
num_time_steps = int(total_time / delta_t)
print("Number of spatial points: ", num_points)
print("Number of temporal points: ", num_time_steps)

#matrix to store the solution at each time step
T = np.zeros((num_time_steps, num_points))

#print(T)

#Initial condition
T0 = np.zeros(num_points)
print("Initial condition: ", T0)

# Source term - Spatial boundary condition
q = np.zeros(num_points)
#q[0]=2
q[int(num_points / 2)] = 0.2
#q[int(num_points/4)]=0.1
#q[num_points-1]=1
print("Source term: ", q)

#FDM matrix
on = -2.0 * gamma * np.ones(num_points)
off = +gamma * np.ones(num_points - 1)
A = np.diag(on) + np.diag(off, 1) + np.diag(off, -1)
#Neumann
A[0, 0] = -1.0 * gamma
A[num_points - 1, num_points - 1] = -1.0 * gamma
#print(A)

#Time stepping
T_next = T0
T[0, :] = T0
#print("u_next:", u_next)

plt.clf()

X = np.linspace(0, length, num_points)

for i in range(1, num_time_steps):
    T_next = np.matmul(A, np.transpose(T_next)) + T_next + q
    T[i, :] = T_next

    #print("Final solution: ", u_next)
    #print("Stored matrix: ", u)

    plt.plot(X, T[i, :])
    plt.title("Temperature distribution with time.")
    plt.xlabel('Distance (m)')
    plt.ylabel('Temperature (C)')
    plt.show()
    plt.pause(0.0005)
