from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(elev=18, azim=30)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim([0,11])
ax.set_ylim([0,11])
ax.set_zlim([0,11])

x = [6 for x in range(0,11)] # Creates a list of 11 numbers '6' -|
y = [6 for x in range(0,11)] # Creates a list of 11 numbers '6'  |-- These lists are the x,y,z coordinate pairs.
z = [x for x in range(0,11)] # Creates a list of 1,2,3,4...,11. -|

u = [0 for x in range(0,11)]
v = [0 for x in range(0,11)]
w = [1 for x in range(0,11)]

ax.quiver(x,y,z,u,v,w,length=0.5)

plt.show()