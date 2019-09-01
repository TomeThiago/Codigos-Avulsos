import os
import sys
import platform

def uid():
	"""
		uid() -> retorna a identificação do usuário
		corrente ou None se não for possivel identificar
	"""

	#Variaveis de ambiente para cada
	#sistema operacional
	us = {'Windows': 'USERNAME', 'Linux' : 'USER'}

	u = us.get(platform.system())
	return os.environ.get(u)

print('Usuário:', uid())
print('plataforma:', platform.platform())
print('Diretório corrente:', os.path.abspath(os.curdir))

exep, exef = os.path.split(sys.executable)
print('Executavel:', exef)
print('Diretorio do executavel:', exep)