class Vertice(object):
	def __init__(self, name, line, column):
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

	# def colorir(self, color):
	# 	if not self.imutable:
	# 		self.colors = color

	# def saturacao(self):
	# 	cores = []
	#
	# 	for adj in self.edges:
	# 		if adj.color not in cores:
	# 			cores.append(adj.color)
	#
	# 	return cores.size()
