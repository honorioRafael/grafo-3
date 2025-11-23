from typing import Final
from node import Node
from important_types import Adjacencies, Degree, NodeNeighbors, Pairs, Path

ORIGIN: Final = 0
DESTINATION: Final = 1

# TODO: work on something if we only have one Node in edgesList
# NOTE: somethings might only work if you don't remove an edge

class AdjacencyList():
	"""Represents a adjancency list of an undirected graph with Nodes."""
	# for now the idea is to just add the graph as dependency
	def __init__(self) -> None:
		self.__adjacencylist: Adjacencies = { "vertices": [], "edges": [] }

	def __removeInVertices(self, verticeName) -> None:
		verticesList = self.__adjacencylist["vertices"]

		for verticeInList in verticesList:
			if(verticeName == verticeInList):
				verticesList.remove(verticeInList)
	
	def __removeInEdges(self, verticeName: str) -> None:
		edgesList = self.__adjacencylist["edges"]

		for pair in range(len(edgesList)):
			for nodeName in edgesList[pair]:
				if(verticeName == nodeName):
					edgesList[pair].remove(nodeName)

	def __isThereNeighbors(self, pairToCheck, existingPair) -> bool:
		origin = pairToCheck[0]
		dest = pairToCheck[1]

		# since it is not directed, we may have BA or AB
		return ((origin == existingPair[0] and dest == existingPair[1]) or (dest == existingPair[0] and origin == existingPair[1]))

	def __initializeDegrees(self) -> Degree:
		degrees: Degree = {}

		for k in self.__adjacencylist["vertices"]:
			degrees[k] = { "din": 0, "dout": 0, "total": 0 }

		return degrees

	def appendVertice(self, vertice: str) -> None:
		if(vertice in self.__adjacencylist["vertices"]):
			raise Exception(f"Vertice {vertice} already exists in list")

		self.__adjacencylist["vertices"].append(vertice)
	
	def appendEdge(self, edge: str, origin: str, dest: str) -> None:
		if(origin not in self.__adjacencylist["vertices"] or dest not in self.__adjacencylist["vertices"]):
			raise Exception("Edge does not exists in list")

		self.__adjacencylist["edges"].append([origin, dest])
		self.__adjacencylist["edges"].append([dest, origin])
	
	def removeVertice(self, verticeName: str) -> None:
		self.__removeInVertices(verticeName)
		self.__removeInEdges(verticeName)
	
	def doesEdgeExists(self, pairToSearch: Pairs) -> bool:
		edgesList = self.__adjacencylist["edges"]

		for pair in range(len(edgesList)):
			if(self.__isThereNeighbors(pairToSearch, edgesList[pair])):
				return True

		return False

	def isPathValid(self, path: Path) -> bool:
		for i in range(len(path) - 1):
			currentPair = [path[i], path[i+1]]

			if(not self.doesEdgeExists(currentPair)):
				return False

		return True
	
	def getNeighboorsFrom(self, verticeName: str, edges: Pairs) -> NodeNeighbors:
		# NOTE: i think there might have a bug here with the current implementation
		edgesList = self.__adjacencylist["edges"]
		neighboors = []

		for pair in edgesList:
			if(verticeName == pair[ORIGIN]):
				neighboors.append(pair[DESTINATION])

		return neighboors

	def printNeighboorsOf(self, verticeName: str, edge: Pairs) -> None:
		neighbors = self.getNeighboorsFrom(verticeName, edge)

		print(f"{verticeName} has of neighboors: {neighbors}")

	def printAdjacenyList(self) -> None:
		edges = self.__adjacencylist["edges"]

		print(self.__adjacencylist["vertices"])

		for pair in self.__adjacencylist["edges"]:
			origin = pair[ORIGIN]
			dest = pair[DESTINATION]

			print(origin,"->",dest)

	def getDegreesFrom(self, verticeName: str) -> Degree:
		edgesList = self.__adjacencylist["edges"]
		totalDegrees = self.__initializeDegrees()

		din = 0
		dout = 0
		total = 0

		for pair in edgesList:
			if(verticeName == pair[0]): dout += 1

			# because it may have been deleted
			if(verticeName == pair[1]): din += 1

			total = din + dout

			totalDegrees[verticeName]["dout"] = dout
			totalDegrees[verticeName]["din"] = din
			totalDegrees[verticeName]["total"] = total

		return totalDegrees

	def getAdjacenyList(self) -> Adjacencies:
		return self.__adjacencylist
