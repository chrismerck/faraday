""" Functions defined in this file allow for the generation of vector
fields through common mathematical functions.

Todo:
	- Implement a function that generates a vector field in the shape of
	  a circle.
	- Implement a function that generates a vector field through a
	  polynomial function.
	- Implement a function that generates a vector field with a path of a
	  curve. This can be done with Bézier Curves or some other form of a
	  parametric equation.

"""

import numpy as np
import vector_field as VectorField

def sin(config):
	""" Generates the (x,y,z) coordinates and the (u,v,w) components that
	are then used to construct a vector field.
	
	Args:
		config (PlotConfig): Holds the configuration for
			the bounds of the returned vector field
			and the resolution of the returned vector 
			field.
	
	Returns:
		VectorField: A vector field that describes the path of
			a sin wave. 
	"""

	START = config.bound.min_x
	END =  config.bound.max_x
	RADIANS = 2 * np.pi

	x = np.arange(START, END, config.res.step)
	y = (((config.bound.max_y-config.bound.min_y) / 2)
	     * np.sin(x * RADIANS))
	z = [config.bound.min_z for k in x] 
	
	u = [config.bound.width/0.05 for k in x]
	v = [config.bound.height/0.05 for k in x] 
	w = [config.bound.min_z for k in x]
	
	return VectorField.VectorField(x, y, z, u, v, w)
