from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg

import field_generator
import resolution
import dimensions
import vector_field
import plot_config as config
import vf_scale
import physics_calc

#--- MAIN ---#

MIN_TESLA = 0.1 #TODO: Abstract. Probably abstracted with plotting stuff.
MAX_TESLA = 0.75 #TODO: Abstract. Probably abstracted with plotting stuff.
TESLA_SCALE = 1 * (10**4) #TODO:Abstract. Probably abstracted with plotting stuff.

B_res = resolution.Resolution('base', 'base')
B_dim = dimensions.Dimensions(0, 5, 0, 5, 0, 2)
B_scale = vf_scale.VF_Scale(MIN_TESLA, MAX_TESLA, TESLA_SCALE)

J_res = resolution.Resolution('base', 'centi')
J_dim = dimensions.Dimensions(0, 4, 0, 2, 2, 2) #TODO: The last argument doesn't do anything, should this mean that all of the arguments should be made optional and the user of this function is forced to look up the required argument list?
J_scale = vf_scale.VF_Scale(0.1, 0.1, 1)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(elev=18, azim=30)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim([B_dim.startWidth, B_dim.endWidth])
ax.set_ylim([B_dim.startHeight, B_dim.endHeight])
ax.set_zlim([B_dim.startLength, B_dim.endLength])

J_config = config.PlotConfig(J_res, J_dim, J_scale)
J_field = field_generator.CosCurrent(J_config)

x,y,z,u,v,w = J_field.unpack()

ax.quiver(x, y, z, u, v, w, normalize = False, color = 'r')
	
B_config = config.PlotConfig(B_res, B_dim, B_scale) 
B_field = physics_calc.Biot_Savart(B_config, J_field).scale(B_scale) #TODO: Think on this scaling, should it be applied in the biot savart or somewhere in there? Since it is already applied in the J-field's generation.

x,y,z,u,v,w = B_field.unpack()
print(u)
ax.quiver(x, y, z, u, v, w, normalize = False)
	
plt.show()


