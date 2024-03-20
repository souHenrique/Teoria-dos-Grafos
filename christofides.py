import numpy as np

def arvore_geradora_minima(grafo_completo):
    #Encontra a Árvore Geradora Mínima do grafo
    num_vertices = len(grafo_completo)
    visitado = [False] * num_vertices
    pai = [None] * num_vertices
    chave = [float('inf')] * num_vertices
    chave[0] = 0

    for vertice_atual in range(num_vertices):
        vertice_selecionado = menor_chave(chave, visitado)
        visitado[vertice_selecionado] = True

        for vertice_adjacente in range(num_vertices):
            if grafo_completo[vertice_atual][vertice_adjacente] > 0 and not visitado[vertice_adjacente] and grafo_completo[vertice_atual][vertice_adjacente] < chave[vertice_adjacente]:
                pai[vertice_adjacente] = vertice_atual
                chave[vertice_adjacente] = grafo_completo[vertice_atual][vertice_adjacente]
    return pai

def menor_chave(chave, visitado):
    #Encontra o índice do vértice com a menor chave
    menor_valor = float('inf')
    menor_indice = -1
    for indice, valor in enumerate(chave):
        if valor < menor_valor and not visitado[indice]:
            menor_valor = valor
            menor_indice = indice
    return menor_indice

def emparelhamento_minimo(grafo_completo, vertices_impares):
    #Encontra um emparelhamento mínimo
    num_vertices = len(grafo_completo)
    emparelhamento = [-1] * num_vertices
    visitado = [False] * num_vertices

    for vertice_impar in vertices_impares:
        peso_minimo = float('inf')
        indice_minimo = -1
        for vertice_adjacente in vertices_impares:
            if vertice_impar != vertice_adjacente and not visitado[vertice_adjacente] and grafo_completo[vertice_impar][vertice_adjacente] < peso_minimo:
                peso_minimo = grafo_completo[vertice_impar][vertice_adjacente]
                indice_minimo = vertice_adjacente
        visitado[vertice_impar] = True
        visitado[indice_minimo] = True
        emparelhamento[vertice_impar] = indice_minimo
    return emparelhamento

def circuito_euleriano(grafo, vertice_inicial):
    #Encontra o circuito euleriano no grafo
    circuito = [vertice_inicial]
    vertice_atual = vertice_inicial
    peso_total = 0 
    while True:
        proximo_vertice = None
        for indice, peso in enumerate(grafo[vertice_atual]):
            if peso > 0:
                proximo_vertice = indice
                peso_total += peso  # Adiciona o peso da aresta ao peso total
                grafo[vertice_atual][indice] = 0
                grafo[indice][vertice_atual] = 0
                circuito.append(proximo_vertice)
                vertice_atual = proximo_vertice
                break
        if proximo_vertice is None:
            break
    return circuito, peso_total

def algoritmo_christofides(graph):
    #Implementa o algoritmo de Christofides
    num_vertices = len(graph)

    grafo_completo = []
    for chave in graph:
        grafo_completo.append(graph[chave])

    #Passos do algoritmo de Christofides
    arvore_geradora = arvore_geradora_minima(grafo_completo)
    vertices_impares = [indice for indice, grau in enumerate(map(sum, zip(*grafo_completo))) if grau % 2 != 0]
    emparelhamento_perfeito = emparelhamento_minimo(grafo_completo, vertices_impares)

    #Combina a Árvore Geradora Mínima com o emparelhamento perfeito mínimo
    grafo_aumentado = [[0] * num_vertices for _ in range(num_vertices)]
    for indice in range(num_vertices):
        if arvore_geradora[indice] is not None:
            grafo_aumentado[indice][arvore_geradora[indice]] = grafo_completo[indice][arvore_geradora[indice]]
            grafo_aumentado[arvore_geradora[indice]][indice] = grafo_completo[indice][arvore_geradora[indice]]
    for indice in range(num_vertices):
        if emparelhamento_perfeito[indice] != -1:
            grafo_aumentado[indice][emparelhamento_perfeito[indice]] = grafo_completo[indice][emparelhamento_perfeito[indice]]
            grafo_aumentado[emparelhamento_perfeito[indice]][indice] = grafo_completo[indice][emparelhamento_perfeito[indice]]

    encontrar_circuito, peso_total = circuito_euleriano(grafo_aumentado, 0)

    #Construir o caminho hamiltoniano
    visitados = set()
    caminho_hamiltoniano = []
    for vertice in encontrar_circuito:
        if vertice not in visitados:
            caminho_hamiltoniano.append(vertice)
            visitados.add(vertice)

    #Retornar as cidades conforme os índices
    caminho_hamiltoniano = [cidade + 1 for cidade in caminho_hamiltoniano]

    #Verificar se todas as cidades estão no caminho
    for indice in range(1, num_vertices + 1):
        if indice not in caminho_hamiltoniano:
            caminho_hamiltoniano.append(indice)

    print("Caminho Hamiltoniano:", caminho_hamiltoniano)
    print("Peso Total do Caminho:", peso_total)
