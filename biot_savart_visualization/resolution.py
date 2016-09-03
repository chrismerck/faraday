class Resolution:
	""" Allows for an easy solution to the problem of solving
		for the 'step' required to perform interpolation at a 
		specific resolution.

	Attributes:
		UNITS_MAG (dict): A dictionary of the SI unit prefixes as the
			keys and the corresponding SI unit exponent shifted up 
			by 24 as the values.
		
			This shift occurs due to the necessity of the magnitude 
			of the unit, not the unit's exponent per se. 
		from_unit (str): An index into UNITS_MAG. Is the bigger unit
			of the two that are involved in the resolution 
			calcuation. 
		up_to_unit (str): An index into UNITS_MAG. Is the smaller unit
			of the two that are involved in the resolution 
			calcluation.
		scalar_tune: A scalar value for fine tuning the step of the
			interpolation.
		magnitude: The magnitude of the calculation. Can also be
			thought of as the ratio of from_unit:up_to_unit 
			assuming the scalar_tune is 1.
		step: The reciprocal of magnitude. This is the final value used
			whenever an interpolation at a given resolution is 
			needed.

	"""
	UNITS_MAG = { 'yocto':0, 'zepto':3, 'atto':6, 'femto':9, 'pico':12, 
		  'nano':15, 'micro':18, 'mili':21, 'centi':22, 'deci':23, 
		  'base':24, 'deca': 25, 'hecto': 26, 'kilo': 27, 'mega': 30, 
		  'giga': 33, 'tera': 36, 'peta': 39, 'exa': 42, 'zetta': 45, 
		  'yotta':48 }

	def __init__(self, from_unit, up_to_unit, scalar_tune=1):
		""" Calculates the appropriate step in respect to the
		paramaters.
	
		Args:
			from_unit (str): An index into UNITS_MAG. Is the bigger 
				unit of the two that are involved in the 
				resolution calcuation. 
			up_to_unit (str): An index into UNITS_MAG. Is the 
				smaller unit of the two that are involved in 
				the resolution calcluation.
			scalar_tune: A scalar value for fine tuning the step 
				of the interpolation.			

		"""

		self.from_unit = self.UNITS_MAG[from_unit]
		self.up_to_unit = self.UNITS_MAG[up_to_unit]
		self.scalar_tune = scalar_tune
		self.magnitude = self.scalar_tune * (10
				 ** (self.from_unit-self.up_to_unit))
		self.step = 1 / self.magnitude
