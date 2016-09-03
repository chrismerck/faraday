class VF_Scale:
	""" Holds the settings required for scaling a vector
	field.

	Attributes:
		min_mag: The minimum magnitude of the vectors in the vector
			field.
		max_mag: The maximum magnitude of the vectors in the vector
			field.
		mag_scale: The scalar value that all magnitudes are to be
			scaled by.

	"""

	def __init__(self, min_mag, max_mag, mag_scale):
		"""
		Args:
			min_mag: The minimum magnitude of the vectors in the 
				vector field.
			max_mag: The maximum magnitude of the vectors in the 
				vector field.
			mag_scale: The scalar value that all magnitudes are to 
				be scaled by.

		"""		
		self.min_mag = min_mag
		self.max_mag = max_mag
		self.mag_scale = mag_scale
