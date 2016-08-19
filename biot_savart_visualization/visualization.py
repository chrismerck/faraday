#TODO: Generalize all of the functions
#TODO: Add a single option that controlls the resolution, or how precise the calculations are going to be
#TODO: Document and and re-write some of the code once everything is working proepry. Just PEP 8 everything. Optimize too.

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg

def Scale_Vector_Field(vectorField,magScale,minMagScale,maxMagScale):
	'''
		Description:
			Allows for the scaling of the quiver vectors so they can be visualized properly.
		Params: 
			@vectorField The vector field that is to be scaled, in the form of a dict that has the values as the magnitude components.
			@magScale A scalar scale value which all of magnetutides are to be scaled by.
			@minMagScale The minumum magnitude of the quiver arrows. A scalar.
			@maxMagScale The maximum magnitude of the quiver arrows. A scalar.
  		
		Return: 
			A vector field scaled to the appropriate values.
	'''

	newVectorField = {}

	for posVec,magVec in vectorField.items():
		
		mag = np.linalg.norm(magVec)

		unitX = magVec[0]/mag
		unitY = magVec[1]/mag
		unitZ = magVec[2]/mag
		
		scaledMag = mag * magScale
		if scaledMag < minMagScale:
			scaledVec = (unitX * minMagScale, unitY * minMagScale, unitZ * minMagScale)
			newVectorField[posVec] = scaledVec
		elif scaledMag > maxMagScale:
			scaledVec = (unitX * maxMagScale, unitY * maxMagScale, unitZ * maxMagScale)
			newVectorField[posVec] = scaledVec
		else:			
			scaledVec = (magVec[0] * magScale, magVec[1] * magScale, magVec[2] * magScale)
			newVectorField[posVec] = scaledVec

	return newVectorField

def Biot_Savart_Calc(J,x,y,z):
	'''
		Description: Calculates the dB for a specific point. Not the entire magnetic field at that point but just one part.
		Params: //:TODO, document
		Return: Vector representing the B at a point
	'''
	B = (0,0,0)
	for JVec,v in J.items(): #JVec is the key also.
				
		biotSavartConstant = 10 ** (-7) # The constant reduces down to this since the 4pis cancel out.
		distVec = (x - JVec[0],y - JVec[1],z - JVec[2])
		distVecMag = linalg.norm(distVec) # Distance between the two points.
		distVecUnit = (distVec[0]/distVecMag,distVec[1]/distVecMag,distVec[2]/distVecMag) # Direction between the two points.
	
		crossProduct = np.cross(JVec,distVecUnit)
		dB = (biotSavartConstant * crossProduct) / (distVecMag ** 2)
		
		B = np.add(B,dB)
		
	return B
	
def B_Field_Calc(width, height, length, J, JKeys):
	'''
		Description: Calcualtes the magnetic field based on a current.
		Params: //:TODO, document, dimensions of cube and J is the current density vector field.
		Return: Magnetic field
	'''
	
	B_Field = {}
	
	for x in range(width):
		for y in range(height):
			for z in range(length):
				B_Field_Key = (x,y,z)
				if B_Field_Key not in JKeys:
					B_Field[B_Field_Key] = Biot_Savart_Calc(J, x, y, z)
	return B_Field

def Plot_B_Field(width,height,length):
	'''
		Description: Plots a quiver plot of the magnetic field around a current.
		Params: //:TODO, document, dimensions of cube and J is the current density vector field.
		Return: None
	'''
	
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.view_init(elev=18, azim=30)

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	ax.set_xlim([0,width])
	ax.set_ylim([0,height])
	ax.set_zlim([0,length])

	
#Begin Current Density Field Quiver and Generation.
	x = [width/2 for i in range(width)]
	y = [height/2 for i in range(height)]
	z = [i for i in range(length)]

	JKeys = list(zip(x, y, z))

	J = {i : 1 for i in JKeys}

	u = [0 for i in range(width)]
	v = [0 for i in range(height)]
	w = [1 for i in range(length)]
	
	ax.quiver(x, y, z, u, v, w, normalize = True, color = 'r')
#End Current Density Field Quiver and Generation.

#Begin B Field Quiver and Generation.

	MIN_TESLA = 0.1
	MAX_TESLA = 1
	TESLA_SCALE = 1 * (10**6)

	_B = B_Field_Calc(width, height, length, J, JKeys)

	B = Scale_Vector_Field(_B, TESLA_SCALE, MIN_TESLA, MAX_TESLA)

	x = []
	y = []
	z = []
	
	u = []
	v = []
	w = []
	
	for key,value in B.items():
		x.append(key[0])
		y.append(key[1])
		z.append(key[2])
		
		u.append(value[0])
		v.append(value[1])
		w.append(value[2])

	ax.quiver(x, y, z, u, v, w, normalize = False)
#End B Field Quiver and Generation.
	
	plt.show()

Plot_B_Field(7,7,7) # Limitation: Must be a cube. So for example, 
					# the arguments 2,3,5 will not work because they do not for a cube.
