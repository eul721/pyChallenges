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

print('Start coloring...')
#TODO: implement recursive coloring algorithm
