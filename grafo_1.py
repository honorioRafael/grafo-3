def adicionar_aresta(grafo, u, v):
    """
    Cria uma conexao direcionada do vertice u para o vertice v no dicionario grafo.
    """
    if u not in grafo:
        grafo[u] = []
    grafo[u].append(v)

def dfs(grafo, vertice_inicial):
    """
    Implementa a busca em profundidade iterativa utilizando uma pilha explicita conforme o pseudo-codigo.
    """
    pilha = [vertice_inicial]
    visitados = set()

    print(f"Iniciando DFS a partir de {vertice_inicial}:")

    while len(pilha) > 0:
        vertice = pilha.pop()
        
        if vertice in visitados:
            continue

        visitados.add(vertice)
        print(vertice, end=' ')

        vizinhos = grafo.get(vertice, [])
        
        for vizinho in reversed(vizinhos):
            if vizinho not in pilha:
                if vizinho not in visitados:
                    pilha.append(vizinho)
    print()

if __name__ == "__main__":
    grafo = {}
    adicionar_aresta(grafo, 'A', 'B')
    adicionar_aresta(grafo, 'A', 'C')
    adicionar_aresta(grafo, 'B', 'C')
    adicionar_aresta(grafo, 'C', 'A')
    adicionar_aresta(grafo, 'C', 'D')
    adicionar_aresta(grafo, 'D', 'D')

    dfs(grafo, 'C')