from pathlib import Path
import sys

import bf

import prim

import christofides

import dijkstra

import conversor


def list_files_in_directory(directory):
    files = list(directory.glob('*'))
    files_dict = {i: file.name for i, file in enumerate(files, start=1)}
    return files_dict

def choose_algorithm():
    print("Escolha o algoritmo:")
    print("1: Prim")
    print("2: Dijkstra")
    print("3: Christofides")
    print("4: Força Bruta")
    alg_choice = input("Digite o número do algoritmo: ")
    return alg_choice

def main():
    src_dir = Path(__file__).resolve().parent / 'bases'
    files_dict = list_files_in_directory(src_dir)

    for index, file in files_dict.items():
        print(f"{index}: {file}")

    try:
        file_index = int(input('Selecione o índice do arquivo: '))
        file_name = files_dict.get(file_index)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return

    if not file_name:
        print("Índice inválido.")
        return

    file_path = src_dir / file_name

    if file_path.exists() and file_path.is_file():
        graph = conversor.Converter(str(file_path)).grafo()

        alg_choice = choose_algorithm()
        print(40*'=')

        if alg_choice == '1':
            prim.prim(graph)
        elif alg_choice == '2':
            start = 1
            dijkstra.dijkstra(graph, start, file_index)
        elif alg_choice == '3':
            christofides.algoritmo_christofides(graph)
        elif alg_choice == '4':
            start = 1
            bf.approximate_tsp(graph, start, file_index)
        else:
            print("Escolha de algoritmo inválida.")
    else:
        print(f"Arquivo '{file_name}' não encontrado no diretório '{src_dir}'.")

if __name__ == "__main__":
    main()
