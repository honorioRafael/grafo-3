from typing import Final
from node import Node
from important_types import(
	NodeNeighbors,
	NodeList,
	NodeConnections,
	NodeOutDegree,
	NodeInDegree,
	NodeTotal,
	Degree,
	Path
)

# TODO: maybe create a NodeException

MINIMAL_TRIVIAL_LENGTH: Final = 2

class Graph():
	"""Represents a undirected graph with Nodes.

	Keyword arguments:

	:param edges: the dictionary to represent the graph as a whole.
	"""
	def __init__(self) -> None:
		self.__edges: dict = {}

	# TODO: create a setEdges

	def __isTrivial(self, pathLength: int) -> bool:
		return (pathLength < MINIMAL_TRIVIAL_LENGTH)

	def __inEdge(self, origin, dest) -> bool:
		edges = self.__edges

		if(origin in edges and dest in edges[origin]): return True

		return False

	def __findOutDegrees(self, verticeName: str) -> NodeOutDegree:
		# here we need the length 'cause we are intrepreting the length
		# as the out degree, because if node A is connecting to other three
		# nodes, then we will have three connections coming OUT from A
		return len(self.__edges[verticeName])

	def __findInDegrees(self, verticeName: str, vertices: NodeNeighbors) -> NodeInDegree:
		# now to get the IN degree, we will need to go back to the start of the graph
		# and search for which node is coming in to vertice
		# we need to get the items 'cause then if we get to the key that is verticeName
		# we will be making things wrong
		din = 0

		if(verticeName in vertices): din += 1

		return din

	def __initializeDegrees(self) -> dict:
		degrees: dict = {}

		for k in self.__edges.keys():
			degrees[k] = {
				"din": 0,
				"dout": 0,
				"total": 0
			}

		return degrees

	def getNeighbors(self, verticeName: str) -> NodeNeighbors:
		edges = self.__edges

		if(verticeName not in edges):
			raise Exception(f"Node '{verticeName}' unknown!")

		return edges[verticeName]

	def getDegreesFrom(self, vertice: Node) -> Degree:
		totalDegrees = self.__initializeDegrees()

		for k,v in self.__edges.items():
			din = 0
			dout = 0
			total = 0

			dout = self.__findOutDegrees(k)
			din = self.__findInDegrees(vertice.getName(), v)
			total = dout + din

			totalDegrees[k]["dout"] = dout
			totalDegrees[k]["din"] = din
			totalDegrees[k]["total"] = total

		return totalDegrees

	def isPathValid(self, path: Path) -> bool:
		pathLength = len(path)

		if(self.__isTrivial(pathLength)): return True

		for i in range(pathLength - 1):
			testPair = (path[i], path[i+1])

			if(not self.__inEdge(testPair[0], testPair[1])):
				return False

		return True

	def appendEdge(self, edgeToAppend: Node) -> None:
		self.__edges[edgeToAppend.getName()] = edgeToAppend.getConnections()

	def removeVertice(self, edgeToRemove: Node) -> None:
		edges = self.__edges
		nameOfEdge = edgeToRemove.getName()

		if(nameOfEdge not in edges):
			raise Exception(f"Edge {nameOfEdge} does not exists")

		for vertices in edges.values():
			for i in range(len(vertices)):
				if(vertices[i] == nameOfEdge): vertices[i] = None

		# TODO: remove this del
		del edges[nameOfEdge]

	def getEdges(self) -> NodeList:
		return self.__edges
