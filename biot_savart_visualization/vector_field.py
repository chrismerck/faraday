import numpy as np
import vf_scale

class VectorField:
	
	def __init__(self,x,y,z,u,v,w):
		
		self.keys = list(zip(x,y,z))
	
		self.vec_field = { self.keys[i] : (u[i],v[i],w[i]) for i in range( len( self.keys)) }

	def scale(self,vec_scale):
		
		magScale = vec_scale.magScale
		minMagScale = vec_scale.minMag
		maxMagScale = vec_scale.maxMag

		for posVec,magVec in self.vec_field.items():
			
			mag = np.linalg.norm(magVec)       
	         
			unitX = magVec[0]/mag
			unitY = magVec[1]/mag
			unitZ = magVec[2]/mag

			scaledMag = mag * magScale
			if scaledMag < minMagScale:
				scaledVec = (unitX * minMagScale, unitY * minMagScale, unitZ * minMagScale)    
				self.vec_field[posVec] = scaledVec
			elif scaledMag > maxMagScale:      
				scaledVec = (unitX * maxMagScale, unitY * maxMagScale, unitZ * maxMagScale)
				self.vec_field[posVec] = scaledVec
			else:                   
				scaledVec = (magVec[0] * magScale, magVec[1] * magScale, magVec[2] * magScale)
				self.vec_field[posVec] = scaledVec
		return self
	
	def unpack(self):
		
		x = []
		y = []
		z = []

		u = []
		v = []
		w = []

		for key,val in self.vec_field.items():
		
			x.append(key[0])
			y.append(key[1])
			z.append(key[2])

			u.append(val[0])
			v.append(val[1])
			w.append(val[2])
						
		return (x,y,z,u,v,w)	
