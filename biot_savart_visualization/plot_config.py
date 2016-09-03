class PlotConfig:
	""" Container class for the settings that are used when the 
	generation of vector fields occur.

	The settings include the resolution and the bounds of the vector field. 

	Attributes:
		res (Resolution): The resolution at which any calculations 
			upon an object should take place in.
		bound (Cube): The cubic bounds of an object in space.

	Todo:
		- Is this class even necessary?
	"""


	def __init__(self, res, bound):
		"""
		Args:
			res (Resolution): The resolution at which any
				calculations upon an object should take place
				in.
			bound (Cube): The cubic bounds of an object in space.
		"""
		self.res = res
		self.bound = bound
