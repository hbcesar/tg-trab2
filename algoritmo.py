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

def algoritmoIngenuo(g):
    #lista de vertices
    vertices = list(g.vertices)

    #ordena os vertices por ordem crescente de grau
    sorted(vertices, cmp=compare, reverse=True)

    #transforma a lista em uma fila
    vertices = deque(vertices)

    #lista de vertices ja coloridos
    colored = []

    while vertices:
        v = vertices.popleft()
        colored.append(v)


"""
Algoritmo Ingênuo Melhorado
função Col_ingenuo(G : grafo): Grafo colorido
Ordenar os vértices de G em ordem decrescente de grau
i := 1
Enquanto G contém vértices não coloridos
    Para Cada vértice vde G não colorido:
        Se Nenhum vértice adjacente a vpossui a cor i:
            Atribuir cor iao vértice v
            i := i + 1
Retornar G
"""
