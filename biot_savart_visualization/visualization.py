#TODO: Generalize all of the functions
#TODO: Add a single option that controlls the resolution, or how precise the calculations are going to be
#TODO: Document and and re-write some of the code once everything is working proepry. Optimize too.

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg

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
	# Dimensions of cube 
	
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
	x = [3 for x in range(width)] # Creates a list of 11 numbers '6' -
	y = [3 for x in range(height)] # Creates a list of 11 numbers '6'  -- These lists are the x,y,z coordinate pairs.
	z = [x for x in range(length)] # Creates a list of 1,2,3,4...,11. -

	JKeys = zip(x, y, z)

	J = {x : 1 for x in JKeys}

	u = [0 for x in range(width)]
	v = [0 for x in range(height)]
	w = [1 for x in range(length)]
	
	ax.quiver(x, y, z, u, v, w, length=0.5, color = 'r')
#End Current Density Field Quiver and Generation.

#Begin B Field Quiver and Generation.
	B = B_Field_Calc(width, height, length, J, JKeys)

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

	ax.quiver(x, y, z, u, v, w, length=0.5)
#End B Field Quiver and Generation.
	
	plt.show()

Plot_B_Field(6,6,6) # Limitation: Must be a cube. So for example, 
					# the arguments 2,3,5 will not work because they do not for a cube.