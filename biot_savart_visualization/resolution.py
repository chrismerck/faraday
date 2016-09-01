class Resolution:

	UNITS = { 'yocto':0, 'zepto':3, 'atto':6, 'femto':9, 'pico':12, 
		  'nano':15, 'micro':18, 'mili':21, 'centi':22, 'deci':23, 
		  'base':24, 'deca': 25, 'hecto': 26, 'kilo': 27, 'mega': 30, 
		  'giga': 33, 'tera': 36, 'peta': 39, 'exa': 42, 'zetta': 45, 
		  'yotta':48 }

	def __init__(self, from_unit, up_to_unit, scalar_tune=1):

		self.from_unit = self.UNITS[from_unit]
		self.up_to_unit = self.UNITS[up_to_unit]
		self.scalar_tune = scalar_tune
		self.exp = self.from_unit - self.up_to_unit 
		self.step = 1 / (self.scalar_tune * (10**self.exp))
