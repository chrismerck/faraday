""" Functions in this file calculate the Biot-Savart equation. """

import vector_field as VectorField
import numpy as np
from numpy import linalg

def _dB_calc(J_field, x, y, z):
	""" Calcualtes the magnetic field at a point due to a current.
		
	Args:
		J_field (VectorField): Vector field describing the current
			that the magnetic field is generated from. 
		x: The x coordinate of the point in the magnetic field.
		y: The y coordinate of the point in the magnetic field.
		z: The z coordinate of the point in the magnetic field.
	Returns:
		tuple (u,v,w): A tuple with the magnitude of the magnetic field
			at the point (x,y,z).
	"""
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
	""" Calcualtes and generates a magnetic field due to a current.
	
	Args:
		B_config (PlotConfig): Holds the configuration for the bounds
			of the returned magnetic field and the
			resolution of the returned magnetic field.
		J_field (VectorField): The vector field that describes the
			current density at a set of points.
	Returns:
		VectorField: Returns a magnetic field generated from an
			electric current.
	"""
	bound = B_config.bound
	res = B_config.res

	x = []
	y = []
	z = []

	u = []
	v = []
	w = []
	
	for _x in np.arange(bound.min_x, bound.max_x, res.step):
		for _y in np.arange(bound.min_y, bound.max_y, res.step):
			for _z in np.arange(bound.min_z, bound.max_z,
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
