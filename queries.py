from adjaceny_list import AdjacencyList

def bfs(aj: AdjacencyList, startNode: str) -> None:
    queue = [startNode]
    visited = []

    while queue:
        firstItem = queue[0]

        queue.remove(firstItem)
        visited.append(firstItem)
        startingNeighbors = aj.getNeighboorsFrom(firstItem)

        for neighbor in range(len(startingNeighbors)):
            # we already visited
            if(startingNeighbors[neighbor] in queue): continue
            if(startingNeighbors[neighbor] in visited): continue

            queue.append(startingNeighbors[neighbor])

    print(visited)