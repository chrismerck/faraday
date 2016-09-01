import numpy as np
import vector_field as VectorField

def sin(config):

	START = config.dim.start_width
	END =  config.dim.end_width
	RADIANS = 2 * np.pi

	x = np.arange(START, END, config.res.step)
	y = (((config.dim.start_height - config.dim.end_height) / 2) 
	     * np.sin(x * RADIANS))
	z = [config.dim.start_length for k in range(len(x))] 
	
	u = [config.dim.width/0.05 for k in range(len(x))]
	v = [config.dim.height/0.05 for k in range(len(x))] 
	w = [config.dim.start_length for k in range(len(x))]
	
	return VectorField.VectorField(x, y, z, u, v, w)
