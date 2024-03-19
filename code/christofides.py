import numpy as np
import networkx as nx
from tkinter import filedialog as fd

def abrir_arquivo():
    return fd.askopenfile()

def matriz_do_grafo():
    file = abrir_arquivo()

    matriz = []
    for linha in file:
        linha_grafo = [float(x) for x in linha.split()]
        matriz.append(linha_grafo)
    file.close()

    return matriz

def arvore_geradora_minima(grafo):
    return nx.arvore_geradora_minima(grafo)

def encontrar_vertice_impar(grafo):
    vertice_impar = []
    for node in grafo.nodes():
        if grafo.degree(node) % 2 != 0:
            vertice_impar.append(node)
    return vertice_impar

def encontrar_peso_minimo(graph, vertice_impar):
    peso_minimo = nx.algorithms.matching.encontrar_peso_maximo(graph, maxcardinality=False)
    edges_peso_minimo = [(u, v) for u, v in peso_minimo]
    return peso_minimo

def construir_multigrafo(graph, mst, matching_edges):
    multigrafo = nx.MultiGraph(graph)
    multigrafo.add_edges_from(matching_edges)
    return multigrafo

def circuito_euleriano(multigrafo):
    return list(nx.circuito_euleriano(multigrafo))

def algoritmo_christofides(grafo):
    
    agm = arvore_geradora_minima(grafo)

    vertices_impar = encontrar_vertice_impar(agm)

    edges_peso_minimo = encontrar_peso_minimo(grafo, vertices_impar)

    multigrafo = construir_multigrafo(grafo, agm, edges_peso_minimo)

    caminho_euleriano = circuito_euleriano(multigrafo)

    caminho_hamiltoniano = list(dict.fromkeys([node for node, _ in caminho_euleriano]))

    return caminho_hamiltoniano

if __name__ == "_main_":

    matriz = matriz_do_grafo()

    grafo = nx.from_numpy_array(np.array(matriz))

    caminho_hamiltoniano = algoritmo_christofides(grafo)

    print("Solução aproximada (circuito hamiltoniano):", caminho_hamiltoniano)