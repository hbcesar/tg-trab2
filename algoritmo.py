#**************************************************************
#           2º Trabalho de Teoria dos Grafos
#              César Henrique Bernabé
#                   João Reis
#**************************************************************

from vertice import Vertice
from collections import deque
import sys

def compare(v1, v2):
    if v1.grau < v2.grau:
        return -1
    elif v1.grau > v2.grau:
        return 1
    else:
        return 0

def algoritmoGuloso(g):
    #lista de vertices
    vertices = list(g.vertices)

    #ordena os vertices por ordem crescente de grau
    sorted(vertices, cmp=compare, reverse=True)

    #transforma a lista em uma fila
    vertices = deque(vertices)

    i = 0

    while vertices:
        #pega o primeiro vertice da fila
        v = vertices.popleft()

        #variavel de controle
        tem_cor = false

        #verifica se algum dos vertices adjacentes tem a cor
        for adj in v.edges:
            if adj.cor is i:
                tem_cor = true

        #se nenhum dos adjacentes tem aquela cor, preenche com a cor
        if not tem_cor:
            v.cor = i

        #atualiza i
        i += 1

        #se atingiu o numero maximo de cores, reinicia
        if i >= (g.n * g.n):
            i = 0

        #se v ainda nao foi colorido ele retorna pro começo da fila
        if v.cor is -1:
            vertices.appendleft(v)




"""
Algoritmo Ingênuo Melhorado
função Col_ingenuo(G : grafo): Grafo colorido
Ordenar os vértices de G em ordem decrescente de grau
i := 1
Enquanto G contém vértices não coloridos
    Para Cada vértice vde G não colorido:
        Se Nenhum vértice adjacente a v possui a cor i:
            Atribuir cor iao vértice v
            i := i + 1
Retornar G
"""
