class Grafo(object):
    def __init__(self, n):
        self.n = n
        self.vertices = []

    def addVertice(v):
        self.vertice.append(v)

    def montar():
        nmrVertices = (self.n * self.n) * (self.n * self.n)

        #cria os vertices
        for i in range(nmrVertices):
            self.vertice.append(new Vertice())

        #adiciona adjacencias as linhas
        for i in range(0, nmrVertices, n*n):
            for j in range(i, i + (n*n)):
                for k in range(i , i + (n*n)):
                    if k is not j:
                        self.vertices[j].adjacente(vertices[k])

        #adiciona adjacencias as colunas
        for i in range(0, n*n):
            for j in range(i, i + nmrVertices - (n*n), (n*n)):
                for k in range(i, i + nmrVertices - (n*n), (n*n)):
                    if k is not j:
                        self.vertices[j].adjacente(vertices[k])

        #adiciona adjacencias aos blocos

        #iniciar algumas cores
