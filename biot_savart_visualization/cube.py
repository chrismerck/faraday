class Cube:
	""" Describes the bounds of a 3D cube.

	Attributes:
		min_x: The beginning of the cube on the x-axis.
		max_x: The end of the cube on the x-axis.
		min_y: The beginning of the cube on the y-axis.
		max_y: The end of the cube on the y-axis
		min_z: The beginning of the cube on the z-axis.
		max_z: The end of the cube on the z-axis.
		width: The width of the cube described by the min_x and max_y
			parameters.
		height: The height of the cube described by the min_y and max_y
			parameters.
		length: The length (or depth) of the cube described by the
			min_z and max_z parameters.
	"""

	def __init__(self, min_x, max_x, min_y, max_y, min_z, max_z):
		""" Initializes a valid 3D cube.
		
		Note:
			It falls upon the caller to ensure that the paramaters
			create a valid cube. 
			
			A valid cube is one whose width, height and length are
			non negative.
		Args:
			min_x: The beginning of the cube on the x-axis.
			max_x: The end of the cube on the x-axis.
			min_y: The beginning of the cube on the y-axis.
			max_y: The end of the cube on the y-axis
			min_z: The beginning of the cube on the z-axis.
			max_z: The end of the cube on the z-axis.
		"""
		self.min_x = min_x
		self.max_x = max_x

		self.min_y = min_y
		self.max_y = max_y

		self.min_z = min_z
		self.max_z = max_z
		
		self.width = self.max_x - self.min_x
		self.height = self.max_y - self.min_y
		self.length = self.max_z - self.min_z
