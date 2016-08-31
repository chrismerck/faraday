class Resolution:

	UNITS = { 'yocto':0, 'zepto':3, 'atto':6, 'femto':9, 'pico':12, 
		  'nano':15, 'micro':18, 'mili':21, 'centi':22, 'deci':23, 
		  'base':24, 'deca': 25, 'hecto': 26, 'kilo': 27, 'mega': 30, 
		  'giga': 33, 'tera': 36, 'peta': 39, 'exa': 42, 'zetta': 45, 
		  'yotta':48 }

	def __init__(self, fromUnit, upToUnit, scalarTune=1):

		self.fromUnit = self.UNITS[fromUnit]
		self.upToUnit = self.UNITS[upToUnit]
		self.scalarTune = scalarTune
		self.exp = self.fromUnit - self.upToUnit 
		self.step = 1 / (self.scalarTune * (10**self.exp))
