import heapq


def dijkstra(graph, start, file_index):
    distancia_total = 0
    distancias = {vertice: float('inf') for vertice in range(1, len(graph) + 1)}
    distancias[start] = 0
    fila_de_prioridade = [(0, start)]

    antecessores = {vertice: None for vertice in range(1, len(graph) + 1)}
    path = []

    while fila_de_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_de_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue

        distancia_total += distancia_atual

        if vertice_atual != start:
            path.append(vertice_atual)

        for vizinho, peso in enumerate(graph[vertice_atual], start=1):
            if peso > 0:
                distancia = distancia_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    antecessores[vizinho] = vertice_atual
                    heapq.heappush(fila_de_prioridade, (distancia, vizinho))

    print("Caminho percorrido:", [start] + path)
    print(f"Peso total do caminho: {distancia_total}")
