from pymongo import MongoClient

#Conecta com o MongoDB
client = MongoClient('localhost', 27017)
#Define o banco em uso
db = client['test']
prog_list = [
  {
    'Nome:':'Kraftwerk',
    'País':'Alemanha',
    'Albuns': ['Radioactivity','Trans Europe Express']
  },
  {
    'Nome:':'Genesis',
    'País':'Inglaterra',
    'Albuns': ['Foxtrot','The Nursery Crime']
  },
]

#Define a coleção a ser usada
progs = db.progs
#Limpa a coleção
progs.remove({})

#Insere os registros
ids = progs.insert(prog_list)
#Identificadores automaticamente gerados pelo MongoDB
print(ids)

#find_one() localiza o primeiro item na coleção que atenda aos parametros
print(progs.find_one())
print(progs.find_one({'País':'Inglaterra'}))

#find() retorna um iterador com todos os itens que atendem aos parametros
print(list(progs.find({'País':'Inglaterra'})))
