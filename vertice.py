class Vertice(object):
	def __init__(self, name, line, column, n):
		self.name = name
		self.edges = []
		self.grau = 0
		self.line = line
		self.column = column
		self.status = False
		self.colors = range(n*n)
		self.cor = None

	def adjacente(self, n):
		self.edges.append(n)
		self.grau += 1

	def colorir(self, color):
		self.colors = color
		# self.cor = color
		self.status = True



	# def saturacao(self):
	# 	cores = []
	#
	# 	for adj in self.edges:
	# 		if adj.color not in cores:
	# 			cores.append(adj.color)
	#
	# 	return cores.size()
