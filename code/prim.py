import networkx as nx

def prim(grafo_dict):
    in_agm = set()
    agm_arestas = []
    peso_total_prim = 0
    in_agm.add(1)

    while len(in_agm) < len(grafo_dict):
        borda_minima = (None, None, float('inf'))
        for u in in_agm:
            for v in range(1, len(grafo_dict) + 1):
                peso = grafo_dict[u][v-1]
                if v not in in_agm and 0 < peso < borda_minima[2]:
                    borda_minima = (u, v, peso)
        if borda_minima[0] is not None:
            u, v, peso = borda_minima
            agm_arestas.append((u, v))
            in_agm.add(v)
            peso_total_prim += peso

    print("MST calculada pelo algoritmo de Prim:")
    for u, v in agm_arestas:
        print(f"Aresta: ({u}, {v})")
    print(f"Peso total da MST pelo algoritmo de Prim: {peso_total_prim}")

    G = nx.Graph()
    for u, conexoes in grafo_dict.items():
        for v, peso in enumerate(conexoes, start=1):
            if peso > 0:
                G.add_edge(u, v, weight=peso)

    mst_nx = nx.minimum_spanning_tree(G)
    peso_total_nx = sum(d['weight'] for u, v, d in mst_nx.edges(data=True))

    print(40*'=')
    print("MST calculada pelo NetworkX:")
    for u, v, d in mst_nx.edges(data=True):
        print(f"Aresta: ({u}, {v}) com peso {d['weight']}")
    print(f"Peso total da MST pelo NetworkX: {peso_total_nx}")