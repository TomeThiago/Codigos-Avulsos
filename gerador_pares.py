#A sintaxe é semelhante a da função tradicional, 
# só que a instrução yield retorna o próximo valor

def gen_pares():
	"""
	Gera números pares infinitamente
	"""
	i = 0
	while True:
		i += 2
		yield i

#Mostra cada numero e passa para o proximo
for n in gen_pares():
	print(n)