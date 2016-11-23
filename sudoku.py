# -*- coding: utf-8 -*-
#**************************************************************
#           2º Trabalho de Teoria dos Grafos
#              César Henrique Bernabé
#                   João Reis
# https://medium.com/@random.wicket/solucionador-de-sudoku-com-teoria-dos-grafos-b62a4fa9609b#.hi11719gh
# https://pyladiessanca.gitbooks.io/teoria_dos_grafos_-_ufscar_2015/content/chapter4.html
#**************************************************************

import sys
from grafo import Grafo
from welshpowell import WelshPowell

def main(argv):

	# #chama algoritmo
	a = WelshPowell()

	flag = False
	falhas = -1
	while not flag:
		# open and read file
		fp = open("entrada4.txt", 'r')
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

		flag = a.wp(g)
		falhas += 1

	#
	# #imprime resultado
	g.imprimir()

	print "Falhas", falhas
	# g.imprimirExato()


if __name__ == '__main__':
	main(sys.argv)
