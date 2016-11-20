#**************************************************************
#           2º Trabalho de Teoria dos Grafos
#              César Henrique Bernabé
#                   João Reis
#**************************************************************

import grafo as g
import algoritmo
import sys

def main(argv):
	#inicializa
	g = Grafo(n)
	g.montar()

	#chama algoritmo
	startWelshPowel(g)

	#imprime resultado
	g.imprimir()


if __name__ == '__main__':
    main(sys.argv)
