import calc
import os

l = [23,54,31,77,12,34]

print(calc.media(l))

print(os.name)
#Entrada de um usuário
temp = int(input('Entre com a temperatura: '))

#Estrutura de Condição
if temp <0:
	print('Congelando...')
elif 0 <= temp <= 20:
	print('Frio')
elif 21 <= temp <= 25:
	print('Normal')
else:
	print('Muito quente!')

#Estrutura de repetição
#COM FOR
s = 0

for x in range(1,100):
	s = s + x
print(s)

#Com WHILE
s = 0 
x = 1
while x < 100:
	s = s + x
	x = x + 1
print(s)

#Convertendo de real para inteiro
print('int(3.14)', int(3.14))

#Convertendo de inteiro para real
print('float(5)', float(5))

#Cálculo entre inteiro e real resulta em real
print('5.0 / 2 + 3 =', 5.0 / 2 + 3)

#Inteiro em outra base
print("int('20',8) =", int('20',8)) #base 8
print("int('20',16) =", int('20',16)) #base 16

#Operadores com números complexos
c = 3 + 4j
print('c =', c)
print('Parte real:', c.real)
print('Parte imaginária:', c.imag)
print('Conjugado:', c.conjugate())

s = 'Thiago'

#Concatenação
print('The' + s + ' run away')

#Interpolação
print('tamanho de %s => %d' % (s, len(s)))

#String tratada como sequência
for ch in s: print(s.upper())

#O que acontecerá
print(3 * s)

#Simbolos usados para Interpolaçãp
'''
%s: String
%d: inteiro
%o: octal
%x: hexadecimal
%f: real
%e: real exponencial
%%: sinal de porcentagem
'''

#Zeros a esquerda
print('Agora são %02d:%02d.' %(16,30))

#Real (números após o ponto controla as casas decimais)
print('Porcentagem: %.1f%%, Exponencial:%.2e' % (5.333, 0.00314))

#Octal para Hexadecimal
print('Decimal: %d, Octal: %o, Hexadecimal: %x' %(10, 10, 10))

musicos = [('Page','guitarrista','Led Zeppelin'), ('Frip','guitarrista','King Crimson')]

#Parametros identificados pela ordem
msg = '{0} é {1} do {2}'

for nome, funcao, banda in musicos:
	print(msg.format(nome, funcao, banda))

#Parametros identificado por nome
msg = '{saudacao}, são {hora:02d}:{minuto:02d}'
print(msg.format(saudacao='Bom dia', hora=7, minuto=30))

#Função builtin format()
print('Pi =', format(3.14159, '.3e'))

#Manipulação de string
print('Python'[::-1])
#Mostra: nohtyP

import string

#O alfabeto
a = string.ascii_letters
print(a)

#Rodando o alfabeto um caractere para a esquerda
b = a[1:] + a[0]

#A função maketrans() cria uma tabela de tradução
#entre os caracteres das duas strings que ela
#recebeu como parametro
#Os caracteres ausentes nas tabelas serão
#copiados para a saída

tab = str.maketrans(a,b)

#A mensagem
msg = '''Esse texto será traduzido...Vai ficar bem estranho.'''

#A função translate() usa a tabela de tradução
# criada pela maketrans() para traduzir uma string
print(msg.translate(tab))

#Cria uma string template
st = string.Template('$aviso aconteceu em $quando')

#Preenche o modelo com um dicionario
s = st.substitute({'aviso':'Falta de eletricidade','quando': '03 de Abril de 2002'})

#Mostra:
#Falta de eletricidade aconteceu em 03 de Abril de 2002
print(s)

s = bytearray(b'Python')
s[0] = ord('p')
print(s.decode())

#String unicode
u = 'Hüsker Dü'

#Convertendo para bytes
s = u.encode('latin1')
print(s, '=>', type(s))

#Bytes para unicode
s = bytes('Hüsker Dü', 'latin1')
u = s.decode('latin1')
print(u, '=>', type(u))

#LISTA

#Uma nova lista: Brit Progs dos anos 70
progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']

#Varrendo a lista inteira
for prog in progs:
	print(prog)

#Trocando o último elemento
progs[-1] = 'King Crimson'

#Incluindo
progs.append('Camel')

#Removendo
progs.remove('Pink Floyd')

#Ordena a lista
progs.sort()

#Invertando a lista
progs.reverse()

#Imprime numerado
for i, prog in enumerate(progs):
	print(i + 1, '=>', prog)

#Imprime do segundo item em diante
print(progs[1:])

lista = ['A','B','C']
print('lista:', lista)

#A lista vazia é avaliada como falsa
while lista:
	#Em filas, o primeiro item é o primeiro a sair
	#pop(0) remove e retorna o primeiro item
	print('Saiu', lista.pop(0), ' faltam', len(lista))

#Mais itens na lista

lista += ['D','E','F']
print('lista:', lista)

