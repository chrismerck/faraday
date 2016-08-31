import vector_field
import numpy as np
from numpy import linalg

def _dB_calc(J_field,x,y,z):
	'''
                Description: Calculates the dB for a specific point. Not the entire magnetic field at that point but just one part.
                Params: //:TODO, document
                Return: Vector representing the B at a point
	'''
	B = (0,0,0)
	for JVec,v in J_field.vec_field.items(): #JVec is the key also.

		biotSavartConstant = 10 ** (-7) # The constant reduces down to this since the 4pi cancel out.
		distVec = (x - JVec[0],y - JVec[1],z - JVec[2])
		distVecMag = linalg.norm(distVec) # Distance between the two points.
		distVecUnit = (distVec[0]/distVecMag,distVec[1]/distVecMag,distVec[2]/distVecMag) # Direction between the two points.

		crossProduct = np.cross(JVec,distVecUnit)
		dB = (biotSavartConstant * crossProduct) / (distVecMag ** 2)

		B = np.add(B,dB)

	return B

def Biot_Savart(B_config,J_field):
	'''
                Description: Calcualtes the magnetic field based on a current.
                Params: //:TODO, document, dimensions of cube and J is the current density vector field.
                Return: Magnetic field
	'''

	dim = B_config.dim
	res = B_config.res
	scale = B_config.scale

	x = []
	y = []
	z = []

	u = []
	v = []
	w = []

	for _x in np.arange(dim.startWidth,dim.endWidth,res.step):
		for _y in np.arange(dim.startHeight,dim.endHeight,res.step):
			for _z in np.arange(dim.startLength,dim.endLength,res.step):
				x.append(_x)
				y.append(_y)
				z.append(_z)
	
				if (_x,_y,_z) not in J_field.keys:
	
					_u,_v,_w = _dB_calc(J_field, _x, _y, _z)
					u.append(_u)
					v.append(_v)
					w.append(_w)

	return vector_field.VectorField(x,y,z,u,v,w)
