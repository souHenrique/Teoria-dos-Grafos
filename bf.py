optimal_tour_length = {
    1: 33523,
    2: 699,
    3: 19,
    4: 937,
    5: 2085,
    6: 291
}

def approximate_tsp(graph, start, file_index):
    tour = [start]
    current_node = start
    total_weight = 0

    while len(tour) < len(graph):
        min_distance = float('inf')
        next_node = None
        for neighbor, weight in enumerate(graph[current_node], start=1):
            if neighbor not in tour and neighbor != start and weight < min_distance:
                min_distance = weight
                next_node = neighbor
        
        total_weight += min_distance
        tour.append(next_node)
        current_node = next_node

    total_weight += graph[current_node][start]
    tour.append(start)
    optimal_length = optimal_tour_length.get(file_index, None)
    percentage_difference = abs(total_weight - optimal_length) / optimal_length * 100
    
    print(f"Tour: {tour}\nPeso total: {total_weight}\nValor esperado: {optimal_length}\nMargem de erro: {percentage_difference:.3f}%")