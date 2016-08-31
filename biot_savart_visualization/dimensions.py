
class Dimensions:

	def __init__(self,startWidth,endWidth,startHeight,endHeight,startLength,endLength):

		self.startWidth= startWidth # x
		self.endWidth = endWidth
 
		self.startHeight = startHeight # y
		self.endHeight = endHeight

		self.startLength = startLength # z
		self.endLength = endLength
		
		
		self.width = self.endWidth - self.startWidth
		self.height = self.endHeight - self.startHeight
		self.length = self.endLength - self.startLength
