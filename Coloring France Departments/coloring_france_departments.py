import operator
from MapNode import MapNode



nNodes = int(input("Provide the number of nodes: "))
nodes = {}

for i in range(nNodes):
	thisInput=input("Info for Node " + str(i+1) + " : ")
	info = thisInput.split(' ')
	nodes[info[0]]=MapNode(info[0],info[1:])	



queue = []
colored = []

#TODO: implement recursive coloring algorithm

print('Node with most neighbors : ' + str(MapNode.GetNodeWithMostNeighbors(nodes)))
queue.append(MapNode.GetNodeWithMostNeighbors(nodes))

print('Start coloring...')

colors = [0];
while len(queue) > 0:
	cur_node = queue[0]
	cur_node.CacheAvailableColors(colors)
