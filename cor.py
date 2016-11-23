class Cor(object):
	def __init__(self, name):
		self.name = name
		self.instancias = 0

	def update(self):
		self.instancias += 1

	def downgrade(self):
		self.instancias -= 1

	def __lt__(self, other):
		if self.instancias < other.instancias:
			 return -1
		elif self.instancias > other.instancias:
			return 1
		else:
			return 0

	def __str__(self):
		return str(self.name)
