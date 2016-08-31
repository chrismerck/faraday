import numpy as np
import resolution
import dimensions
import plot_config
import vector_field

def CosCurrent(config):
	'''
	Params:
		@resolution An object that stores all of the data in regards to the percision of the calculations. 
		@dimensions An object that specifies the dimenisons of the 3D space that will be used to plot the 
	'''
	START = config.dim.startWidth
 # Make this a variable, possibly a seperate class called Dimension
	END =  config.dim.endWidth # Abstract this to a seperate class. I think. I might be wrong. Same class as variable above. 
	RADIANS = 2 * np.pi
	x = np.arange(START, END, config.res.step)
	y = ((config.dim.startHeight - config.dim.endHeight)/2) * np.sin(x * RADIANS)
	z = [config.dim.startLength for k in range(len(x))] # Idk, I mean this seems fine right? Every coordiange will have 1 as the depth. Eh.
	#The u,v,w components don't really matter for the calculation, but for displaying they should be to an apporproiate scale.
	
	u = [config.dim.width/0.05 for k in range(len(x))]   #TODO
	v = [config.dim.height/0.05 for k in range(len(x))] #TODO
	w = [config.dim.startLength for k in range(len(x))]
	
	return vector_field.VectorField(x,y,z,u,v,w)
