class MapNode:
	kMaximumAvailableColors = 0

	def __init__ (self, uniqid, neighbors):
		self.uniqid = uniqid
		self.neighbors = neighbors
		self.color = None
		self.available_colors= []

	def SetColor(self,color):
		self.color = color
	def InitializeAvailableColors(self,k):
		kMaximumAvailableColors = k

	def __repr__(self):
		return "Node " + str(self.uniqid)+ " with neighbors " + str(self.neighbors) + " and color " + str(self.color) + "."
	def __str__(self):
		return "Node " + str(self.uniqid)+ " with neighbors " + str(self.neighbors) + " and color " + str(self.color) + "."

	@staticmethod
	def GetNodeWithMostNeighbors(nodes):
		if not isinstance(nodes,dict):
			raise TypeError('nodes is not a dict')
		for node in nodes:
			if not isinstance(nodes[node],MapNode):
				raise TypeError('dict contains non-node elements')
		candidate = nodes[min(nodes)]	
		for node in nodes:
			if len(nodes[node].neighbors) > len(candidate.neighbors):
				candidate = nodes[node]  
		return candidate
	def CacheAvailableColors(self,total_colors):
		available_colors = total_colors
		for neighbor in self.neighbors:
			if self.neighbors[neighbor].color in total_colors:
				available_colors.remove(self.neighbors[neighbor].color)	
		self.available_colors = available_colors;
