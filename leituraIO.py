import sys
import os.path

#input() retorna a string digitada
fn = input('Nome do arquivo: ').strip()

if not os.path.exists(fn):
	print('Tente outra vez...')
	sys.exit()

#Numerando as linhas
for i, s in enumerate(open(fn)):
	print(i + 1, s, end='')

#Imprime uma lista contendo linhas do arquivo
print(open('temp.txt').readlines())