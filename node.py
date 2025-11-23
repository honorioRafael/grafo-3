class Node():
    def __init__(self, name: str, connections: list[str]) -> None:
        self.__name = name
        self.__connections = connections

    def getName(self) -> str:
        return self.__name
    
    def getConnections(self):
        return self.__connections
    
    def appendEdge(self, nodeName) -> None:
        self.__connections.append(nodeName)
