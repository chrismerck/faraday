import numpy as np

class VectorField:
	""" Wrapper around a dictionary in order to create a
	more easily managable and extendable type.

		Attributes:
			keys (list): The (x,y,z) coordinates of vectors and
				also the list of keys for the raw python dictionary.
			vec_field (dict): The dictionary that contains the
				vector field data. Entries into this dictionary 
				are vectors in the form of '(x,y,z):(u,v,w)'.

	"""	
	def __init__(self, x, y, z, u, v, w):
		""" Creates a vector field from the paramaters. The data
		structure used to represent the field is a dictionary.

		Note:
			Responsibility falls upon the caller to ensure that all
				of the parameters are equal in length.

		Args:
			x: The positonal x components of the vectors inside the
				vector field.
			y: The positonal y components of the vectors inside the 
				vector field.
			z: The positonal z components of the vectors inside the
				vector field.
			u: The magnitudes in the x direction of the vectors
				inside the vector field. 
			v: The magnitudes in the y direction of the vectors
				inside the vector field.
			w: The magnitudes in the z direction of the vectors
				inside the vector field.

		"""
		self.keys = list(zip(x, y, z))
		self.vec_field = {self.keys[i] : (u[i], v[i], w[i]) 
				  for i in range(len(self.keys))}

	def scale(self, vec_scale):
		""" Scales the vector field's vector magnitudes in accordance
		to the settings in vec_scale. 
		
		Once a vector's magnitude is scaled, it is checked for being
		too small, or too large. If one of these conditions is true,
		the vector's magnitude is set to the minimum or maximum value 
		respectively.
		
			Args:
				vec_scale (VF_Scale): Holds the scale value,
					the minumum vector magnitude, and the 
					maximum vector magnitude.
					
			Returns:
				VectorField: Returns self which is now the
					modified and scaled version of the
					vector field.

		"""
		mag_scale = vec_scale.mag_scale
		min_mag_scale = vec_scale.min_mag
		max_mag_scale = vec_scale.max_mag

		for pos_vec, mag_vec in self.vec_field.items():
			
			mag = np.linalg.norm(mag_vec)       
	         
			unit_x = mag_vec[0] / mag
			unit_y = mag_vec[1] / mag
			unit_z= mag_vec[2] / mag

			scaled_mag = mag * mag_scale
			
			if scaled_mag < min_mag_scale:
				scaled_vec = (unit_x * min_mag_scale, 
					      unit_y * min_mag_scale, 
					      unit_z * min_mag_scale)    
				self.vec_field[pos_vec] = scaled_vec
			
			elif scaled_mag > max_mag_scale:
				scaled_vec = (unit_x * max_mag_scale,
					      unit_y * max_mag_scale,
					      unit_z * max_mag_scale)
				self.vec_field[pos_vec] = scaled_vec
			
			else:
				scaled_vec = (mag_vec[0] * mag_scale, 
					      mag_vec[1] * mag_scale, 
					      mag_vec[2] * mag_scale)
				self.vec_field[pos_vec] = scaled_vec
		return self
	def unpack(self):
		""" Unpacks the components of a vector field into seperate
		variables.

			Returns:
				tuple (x,y,z,u,v,w): Returns the individual
					components of the vector field in a
					tuple.

		"""
		x = []
		y = []
		z = []

		u = []
		v = []
		w = []

		for key, val in self.vec_field.items():
		
			x.append(key[0])
			y.append(key[1])
			z.append(key[2])

			u.append(val[0])
			v.append(val[1])
			w.append(val[2])
						
		return (x, y, z, u, v, w)
