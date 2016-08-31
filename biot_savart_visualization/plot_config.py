import dimensions
import resolution
import vf_scale #are these imports even necessary?

class PlotConfig:

	def __init__(self,res,dim,scale):

		self.res = res
		self.dim = dim
		self.scale = scale
