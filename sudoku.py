# -*- coding: utf-8 -*-
#**************************************************************
#           2º Trabalho de Teoria dos Grafos
#              César Henrique Bernabé
#                   João Reis
#
#**************************************************************

import sys
import time
from grafo import Grafo
from welshpowell import WelshPowell
from coloracaolargura import ColoracaoLargura

def main(argv):

	# #chama algoritmo
	# a = WelshPowell()
	a = ColoracaoLargura()

	for i in range(2, 6):
		tempos = 0
		falhas = []
		exatos = 0

		entrada = "entrada%d.txt" % (i)
		for i in range(10):
			# open and read file
			fp = open(entrada, 'r')
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

			#transforma de matriz para lista
			g.vertices = g.verticesArray()

			#roda o algoritmo
			inicio = time.clock()
			a.cl(g)
			# a.wp(g)
			fim = time.clock()

			tempos += fim-inicio

			if g.falhas == 0:
				exatos += 1
			else:
				falhas.append(g.falhas)

		#calcula resultados
		media = 0
		for f in falhas:
			media += f
		if len(falhas):
			media /= len(falhas)
		else:
			falhas.append(0)
		falhas.sort()

		#imprime resultados
		print "--------------- RESULTADOS --------------"
		print "Tempo Médio", tempos/10
		print "Restrições violadas:"
		print "\tMédia:\t", media
		print "\tMelhor:\t", falhas[0]
		print "\tPior:\t", falhas[-1]
		print "Soluções corretas:", exatos

		# #imprime resultado
		# g.imprimir()

if __name__ == '__main__':
	main(sys.argv)
