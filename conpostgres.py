try:
	import psycopg2
except:
	print('Instale a dependencia de conexão do postgres (psycopg2) antes da execução do sistema!')
	raise SystemExit

#Para bancos de dados locais (via Unix Domain Sockets)
#con = psycopg2.connect(database='music')

#Via TCP/IP
con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='bakuman10')

cur = con.cursor()

#Cria uma tabela
sql = 'create table tracks '\
	'(id serial primary key, '\
	'track varchar(100), '\
	'band varchar(100))'

cur.execute(sql)

#O comando de inclusão usa interpolação
sql = 'insert into tracks values (default, %s, %s)'

#Dados
recset = [('Kashmir', 'Led Zeppelin'), ('Starless', 'King Crimson')]

#Insere os registros
for rec in recset:
	cur.execute(sql, rec)

con.commit()
cur.execute('select * from tracks')
recset = cur.fetchall()

#Mostra
for rec in recset:
	print(rec)

con.close()