while lista:
	#Em pilhas,primeiro item é o ultimo a sair
	#pop() remove e retorna o último item
	print('Saiu', lista.pop(), ', faltam', len(lista))

#TUPLA

#Lista podem ser convertidas a tuplas
# tupla = tuple(lista)

#Tuplas podem ser convertidas a lista
# lista = list(tupla)

t = ([1,2],4)
t[0].append(3)
print(t)

#set: sequencia mutável unívoca (sem repetições) não ordenada
#frozenset: sequência imutável unívoca não ordenada

#Conjunto de Dados
s1 = set(range(3))
s2 = set(range(10, 7, -1))
s3 = set(range(2, 10, 2))

#Exibe os dados
print('s1:', s1, '\ns2:', s2, '\ns3', s3)

#União
s1s2 = s1.union(s2)
print('União de s1 e s2:', s1s2)

#Diferença
print('Diferença com s3:', s1s2.difference(s3))

#Intersecção
print('Intersecção com s3:', s1s2.intersection(s3))

#Testa se um st inclui outro
if s1.issubset([1, 2]):
	print('s1 inclui 1 e 2')

#Testa se não existe elementos em comum
if s1.isdisjoint(s2):
	print('s1 e s2 não tem elementos em comum')

#Quando uma lista é convertida para set, as repetições são descartadas

#DICIONARIO

dic = {'nome': 'Shirley Manson', 'banda': 'Garbage'}

#Acessando elementos:
print('Nome', dic['nome'])

#Adicionando elementos
dic['album'] = 'Version 2.0'

#Apagando um elemento do dicionário
del dic['album']

#Obtendo od itens, chaves e valores:
print('itens', dic.items())
print('chaves', dic.keys())
print('valores', dic.values())

#Exemplo com dicionarios

#Progs e seus albuns
progs = {'Yes': ['Close to The Edge', 'Fragile'],
	'Genesis': ['Foxtrot', 'The Nursery Crime'],
	'ELP': ['Brain Salad Surgery']}

#Mais progs
progs['King Crimson'] = ['Red', 'Discipline']

#items() retorna uma lista
#tuplas com a chave e o valor
for prog, albuns in progs.items():
	print(prog, '=>', albuns)

print(len(progs), 'bandas')

#Se tiver 'ELP' deleta
if 'ELP' in progs:
	del progs['ELP']

print('Aagora', len(progs), 'bandas')

#MATRIZ

#matriz esparsa é uma estrutura é uma estrutura
#que só armazena os valores que existem na matriz

dim = 6,12
mat = {}

#Tuplas são imutaveis
#Cada tupla representa
#uma posição na matriz

mat[3,7] = 3
mat[4,6] = 5
mat[6,3] = 7
mat[5,4] = 6
mat[2,9] = 4
mat[1,0] = 9

for lin in range(dim[0]):
	for col in range(dim[1]):
		#Metodo get(chave, valor)
		#retorna o valor da chave
		#no dicionario ou se a chave
		#não existir, retorna o
		#segundo argumento
		print(mat.get((lin,col),0), end=' ')
	print()

#Matriz em forma de string
matriz = '''000000000000
			900000000000
			000000000400
			000000030000
			000000500000
			000060000000'''

mat = {}

#Quebra a matriz em linhas
for lin, linha in enumerate(matriz.splitlines()):
	#Quebra a linha em colunas
	for col, coluna in enumerate(linha.split()):
		coluna = int(coluna)
		#Coloca a coluna no resultado,
		#se for diferente de zero
		if coluna:
			mat[lin, col] = coluna
print(mat)

#Some um nas dimensões pois a contagem começa em zero
print('Tamanho da matriz completa:', (lin+1) * (col + 1))
print('Tamanho da matriz esparsa:', len(mat))

#FUNÇOES
def fatorial(num):
	if num <= 1:
		return 1
	else:
		return(num * fatorial(num - 1))

#Testando fatorial()
print(fatorial(5))

#Fibonacci

def fib(n):
	"""Fibonacci:
	fib(n) = fib(n - 1) + fib(n - 2) se n > 1
	fib(n) = 1 se n <= 1
	"""

	if n > 1:
		return fib(n - 1) + fib(n - 2)
	else:
		return 1

#Mostra os primeiros elementos de Fibonacci
for i in range(6):
	print(i, '=>', fib(i))

#Conversão de RGB
def rgb_html(r=6, g=0, b=0):
	"""Converte R,G,B em #RRGGBB"""
	return '#%02x%02x%02x' % (r,g,b)

def html_rgb(color='#000000'):
	'''Converte #RRGGBB em R,B,G'''
	if color.startswith('#'): color = color[1:]

	r = int(color[:2], 16)
	g = int(color[2:4], 16)
	b = int(color[4:], 16)
	return r,g,b #Uma sequencia

print(rgb_html(200,200,255))
print(rgb_html(b=200, g=200, r=255)) #O que houve?
print(html_rgb('#c8c8ff'))