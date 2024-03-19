import numpy as np


def arvore_geradora_minima(grafo):
    """Calcula a Árvore Geradora Mínima do grafo."""
    n = len(grafo)
    visitado = [False] * n
    pai = [None] * n
    chave = [float('inf')] * n
    chave[0] = 0

    for i in range(n):
        u = min_key(chave, visitado)
        visitado[u] = True

        for v in range(n):
            if grafo[u][v] > 0 and not visitado[v] and grafo[u][v] < chave[v]:
                pai[v] = u
                chave[v] = grafo[u][v]

    return pai


def min_key(chave, visitado):
    """Encontra o índice do vértice com a menor chave."""
    menor_valor = float('inf')
    menor_indice = -1
    for i in range(len(chave)):
        if chave[i] < menor_valor and not visitado[i]:
            menor_valor = chave[i]
            menor_indice = i
    return menor_indice


def emparelhamento_minimo(grafo, vertices_impares):
    """Encontra um emparelhamento perfeito mínimo."""
    n = len(grafo)
    emparelhamento = [-1] * n
    visitado = [False] * n

    for u in vertices_impares:
        peso_minimo = float('inf')
        indice_minimo = -1
        for v in vertices_impares:
            if u != v and not visitado[v] and grafo[u][v] < peso_minimo:
                peso_minimo = grafo[u][v]
                indice_minimo = v
        visitado[u] = True
        visitado[indice_minimo] = True
        emparelhamento[u] = indice_minimo

    return emparelhamento


def circuito_euleriano(grafo, no_inicial):
    """Encontra um circuito euleriano no grafo."""
    circuito = [no_inicial]
    atual = no_inicial
    while True:
        proximo_no = None
        for i, peso in enumerate(grafo[atual]):
            if peso > 0:
                proximo_no = i
                grafo[atual][i] = 0
                grafo[i][atual] = 0
                circuito.append(proximo_no)
                atual = proximo_no
                break
        if proximo_no is None:
            break
    return circuito


def algoritmo_christofides(graph):
    """Implementação do algoritmo de Christofides."""
    n = len(graph)

    # Construção do grafo completo
    grafo = []
    for i in graph:
        grafo.append(graph[i])

    # Passos do algoritmo de Christofides
    arvore = arvore_geradora_minima(grafo)
    impares = [i for i, grau in enumerate(map(sum, zip(*grafo))) if grau % 2 != 0]
    emparelhamento = emparelhamento_minimo(grafo, impares)

    # Combina a Árvore Geradora Mínima com o emparelhamento perfeito mínimo
    grafo_aumentado = [[0] * n for _ in range(n)]
    for i in range(n):
        if arvore[i] is not None:
            grafo_aumentado[i][arvore[i]] = grafo[i][arvore[i]]
            grafo_aumentado[arvore[i]][i] = grafo[i][arvore[i]]
    for i in range(n):
        if emparelhamento[i] != -1:
            grafo_aumentado[i][emparelhamento[i]] = grafo[i][emparelhamento[i]]
            grafo_aumentado[emparelhamento[i]][i] = grafo[i][emparelhamento[i]]

    # Encontra um circuito euleriano no grafo resultante
    circ_euleriano = circuito_euleriano(grafo_aumentado, 0)

    # Construção do caminho hamiltoniano
    visitados = set()
    caminho_hamiltoniano = []
    for no in circ_euleriano:
        if no not in visitados:
            caminho_hamiltoniano.append(no)
            visitados.add(no)

    # Ajuste para retornar as cidades conforme os índices
    caminho_hamiltoniano = [cidade + 1 for cidade in caminho_hamiltoniano]

    # Certificar-se de que todas as cidades estão no caminho
    for i in range(1, n + 1):
        if i not in caminho_hamiltoniano:
            caminho_hamiltoniano.append(i)

    print(caminho_hamiltoniano)