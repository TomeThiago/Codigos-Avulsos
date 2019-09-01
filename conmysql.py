import pymysql

#Cria uma conexão
con = pymysql.connect(db='test', user='root', passwd='')

#Cria um cursor
cur = con.cursor()

#Executa um comando SQL
cur.execute('show databases')

#Recupera o resultado
recordset = cur.fetchall()

#Mostra o resultado
for record in recordset:
	print(record)

#Fecha a conexão
con.close()