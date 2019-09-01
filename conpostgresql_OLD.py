try:
	import postgres
except:
	print('Instale a dependencia de conexão do postgress antes da execução do sistema!')
	raise SystemExit

#Via TCP/IP
db = postgres.open(host='localhost', database='', user='', password='')

#Cria uma tabela
sql = 'create table tracks '\
	'(id serial primary key, '\
	'track varchar(100), '\
	'band varchar(100))'

db.execute(sql)

#O comando de inclusão usa interpolação
sql = db.prepare('insert into tracks values (default, $1, $2)')

#Dados
recset = [('Kashmir', 'Led Zeppelin'), ('Starless', 'King Crimson')]

#Insere os registros
for rec in recset:
	sql(*rec)

#Recupera os registros
qry = db.prepare('select * from tracks')

#Mostra
for rec in qry:
	print(rec)

db.close()