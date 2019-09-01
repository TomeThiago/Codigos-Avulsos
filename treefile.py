import os

#Encontra arquivos recursivamente
def find(path='.'):
	try:
		listdir = os.listdir(path)
	except PermissionError:
		listdir = []

	for item in listdir:
		fn = os.path.normpath(os.path.join(path, item))
		if os.path.isdir(fn):
			for f in find(fn):
				yield f
		else:
			yield fn

#A cada iteração o gerador devolve
#um novo nome de arquivo
for fn in find('c:/'):
	print(fn)  