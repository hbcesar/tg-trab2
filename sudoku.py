#**************************************************************
#           2º Trabalho de Teoria dos Grafos
#              César Henrique Bernabé
#                   João Reis
#**************************************************************

import grafo as g
import algoritmo
import sys

def main(argv):


	# open and read file
    fp = open("entrada.txt", 'r')
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
        verticeEstatico = line.split(';'))
		i = int(verticeEstatico[0])
		j = int(verticeEstatico[1])
		color = int(verticeEstatico[2])
		g.colorir(i, j, color)

	#chama algoritmo
	startWelshPowel(g)

	#imprime resultado
	g.imprimir()


if __name__ == '__main__':
    main(sys.argv)
