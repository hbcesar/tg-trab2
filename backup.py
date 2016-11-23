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





def compare(self, v1, v2):
	if v1.grau < v2.grau:
		return -1
	elif v1.grau > v2.grau:
		return 1
	else:
		return 0

def algoritmoIngenuo(self, G):
	#lista de vertices
	vertices = list(G.vertices)

	#ordena os vertices por ordem crescente de grau
	sorted(vertices, cmp=self.compare, reverse=True)

	#transforma a lista em uma fila
	fila = deque(vertices)

	i = 0
	resposta = []

	while fila:
		#pega o primeiro vertice da fila
		v = fila.popleft()

		#variavel de controle
		tem_cor = False

		#verifica se algum dos vertices adjacentes tem a cor
		for adj in v.edges:
			if adj.cor is i:
				tem_cor = True

		#se nenhum dos adjacentes tem aquela cor, preenche com a cor
		if not tem_cor:
			v.colors = i
			v.status = True

		#atualiza i
		i += 1

		#se atingiu o numero maximo de cores, reinicia
		if i >= (G.n * G.n):
			i = 0

		#se v ainda nao foi colorido ele retorna pro comeco da fila
		# if v.cor is None:
			# fila.appendleft(v)
		# elif v not in resposta:
			# resposta.append(v)
		resposta.append(v)

	#salvar a resposta
	# sorted(resposta, key=name)
	G.vertices = resposta

######################### Algortimo de Welsh Powel #############################
#Inicia o algoritmo
def leleo(self, G):
	#recebe vertices em forma de lista
	# vertices = G.verticesArray()
	vertices = G.vertices

	#percorre lista de vertices chamando algoritmo
	for v in vertices:
		if not v.status:
			v.status = True
			self.welshpowel(vertices)
			self.update(vertices)

		#vertices que nao foram preenchidos ficam como 'falhas'
	self.clear(vertices)

	#salva resultados
	# G.falhas = falhas
	# sorted(vertices, key=name)
	# G.resposta = vertices

def welshpowel(self, vertices):
	#percorre lista de vertices
	for v in vertices:
		#se vertice ainda nao foi colorido
		if not v.status:
			#percorre os vizinhos que ja estao coloridos removendo a cor deles na lista de possiveis cores do vertice atual
			for adj in v.edges:
				if adj.status:
					try:
						v.colors.remove(adj.colors)
					except:
						pass

def update(self, vertices):
	#percorre todos os vertices atualizando os labels de colorido ou nao
	for v in vertices:
		if not v.status and len(v.colors) == 1:
			v.status = True
			v.colors = v.colors[0]

def clear(self, vertices):
	falhas = 0

	#verifica vertices que nao foram corretamente coloridos
	for v in vertices:
		if v.status and type(v.colors) is not int:
			v.status = False
			falhas += 1

			return falhas

def startWelshPowel(self, G):
	for i in range(9):
		self.leleo(G)
		self.welshpowel(G.vertices)
		self.update(G.vertices)





















def compare(self, v1, v2):
	if v1.grau < v2.grau:
		return -1
	elif v1.grau > v2.grau:
		return 1
	else:
		return 0

def compare2(self, v1, v2):
	if not v1.status and v2.status:
		return -1
	elif v1.status and not v2.status:
		return 1
	else:
		return 0

def WP(self, G):
	vertices = G.vertices

	#ordena os vertices por ordem crescente de grau
	sorted(vertices, cmp=self.compare, reverse=True)

	colors = range(4)

	resposta = []

	vertices[0].colorir(colors[0])
	resposta.append(vertices[0])
	del vertices [0]



	for v in vertices:
		if v.status:
			resposta.append(v)
			vertices.remove(v)

	while vertices:
		# vertices[0].colorir(colors[0])
		# resposta.append(vertices[0])
		# del vertices [0]

		for c in colors:
			for v in vertices:
				has = False

				for adj in v.edges:
					if adj.cor is c:
						has = True

				if not has:
					v.colorir(c)
					resposta.append(v)
					vertices.remove(v)
					continue

	k = 1
	resposta.sort()
	for r in resposta:
		print r.cor,
		if k % 4 is 0:
			print
		k += 1





"""
Step 1: All vertices are sorted according to the decreasing value of their degree in a list V.
Step 2: Colors are ordered in a list C.
Step 3: The first non colored vertex v in V is colored with the first available color in C. available means a color that was not previously used by the algorithm.
Step 4: The remaining part of the ordered list V is traversed and the same color is allocated to every vertex for which no adjacent vertex has the same color.
Step 5: Steps 3 and 4 are applied iteratively until all the vertices have been colored.
"""
