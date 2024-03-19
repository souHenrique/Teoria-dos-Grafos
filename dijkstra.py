import heapq

optimal_tour_length = {
    1: 33523,
    2: 699,
    3: 19,
    4: 937,
    5: 2085,
    6: 291
}

def dijkstra(graph, start, file_index):
    distancia_total = 0
    distancia = {vertex: float('inf') for vertex in range(1, len(graph) + 1)}
    distancia[start] = 0
    queue_de_prioridade = [(0, start)]

    tamanho_otimo = optimal_tour_length.get(file_index)
    threshold_distance = tamanho_otimo * 1.5

    while queue_de_prioridade:
        current_distance, current_vertex = heapq.heappop(queue_de_prioridade)

        if current_distance > distancia[current_vertex]:
            continue

        distancia_total += current_distance

        if distancia_total > threshold_distance:
            break

        for vizinho, peso in enumerate(graph[current_vertex], start=1):
            if peso > 0:
                distancia = current_distance + peso
                if distancia < distancia[vizinho]:
                    distancia[vizinho] = distancia
                    heapq.heappush(queue_de_prioridade, (distancia, vizinho))

    porcentagem_da_diferenca = abs(distancia_total - tamanho_otimo) / tamanho_otimo * 100

    print(f"Peso total: {distancia_total}\nValor esperado: {tamanho_otimo}\nMargem de erro: {porcentagem_da_diferenca:.3f}%")