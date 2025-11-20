def adicionar_aresta(grafo, u, v):
    """
    Adiciona uma aresta entre dois vertices.
    """
    if u not in grafo:
        grafo[u] = []
    if v not in grafo:
        grafo[v] = []
    grafo[u].append(v)

def tem_ciclo(grafo):
    """
    Itera sobre todos os vertices para garantir a verificacao em grafos desconexos e chama a deteccao iterativa.
    """
    visitados = set()
    vertices = list(grafo.keys())

    for vertice_inicial in vertices:
        if vertice_inicial not in visitados:
            if detectar_ciclo_iterativo(grafo, vertice_inicial, visitados):
                return True
    return False

def detectar_ciclo_iterativo(grafo, vertice_inicial, visitados_global):
    """
    Implementa a deteccao de ciclos usando pilha e rastreamento do pai conforme o pseudo-codigo fornecido.
    """
    pilha = [(vertice_inicial, None)]
    
    visitados_locais = set()

    while len(pilha) > 0:
        item = pilha.pop()
        vertice_atual, pai = item

        if vertice_atual in visitados_locais:
            continue

        visitados_locais.add(vertice_atual)
        visitados_global.add(vertice_atual)

        vizinhos = grafo.get(vertice_atual, [])

        for vizinho in vizinhos:
            
            vizinho_na_pilha = False
            for v_p in pilha:
                if v_p[0] == vizinho:
                    vizinho_na_pilha = True
                    break
            
            vizinho_visitado = vizinho in visitados_locais

            if not vizinho_na_pilha and not vizinho_visitado:
                pilha.append((vizinho, vertice_atual))
            else:
                if vizinho != pai:
                    return True
    
    return False

if __name__ == "__main__":
    grafo_com_ciclo = {}
    adicionar_aresta(grafo_com_ciclo, 'A', 'B')
    adicionar_aresta(grafo_com_ciclo, 'B', 'C')
    adicionar_aresta(grafo_com_ciclo, 'C', 'A') 
    
    print(f"Grafo 1 tem ciclo? {tem_ciclo(grafo_com_ciclo)}")

    grafo_sem_ciclo = {}
    adicionar_aresta(grafo_sem_ciclo, 'X', 'Y')
    adicionar_aresta(grafo_sem_ciclo, 'Y', 'Z')
    adicionar_aresta(grafo_sem_ciclo, 'X', 'W')
    
    print(f"Grafo 2 tem ciclo? {tem_ciclo(grafo_sem_ciclo)}")