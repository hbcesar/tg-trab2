# -*- coding: utf-8 -*-
#**************************************************************
#           2º Trabalho de Teoria dos Grafos
#              César Henrique Bernabé
#                   João Reis
#
#**************************************************************

import sys
from grafo import Grafo
from welshpowell import WelshPowell
from coloracaolargura import ColoracaoLargura

def main(argv):

	# #chama algoritmo
	# a = WelshPowell()
	a = ColoracaoLargura()

	flag = False
	falhas = -1
	# while not flag:
	# open and read file
	fp = open("entrada5.txt", 'r')
	data = fp.read().split('\n')
	data.remove('')

	#pega tamanho do sudoku
	n = int(data[0])
	del data[0]

	#inicializa
	g = Grafo(n)
	g.montar()

	#le elementos estaticos
	for line in data:
		verticeEstatico = line.split(';')
		i = int(verticeEstatico[0])
		j = int(verticeEstatico[1])
		color = int(verticeEstatico[2])
		g.colorir(i, j, color)

	g.vertices = g.verticesArray()

	a.cl(g)

	#
	# #imprime resultado
	g.imprimir()

	print "Falhas", g.falhas
	# g.imprimirExato()


if __name__ == '__main__':
	main(sys.argv)
