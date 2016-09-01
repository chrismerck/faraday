from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg

import resolution as Resolution
import dimensions as Dimensions
import vf_scale as VF_Scale
import plot_config as PlotConfig
import field_generator
import physics_calc as calc

MIN_TESLA = 0.1
MAX_TESLA = 0.75 
TESLA_SCALE = 1 * (10**5)

B_res = Resolution.Resolution('base', 'base')
B_dim = Dimensions.Dimensions(-5, 5, -5, 5, -5, 5)
B_scale = VF_Scale.VF_Scale(MIN_TESLA, MAX_TESLA, TESLA_SCALE)

J_res = Resolution.Resolution('base', 'centi')
J_dim = Dimensions.Dimensions(0, 4, 0, 2, 0, 2)#Last argument does nothing.
J_scale = VF_Scale.VF_Scale(0.1, 0.1, 1)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(elev=18, azim=30)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim([B_dim.start_width, B_dim.end_width])
ax.set_ylim([B_dim.start_height, B_dim.end_height])
ax.set_zlim([B_dim.start_length, B_dim.end_length])

J_config = PlotConfig.PlotConfig(J_res, J_dim)
J_field = field_generator.sin(J_config).scale(J_scale)
x, y, z, u, v, w = J_field.unpack()
ax.quiver(x, y, z, u, v, w, normalize=False, color='r')

B_config = PlotConfig.PlotConfig(B_res, B_dim) 
B_field = calc.biot_savart(B_config, J_field).scale(B_scale)
x, y, z, u, v, w = B_field.unpack()
ax.quiver(x, y, z, u, v, w, normalize=False)

plt.show()
