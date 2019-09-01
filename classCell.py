class Cell(object):
	"""
	Classe para céduka de planilha
	"""
	def __init__(self, formula='""', format='%s'):
		"""
		Inicializa a célula
		"""
		self.formula = formula
		self.format = format
	
	def __repr__(self):
		"""
		Retorna a represantação em string da célula
		"""
		return self.format % eval(self.formula)

print(Cell('123**2'))
print(Cell('23*2+2'))
print(Cell('abs(-1.45 / 0.3)', '%2.3f'))