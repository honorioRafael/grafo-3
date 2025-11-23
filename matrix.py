from typing import Final
from important_types import Pairs

ORIGIN: Final = 0
DESTINATION: Final = 1

class Matrix():
	def __init__(self, matrixSize: int) -> None:
		self.__matrix = []
		self.__vertices = []

		self.__setMatrixToSize(matrixSize)

	def __isAVertice(self, nodeName: str) -> bool:
		vertices = self.__vertices
		return (nodeName in vertices)

	# https://www.youtube.com/watch?v=B28xAWEerK8	
	def __setMatrixToSize(self, size: int) -> None:
		# no python BS
		for _ in range(size):
			cols = []

			for _ in range(size):
				cols.append(False)

			self.__matrix.append(cols)
	
	def appendVertice(self, verticeName: str) -> None:
		vertices = self.__vertices

		if(self.__isAVertice(verticeName)):
			raise Exception(verticeName,"already exists")

		vertices.append(verticeName)
		
	def appendEdge(self, pair: Pairs) -> None:
		vertices = self.__vertices
		originIndx = 0
		destIndx = 0

		if(not self.__isAVertice(pair[ORIGIN])): self.appendVertice(pair[DESTINATION])
		if(not self.__isAVertice(pair[ORIGIN])): self.appendVertice(pair[DESTINATION])

		originIndx = vertices.index(pair[ORIGIN])
		destIndx = vertices.index(pair[DESTINATION])

		self.__matrix[originIndx][destIndx] = True
		self.__matrix[destIndx][originIndx] = True
	
	def removeVertice(self, verticeName: str) -> None:
		originIndx = 0
		destIndx = 0

		if(not self.__isAVertice(verticeName)):
			raise Exception(verticeName,"does not exists")


		self.__matrix[originIndx][destIndx] = False
		self.__matrix[destIndx][originIndx] = False

	def removeEdge(self, pair: Pairs) -> None:
		if(not self.__isAVertice(pair[ORIGIN])):
			raise Exception(pair[ORIGIN],"Does not exits")

		if(not self.__isAVertice(pair[DESTINATION])):
			raise Exception(pair[DESTINATION],"Does not exits")

		lineIndx = self.__vertices.index(pair[ORIGIN])
		columnIndx = self.__vertices.index(pair[DESTINATION])

		self.__matrix[lineIndx][columnIndx] = False
		self.__matrix[columnIndx][lineIndx] = False

	def printMatrix(self) -> None:
		for i in range(len(self.__matrix)):
			for j in range(len(self.__matrix[i])):
				print(self.__matrix[i][j], end='\t')

			print()

	def getMatrix(self) -> list:
		return self.__matrix
	
	def getVertices(self) -> list:
		return self.__vertices
