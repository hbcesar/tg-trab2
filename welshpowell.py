from grafo import Grafo
from cor import Cor
from collections import deque
import random

class WelshPowell(object):
	def update(self, cores, cor):
		for c in cores:
			if c.name is cor:
				c.update()

	def wp(self, G):
		#aqui rola um while ha vertices nao coloridos
		coloridos = []
		n = G.n * G.n
		cores = []

		for i in range(n):
			cores.append(Cor(i))

		resposta = G.vertices

		while len(coloridos) is not n*n:
			#encontra os vertices ja coloridos e remove a possibilidade daquela cor nos seus adjacentes
			for v in resposta:
				if v.status:
					for e in v.edges:
						try:
							e.colors.remove(v.colors)
						except:
							pass


			#encontra qual a menor possibilidade de escolhas de cor atual
			menor = n
			for v in resposta:
				if not v.status:
					if len(v.colors) < menor:
						menor = len(v.colors)

			#encontra vertices com essa menor possibilidade
			menores = []
			for v in resposta:
				if not v.status:
					if len(v.colors) is menor:
						menores.append(v)


			#se apos eliminacao de possibilidades, houverem vertices com apenas uma
			#defina essa como a cor escolhida
			for v in menores:
				if len(v.colors) is 1:
					self.update(cores, v.colors[0])
					v.colorir(v.colors[0])
					menores.remove(v)

			#dos vertices com menor propabilidade de cores que ainda nao foram coloridos (se houver)
			#encontra o que possui a maior quantidade de vizinhos nao coloridos
			if(menores):
				maior = 0
				atual = []
				for v in menores:
					count = 0
					for e in v.edges:
						if not e.status:
							count += 1
					if count >= maior:
						if count is maior:
							atual.append(v)
						elif count > maior:
							atual = []
							atual.append(v)
							maior = count

				#escolhe randomicamente entre eles
				v = random.choice(atual)

				#pinta o vertice escolhido com a cor de menor instancia
				cores.sort()

				for cor in cores:
					tem = False
					for e in v.edges:
						if e.status and e.colors is cor.name:
							tem = True
					if not tem:
						cor.update()
						v.colorir(cor.name)
						break

			#checa se solucao ainda e possivel
			for v in resposta:
				if not v.status and len(v.colors) is 0:
					print "Falha ao encontra solucao"
					return False

			#atualiza lista de vertices ja coloridos
			for v in resposta:
				if v.status and v not in coloridos:
					coloridos.append(v)

			G.resposta = resposta

		return True
