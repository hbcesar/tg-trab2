# -*- coding: utf-8 -*-
class Vertice(object):
	def __init__(self, name, line, column, n):
		self.name = name
		self.edges = []
		self.grau = 0
		self.line = line
		self.column = column
		self.status = False
		self.colors = range(n*n)

	def adjacente(self, n):
		self.edges.append(n)
		self.grau += 1

	def colorir(self, color):
		self.colors = color
		self.status = True
