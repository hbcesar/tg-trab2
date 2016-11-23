from grafo import Grafo
from cor import Cor
from collections import deque
import random

class Queue(object):
	def __init__(self, ):
		self.queue =[]

	def push(self,elem):
		self.queue.insert(0,elem)

	def pop(self):
		return self.queue.pop()

	def isEmpty(self):
		return len(self.queue) == 0

class ColoracaoLargura(object):
	def cl(self, G):
		fila = Queue()
		falhas = 0
		cores = []

		for i in range (9):
			cores.append(Cor(i))

		fila.push(G.vertices[0])

		while not fila.isEmpty():
			v = fila.pop()

			#se nao tiver sido colorido ainda
			if not v.status:
				result = self.colorir(G, v, cores)

				#se nao conseguiu colorir, conta falha
				if not result:
					falhas += 1

			#adiciona adjacentes a fila
			for e in v.edges:
				if not e.status and e not in fila.queue:
					fila.push(e)

		G.resposta = G.vertices

		return falhas
	#fim cl

	#tenta colorir o vertice
	def colorir(self, G, v, cores):
		#se vizinhos nao possuem cor, colore com ela
		for c in cores:
			temCor = False

			for e in v.edges:
				if c.name is e.colors:
					temCor = True

			if not temCor:
				v.colorir(c.name)
				c.update()
				return True


		#se nao conseguiu colorir com nenhuma delas
		#sera necessaria recoloracao
		if not v.status:
			for c in cores:
				#tenta encontrar aonde cor esta e ve se pode mudar com ela
				for e in v.edges:
					if e.colors is c.name:
						rolezeiro = e

				if self.mudar(G, rolezeiro, cores):
					return True

		#se ainda nao conseguiu, sera necessario backtrack
		if not v.status:
			#ordena cores por ordem de instancias
			# cores.sort()
			# nInstancias = cores[0].instancias
			nInstancias = 999999999
			for c in cores:
				if c.instancias < nInstancias:
					nInstancias = c.instancias

			#pega todas as cores com menor instancia
			candidatas = []
			for c in cores:
				if c.instancias is nInstancias:
					candidatas.append(c)

			print len(candidatas)

			#seleciona randomicamente cor entre as melhores candidatas
			escolhida = random.choice(candidatas)

			print "escolhida", escolhida

			#pinta com cor escolhida e ripa na xulipa
			v.colors = escolhida.name
			escolhida.update()
			return True
		return False
	#fim colorir

	def mudar(self, G, rolezeiro, cores):
		#tenta outra cor senao a atual
		for c in cores:
			if c.name is not rolezeiro.colors:
				vizinhosTemCor = False
				for e in rolezeiro.edges:
					if c.name is e.colors:
						vizinhosTemCor = True

				#se outra cor pode ser colocada, coloca com raiva
				if not vizinhosTemCor:
					#atualiza numero de instancias (-1) da cor que vai ser removida dele
					for cOld in cores:
						if cOld.name is rolezeiro.colors:
							cOld.downgrade()

					rolezeiro.colorir(c.name)

					#conseguiu usar outra cor
					return True
		#nao conseguiu, senta e chora
		return False
