import numpy as np
import vector_field as VectorField

def CosCurrent(config):

	START = config.dim.startWidth
	END =  config.dim.endWidth
	RADIANS = 2 * np.pi

	x = np.arange(START, END, config.res.step)
	y = (((config.dim.startHeight - config.dim.endHeight) / 2) 
	     * np.sin(x * RADIANS))
	z = [config.dim.startLength for k in range(len(x))] 
	
	u = [config.dim.width/0.05 for k in range(len(x))]
	v = [config.dim.height/0.05 for k in range(len(x))] 
	w = [config.dim.startLength for k in range(len(x))]
	
	return VectorField.VectorField(x, y, z, u, v, w)
