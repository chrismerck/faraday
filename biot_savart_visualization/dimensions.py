class Dimensions:

	def __init__(self, start_width, end_width, start_height, end_height,
		     start_length, end_length):
		
		self.start_width = start_width
		self.end_width = end_width

		self.start_height = start_height
		self.end_height = end_height

		self.start_length = start_length
		self.end_length = end_length
		
		self.width = self.end_width - self.start_width
		self.height = self.end_height - self.start_height
		self.length = self.end_length - self.start_length
