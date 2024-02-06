class Converter:
    def __init__(self, file) -> None:
        with open(file, 'r') as arquivo:
            linhas = arquivo.readlines()
            self.lista = ' '.join(linhas)
            self.length = len(linhas[0].split())

    def matrix_converter(self):
        grafo = [float(i) for i in self.lista.split()]
        grafo = [grafo[i:i + self.length] for i in range(0, len(grafo), self.length)]
        return grafo

    def grafo(self):
        matriz_convertida = self.matrix_converter()
        grafo_dict = {}

        for i, linha in enumerate(matriz_convertida, start=1):
            grafo_dict[i] = linha

        return grafo_dict