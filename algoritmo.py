from vertice import Vertice
from collections import deque

def algoritmoIngenuo(g):
    #lista de vertices
    vertices = list(g.vertices)

    #ordena os vertices por ordem crescente de grau
    sorted(vertices, cmp=compare, reverse=True)

    #transforma a lista em uma fila
    vertices = deque(vertices)

    i = 0
	resposta = []

    while vertices:
        #pega o primeiro vertice da fila
        v = vertices.popleft()

        #variavel de controle
        tem_cor = False

        #verifica se algum dos vertices adjacentes tem a cor
        for adj in v.edges:
            if adj.cor is i:
                tem_cor = True

        #se nenhum dos adjacentes tem aquela cor, preenche com a cor
        if not tem_cor:
            v.cor = i

        #atualiza i
        i += 1

        #se atingiu o numero maximo de cores, reinicia
        if i >= (g.n * g.n):
            i = 0

        #se v ainda nao foi colorido ele retorna pro começo da fila
        if v.cor is None:
            vertices.appendleft(v)
		elif v not in resposta:
			resposta.append(v)

	#salvar a resposta
	sorted(resposta, key=name)
	G.resposta = resposta




######################### Algortimo de Welsh Powel #############################
#Inicia o algoritmo
def startWelshPowel(G):
	#recebe vertices em forma de lista
	vertices = G.verticesArray()

	#percorre lista de vertices chamando algoritmo
	for v in vertices:
		if not v.status:
			v.status = True
			welshpowel(vertices)
			update(vertices)

	#vertices que nao foram preenchidos ficam como 'falhas'
	falhas = clear(vertices)

	#salva resultados
	G.falhas = falhas
	sorted(vertices, key=name)
	G.resposta = vertices

def welshpowel(vertices):
	#percorre lista de vertices
	for v in vertices:
		#se vertice ainda nao foi colorido
		if not v.status:
			#percorre os vizinhos que ja estao coloridos removendo a cor deles na lista de possiveis cores do vertice atual
			for adj in v.edges:
				if adj.status:
					try:
						v.colors.remove(ajd.colors)
					except:
						pass

def update(vertices):
	#percorre todos os vertices atualizando os labels de colorido ou nao
	for v in vertices:
		if not v.status and len(v.colors) == 1:
			v.status = True
			v.colors = v.colors[0]

def clear(vertices):
	falhas = 0

	#verifica vertices que nao foram corretamente coloridos
	for v in vertices:
		if not v.status and type(v.colors) is not int:
			v.status = False
			falhas += 1

	return falhas
