import numpy as np
import os

def ler_matriz_distancias(arquivo):
    return np.loadtxt(arquivo, dtype='int')

def vizinho_mais_proximo(matriz_distancias, ponto_inicial):
    numero_de_cidades = len(matriz_distancias)
    visitados = [ponto_inicial]
    custo_total = 0
    
    ponto_atual = ponto_inicial
    
    while len(visitados) < numero_de_cidades:
        menor_distancia = float('inf')
        proxima_cidade = None
        
        for cidade in range(numero_de_cidades):
            if cidade not in visitados and matriz_distancias[ponto_atual][cidade] < menor_distancia:
                menor_distancia = matriz_distancias[ponto_atual][cidade]
                proxima_cidade = cidade
        
        ponto_atual = proxima_cidade
        custo_total += menor_distancia
        visitados.append(ponto_atual)
    
    custo_total += matriz_distancias[ponto_atual][ponto_inicial]
    visitados.append(ponto_inicial)
    
    return visitados, custo_total

def principal():
    diretorio_script = os.path.dirname(os.path.realpath(__file__))
    arquivo = os.path.join(diretorio_script, 'distancia.txt')
    ponto_inicial = int(input('Informe o ponto inicial [0-14]: '))
    
    matriz_distancias = ler_matriz_distancias(arquivo)
    caminho, custo = vizinho_mais_proximo(matriz_distancias, ponto_inicial)
    
    print('Caminho percorrido:', caminho)
    print('Custo total:', custo)

if __name__ == '__main__':
    principal()