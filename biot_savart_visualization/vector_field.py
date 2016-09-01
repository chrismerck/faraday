import numpy as np

class VectorField:
	
	def __init__(self, x, y, z, u, v, w):
		
		self.keys = list(zip(x, y, z))
		self.vec_field = {self.keys[i] : (u[i], v[i], w[i]) 
				  for i in range(len(self.keys))}

	def scale(self, vec_scale):
		
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
