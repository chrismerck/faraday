import vector_field as VectorField
import numpy as np
from numpy import linalg

def _dB_calc(J_field, x, y, z):
	
	B = (0, 0, 0)
	for coordinates, mag in J_field.vec_field.items():

		biot_savart_constant = 10 ** (-7)

		distance = (x - coordinates[0], y - coordinates[1],
			   z - coordinates[2])
		distanceMag = linalg.norm(distance)
		distanceUnit = (distance[0] / distanceMag,
				distance[1] / distanceMag, 
				distance[2] / distanceMag)

		crossProduct = np.cross(coordinates, distanceUnit)
		dB = (biot_savart_constant*crossProduct) / (distanceMag**2)

		B = np.add(B, dB)

	return B

def biot_savart(B_config, J_field):

	dim = B_config.dim
	res = B_config.res

	x = []
	y = []
	z = []

	u = []
	v = []
	w = []
	
	for _x in np.arange(dim.start_width, dim.end_width, res.step):
		for _y in np.arange(dim.start_height, dim.end_height, res.step):
			for _z in np.arange(dim.start_length, dim.end_length,
					    res.step):
	
				if (_x, _y, _z) not in J_field.keys:
					
					x.append(_x)
					y.append(_y)
					z.append(_z)
	
					_u,_v,_w = _dB_calc(J_field, _x, _y,
							    _z)
					
					u.append(_u)
					v.append(_v)
					w.append(_w)
	
	return VectorField.VectorField(x, y, z, u, v, w)
