import vector_field as VectorField
import numpy as np
from numpy import linalg

def _dB_calc(J_field, x, y, z):
	
	B = (0, 0, 0)
	for JVec, v in J_field.vec_field.items():

		biotSavartConstant = 10 ** (-7)
		distVec = (x - JVec[0], y - JVec[1], z - JVec[2])
		distVecMag = linalg.norm(distVec)
		distVecUnit = (distVec[0]/distVecMag,
			       distVec[1]/distVecMag, distVec[2]/distVecMag)

		crossProduct = np.cross(JVec, distVecUnit)
		dB = (biotSavartConstant*crossProduct) / (distVecMag**2)

		B = np.add(B, dB)

	return B

def Biot_Savart(B_config, J_field):

	dim = B_config.dim
	res = B_config.res

	x = []
	y = []
	z = []

	u = []
	v = []
	w = []
	
	for _x in np.arange(dim.startWidth, dim.endWidth, res.step):
		for _y in np.arange(dim.startHeight, dim.endHeight, res.step):
			for _z in np.arange(dim.startLength, dim.endLength,
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
