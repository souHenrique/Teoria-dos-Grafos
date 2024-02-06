import numpy as np
from pathlib import Path

def list_files_in_directory(directory):
    files = list(directory.glob('*'))
    files_dict = {i: file.name for i, file in enumerate(files, start=1)}
    return files_dict

def ler_matriz_distancias(arquivo):
    matriz_distancias = np.loadtxt(arquivo, dtype='int')
    tamanho_matriz = len(matriz_distancias)
    return matriz_distancias, tamanho_matriz

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
    src_dir = Path(__file__).resolve().parent / 'bases'
    files_dict = list_files_in_directory(src_dir)

    for index, file in files_dict.items():
        print(f"{index}: {file}")

    try:
        file_index = int(input('Selecione o índice da base de sua escolha: '))
        file_name = files_dict[file_index]
        file_path = src_dir / file_name
    except (ValueError, KeyError):
        print("Índice inválido.")
        return

    if file_path.exists() and file_path.is_file():
        matriz_distancias, tamanho_matriz = ler_matriz_distancias(file_path)  # Obtendo a matriz de distâncias e o tamanho
        ponto_inicial = int(input(f'Informe o ponto inicial [0-{tamanho_matriz - 1}]: '))
        caminho, custo = vizinho_mais_proximo(matriz_distancias, ponto_inicial)
        print('Caminho percorrido:', caminho)
        print('Custo total:', custo)
        
    else:
        print(f"Arquivo '{file_name}' não encontrado no diretório '{src_dir}'.")

if __name__ == '__main__':
    principal()
