class MapNode:
	kMaximumAvailableColors = 0

	def __init__ (self, uniqid, neighbors):
		self.uniqid = uniqid
		self.neighbors = neighbors
		self.color = None
		self.availableColors = []

	def SetColor(self,color):
		self.color = color
	def InitializeAvailableColors(self,k):
		kMaximumAvailableColors = k

	def __repr__(self):
		return "Node " + str(self.uniqid)+ " with neighbors " + str(self.neighbors) + " and color " + str(self.color) + "."
	def __str__(self):
		return "Node " + str(self.uniqid)+ " with neighbors " + str(self.neighbors) + " and color " + str(self.color) + "."
