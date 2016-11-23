from vertice import Vertice

class Grafo(object):
	def __init__(self, n):
		self.n = n
		self.vertices = [[0 for x in range(n*n)] for y in range(n*n)]

	def colorir(self, i, j, color):
		self.vertices[i][j].colorir(color)

	def montar(self):
		n = self.n * self.n
		nmrVertices = (n * n) * (n * n)

		#incializa os vertices
		k = 0
		for i in range(n):
			for j in range(n):
				self.vertices[i][j] = Vertice(k, i, j, self.n)
				k += 1

		#faz adjacencias das linhas e das colunas
		for i in range(n):
			for j in range(n):
				#ajacentes da linha
				for k in range(n):
					if k is not j:
						self.vertices[i][j].adjacente(self.vertices[i][k])

				#ajacentes dacoluna
				for k in range(n):
					if k is not i:
						self.vertices[i][j].adjacente(self.vertices[k][j])

		#adicionando ajacentes do mesmo bloco, jeova has power
		for i in range(n):
			for j in range(n):
				#limite direito
				lim = j+1;
				while lim % self.n is not 0:
					lim += 1
				direito = lim

				#limite esquerdo
				lim = j
				while lim % self.n is not 0:
					lim -= 1
				esquerdo = lim

				#limite inferior
				lim = i + 1
				while lim % self.n is not 0:
					lim += 1
				inferior = lim

				#superior
				lim = i
				while lim % self.n is not 0:
					lim -= 1
				superior = lim

				for k in range(superior, inferior):
					for l in range(esquerdo, direito):
						if k is not i and l is not j:
							if self.vertices[k][l] not in self.vertices[i][j].edges:
								self.vertices[i][j].adjacente(self.vertices[k][l])

	#retorna matriz de vertices como uma lista
	def verticesArray(self):
		n = self.n * self.n
		vl = []

		for i in range(n):
			for j in range(n):
				vl.append(self.vertices[i][j])

		return vl

	#imprime essa porra
	def imprimir(self):
		i = 0
		n = self.n * self.n

		for v in self.resposta:
			print v.colors,
			i += 1
			if i % n is 0:
				print
