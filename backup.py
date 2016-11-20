	#verifica se linha possui cor
	def verifica_linha(self, linha, cor):
		for i in range(self.n * self.n):
			if self.vertices[linha][i].cor is cor:
				return True
		else:
			return False

	#verifica se coluna possui cor
	def verifica_coluna(self, coluna, cor):
		for i in range(self.n * self.n):
			if self.vertices[i][coluna].cor is cor:
				return True
		else:
			return False

	#verifca se bloco possui cor
	def verifica_bloco(self, linha, coluna, cor):
		i = linha
		j = coluna

		#limite direito
		lim = j+1;
		while lim % self.n not 0:
			lim++
		direito = lim

		#limite esquerdo
		lim = j
		while lim % self.n not 0:
			lim--
		esquerdo = lim

		#limite inferior
		lim = i + 1
		while lim % self.n not 0:
			lim++
		inferor = lim

		#superior
		lim = i
		while l % self.n not 0:
			lim--
		superior = lim

		for k in range(superior, inferior):
			for l in range(esquerdo, direito):
				if self.vertices[k][l].cor is cor:
					return True
				else:
					return False


class Queue(object):
	def __init__(self, ):
		self.queue =[]

	def push(self,elem):
		self.queue.insert(0,elem)

	def pop(self):
		return self.queue.pop()

	def isEmpty(self):
		return len(self.queue) == 0

class Stack(object):
	def __init__(self):
		self.stack =[]

	def push(self,elem):
		self.stack.append(elem)

	def pop(self):
		return self.stack.pop()

	def isEmpty(self):
			return len(self.stack) == 0

class Cor(object):
	def __init__(self, n):
		self.n = n
		self.instancias = 0

def compare(v1, v2):
    if v1.grau < v2.grau:
        return -1
    elif v1.grau > v2.grau:
        return 1
    else:
        return 0


#
# def colorir_vertice(G, v):
# 	#confere se pode usar alguma cor que ainda nao foi usada
# 	for c in G.cores:
# 		linha = G.verifica_linha(v.linha, c.n)
# 		coluna = G.verifica_coluna(v.bloco, c.n)
# 		bloco = G.verifica_bloco(v.linha, v.coluna, c.n)
# 		if not linha and not coluna and not bloco:
# 			v.cor = c.n;
# 			c.instancias++
# 			return
#
# 	if v.cor is None:
# 		#nao conseguiu usar nenhuma cor, tentará recoloroção
# 		for c in G.cores:
# 			while not colored;
# 				linha = G.verifica_linha(v.linha, c.n)
# 				coluna = G.verifica_coluna(v.bloco, c.n)
# 				bloco = G.verifica_bloco(v.linha, v.coluna, c.n)
#
# 				if not linha and not coluna and not bloco:
#
#
# 		# 	if c.instancias < menor_instancia:
# 		# 		menor_instancia = c.instancias
# 		#
# 		# melhores_candidatas = []
# 		# for c in G.cores:
# 		# 	if c.instancias is menor_instancia:
# 		# 		melhores_candidatas.append(c)
# 		#
# 		# count = melhores_candidatas.size()
# 		# random_indice = randint(0, count)
# 		#
# 		# v.cor = melhores_candidatas[random_indice].n
# 		# melhores_candidatas[random_indice].instancias++
# 		#
# 		# return true
# 	return False
#
# def coloracaoEmLargura(G):
# 	listaVertices = G.verticesArray()
# 	falhas = 0
#
# 	filaVertices = Queue()
# 	filaVertices.push(listaVertices[0])
#
# 	while not filaVertices.isEmpty():
# 		atual = filaVertices.pop()
#
# 		if atual.cor is None:
# 			result = colorir_vertice(atual, G)
# 			if not result:
# 				falhas += 1
#
# 		for va in atual.edges:
# 			if va.cor is None:
# 				fila.push(v)
#
# 	return falhas
#
#
#
# # def ColoracaoEmProfundidade(G):
# # 	listaVertices = []
# # 	falhas = 0
# #
# # 	pilha = Stack()
# # 	pilha.push(listaVertices[0])
# #
# # 	while not pilha.isEmpty():
# # 		atual = pilha.pop()
# #
# # 		if atual.cor is 0:
# # 			result = colorir_vertice(G)
# # 			if result is 1:
# # 				falhas += 1
# #
# # 		for v in atual.edges:
# # 			if v.cor is 0:
# # 				pilha.push(v)
# #
# # 	return falhas
